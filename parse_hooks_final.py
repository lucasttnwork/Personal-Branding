import json
import re

def preprocess_content(content):
    """
    Preprocess the content to fix broken lines from PDF export.
    This joins lines that were incorrectly split.
    """
    # First pass: join URL lines that were split
    # Pattern: URL ending without proper termination + next line that's clearly URL continuation

    lines = content.split('\n')
    result = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # If this line has an Instagram URL
        if 'instagram.com' in line:
            # Keep joining next lines while they look like URL continuations
            while i + 1 < len(lines):
                next_line = lines[i + 1].strip()

                # Skip empty lines
                if not next_line:
                    break

                # Check if next line is URL continuation:
                # - Short, no spaces, looks like URL part
                # - OR starts with common URL parameters
                # - OR is a URL ID fragment with optional space before /
                next_line_cleaned = next_line.replace(' ', '')  # Remove spaces for URL parts
                is_url_continuation = (
                    (re.match(r'^[A-Za-z0-9_=/-]+$', next_line_cleaned) and len(next_line_cleaned) < 50) or
                    next_line.startswith(('h=', 'gsh=', 'igsh=', 'm_source=', 'utm_'))
                )

                # But NOT if it looks like a new hook (has regular words)
                looks_like_text = bool(re.search(r'[a-z]{3,}\s+[a-z]{3,}', next_line.lower()))

                if is_url_continuation and not looks_like_text:
                    line = line.rstrip() + next_line_cleaned  # Use cleaned version
                    i += 1
                else:
                    break

            result.append(line)
        else:
            result.append(line)

        i += 1

    return '\n'.join(result)


def clean_hook_text(text):
    """Clean URL fragments and parameters from hook text"""
    # Remove URL parameters that leaked into hook text
    text = re.sub(r'm_source=ig_web_copy_link[^\s]*', '', text)
    text = re.sub(r'utm_source=[^\s]*', '', text)
    text = re.sub(r'igsh=[^\s]*', '', text)
    text = re.sub(r'\b[A-Za-z0-9_-]{10,}==\s*', '', text)

    # Remove URL ID fragments like "9DfdMgZ_ /" at start
    text = re.sub(r'^[A-Za-z0-9_-]{5,}\s*/\s*', '', text)

    # Clean multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def parse_hooks_from_md(input_file, output_file):
    """Parse hooks from teste.md and convert to structured JSON"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Preprocess to fix broken lines
    content = preprocess_content(content)

    # Find all categories using pattern "CATEGORY INSPO HOOK:"
    category_pattern = r'([A-Z][A-Z\s]+)\s*INSPO HOOK:'
    category_matches = list(re.finditer(category_pattern, content))

    hooks_data = []
    hook_number = 1

    for idx, match in enumerate(category_matches):
        category = match.group(1).strip()

        # Get section content
        start = match.end()
        end = category_matches[idx + 1].start() if idx + 1 < len(category_matches) else len(content)
        section = content[start:end]

        # Find all Instagram URLs in this section
        url_pattern = r'https://www\.instagram\.com/[^\s]+'
        url_matches = list(re.finditer(url_pattern, section))

        prev_end = 0
        for url_match in url_matches:
            # Get text before this URL (that's the hook)
            hook_text = section[prev_end:url_match.start()].strip()
            url = url_match.group(0)

            # Clean the hook text
            hook_text = clean_hook_text(hook_text)

            # Remove line breaks within hook
            hook_text = ' '.join(hook_text.split())

            if hook_text:
                hooks_data.append({
                    "number": str(hook_number),
                    "category": category,
                    "hook": hook_text,
                    "inspo_hook": url
                })
                hook_number += 1

            prev_end = url_match.end()

    # Write to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(hooks_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Processed {len(hooks_data)} hooks")
    print(f"📄 Output saved to: {output_file}")

    # Category summary
    categories = {}
    for hook in hooks_data:
        cat = hook['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n📊 Hooks by category:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count} hooks")

    # Show samples
    print("\n📝 Sample hooks:")
    for h in hooks_data[:8]:
        print(f"   #{h['number']} [{h['category']}]")
        print(f"      Hook: {h['hook'][:70]}...")
        print(f"      URL: {h['inspo_hook'][:60]}...")
        print()


if __name__ == "__main__":
    parse_hooks_from_md("teste.md", "viral_hooks_structured.json")
