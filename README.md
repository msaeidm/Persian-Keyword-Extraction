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
