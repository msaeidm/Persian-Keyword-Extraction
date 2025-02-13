# Persian-Keyword-Extraction
A hybrid syntactic-statistical method for extracting keywords from Persian texts.

## Methodology
1. **Preprocessing**: Normalize text (e.g., unify spellings).
2. **Processing**: 
   - POS tagging using Hazm.
   - Generate noun/adjective combinations.
   - Stemming and frequency counting.
3. **Selection**: Pick top 5 combinations by frequency.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   Run the pipeline
from preprocessing import normalize_persian_text
from processing import generate_combinations
from selection import select_keywords

text = open("data/sample_input.txt", encoding="utf-8").read()
normalized = normalize_persian_text(text)
combinations = generate_combinations(normalized)
keywords = select_keywords(combinations)
print(keywords)
