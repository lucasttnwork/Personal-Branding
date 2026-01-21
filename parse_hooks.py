import re
import json

def parse_hooks(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Join all lines with spaces first
    raw_text = " ".join([line.strip() for line in lines if line.strip()])
    
    # Fix very specific link splits that are unambiguous
    # https://... / reels / -> https://.../reels/
    raw_text = re.sub(r'(https?://[^\s]+)\s+(utm_source|igsh|ZA==|h=|sh=)', r'\1\2', raw_text)
    
    # Regex for links - stop at space
    link_pattern = r'https?://(?:www\.)?[\w\-\./%?=&]+'
    
    matches = list(re.finditer(link_pattern, raw_text))
    
    results = []
    current_category = "EDUCATIONAL"
    last_pos = 0
    
    for match in matches:
        link = match.group(0)
        # Clean the link
        link = re.sub(r'[,\.\?!\(\) ]+$', '', link)
        
        text_before = raw_text[last_pos:match.start()].strip()
        
        # Category detection
        cat_match = re.search(r'([A-Z\s]{5,})\sINSPO HOOK:', text_before)
        if cat_match:
            current_category = cat_match.group(1).strip()
            text_before = text_before[cat_match.end():].strip()
        
        # Cleanup
        text_before = re.sub(r'(1000|[\d,]+)\s+VIRAL\s+HOOKS', '', text_before, flags=re.I).strip()
        
        if text_before:
             text_before = " ".join(text_before.split())
             text_before = re.sub(r'^[\.\- ]+', '', text_before)
             
             results.append({
                 "category": current_category,
                 "hook": text_before,
                 "inspo_hook": link
             })
        
        last_pos = match.end()

    return results

if __name__ == "__main__":
    input_file = "/Users/lucasttn/Documents/Documents/Antigravity - Projects/Personal Branding/teste.md"
    output_file = "/Users/lucasttn/Documents/Documents/Antigravity - Projects/Personal Branding/viral_hooks.json"
    
    hooks = parse_hooks(input_file)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(hooks, f, indent=4, ensure_ascii=False)
    
    print(f"Successfully extracted {len(hooks)} hooks to {output_file}")
