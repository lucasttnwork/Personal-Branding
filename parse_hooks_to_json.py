import json
import re

def parse_hooks_from_md(input_file, output_file):
    """
    Parse hooks from teste.md and convert to structured JSON
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by category markers (lines ending with "INSPO HOOK:")
    sections = re.split(r'---+', content)

    hooks_data = []
    hook_number = 1

    for section in sections:
        section = section.strip()
        if not section:
            continue

        # Extract category name from first line (ends with "INSPO HOOK:")
        lines = section.split('\n')
        category = None

        for i, line in enumerate(lines):
            if 'INSPO HOOK:' in line:
                # Extract category name (everything before "INSPO HOOK:")
                category = line.replace('INSPO HOOK:', '').strip()
                # Start processing hooks from next line
                lines = lines[i+1:]
                break

        if not category:
            continue

        # Process hooks in this category
        current_hook = []
        current_url = None
        collecting_url = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Check if line contains Instagram URL or URL parameters
            if 'instagram.com' in line or (collecting_url and ('=' in line or '/' in line)):
                # Extract URL
                url_match = re.search(r'https://www\.instagram\.com/[^\s]+', line)
                if url_match:
                    current_url = url_match.group(0)
                    collecting_url = True

                    # Check if there's hook text before the URL in the same line
                    text_before_url = line[:url_match.start()].strip()
                    if text_before_url and not any(x in text_before_url for x in ['h=', 'gsh=', 'm_source=']):
                        current_hook.append(text_before_url)
                elif collecting_url and current_url:
                    # This might be a continuation of the URL, append to current_url
                    current_url += line

                # Check if URL seems complete (doesn't end with incomplete parameter)
                if current_url and not current_url.endswith('='):
                    # Save the hook
                    hook_text = ' '.join(current_hook).strip()
                    # Clean up hook text from URL fragments
                    hook_text = re.sub(r'\b(utm_source|igsh|m_source)=[^\s]*', '', hook_text).strip()

                    if hook_text or current_url:
                        hooks_data.append({
                            "number": str(hook_number),
                            "category": category,
                            "hook": hook_text,
                            "inspo_hook": current_url
                        })
                        hook_number += 1

                        # Reset for next hook
                        current_hook = []
                        current_url = None
                        collecting_url = False
            elif not collecting_url:
                # This is part of hook text (only if not collecting URL fragments)
                # Skip URL parameter fragments
                if not any(x in line for x in ['utm_source=', 'igsh=', 'm_source=', 'h=MT', 'gsh=MT']):
                    current_hook.append(line)

        # Save any remaining hook
        if current_hook or current_url:
            hook_text = ' '.join(current_hook).strip()
            if hook_text:  # Only save if there's actual text
                hooks_data.append({
                    "number": str(hook_number),
                    "category": category,
                    "hook": hook_text,
                    "inspo_hook": current_url if current_url else ""
                })
                hook_number += 1

    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(hooks_data, f, indent=4, ensure_ascii=False)

    print(f"✅ Processed {len(hooks_data)} hooks")
    print(f"📄 Output saved to: {output_file}")

    # Print category summary
    categories = {}
    for hook in hooks_data:
        cat = hook['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n📊 Hooks by category:")
    for cat, count in sorted(categories.items()):
        print(f"   {cat}: {count} hooks")

if __name__ == "__main__":
    input_file = "teste.md"
    output_file = "viral_hooks_structured.json"

    parse_hooks_from_md(input_file, output_file)
