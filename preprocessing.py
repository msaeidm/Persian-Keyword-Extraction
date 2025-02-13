# -*- coding: utf-8 -*-
import re

def normalize_persian_text(text):
    # Convert Arabic characters to Persian
    text = text.replace('ي', 'ی').replace('ك', 'ک')
    
    # Remove diacritics (e.g., fathah, kasrah)
    text = re.sub(r'[\u064B-\u065F]', '', text)
    
    # Attach prefixes/suffixes (e.g., "می" to verbs)
    text = re.sub(r'\bمی\s+', 'می‌', text)
    
    # Normalize spaces and half-spaces
    text = text.replace('\u200c', '‌')  # Replace half-space
    return text

# Example usage:
input_text = "می رود به کتابخانه ها"
normalized_text = normalize_persian_text(input_text)
print(normalized_text)  # Output: "میرود به کتابخانه‌ها"
