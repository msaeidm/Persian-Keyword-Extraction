# -*- coding: utf-8 -*-
from hazm import POSTagger, Stemmer  # Requires Hazm library

def generate_combinations(text):
    tagger = POSTagger(model='resources/postagger.model')
    stemmer = Stemmer()
    
    # Tokenize and tag words
    words = text.split()
    tagged = tagger.tag(words)
    
    # Extract nouns/adjectives and create combinations
    combinations = []
    for i in range(len(tagged)):
        if tagged[i][1] in ['N', 'AJ']:
            for j in range(i+1, len(tagged)):
                if tagged[j][1] in ['N', 'AJ']:
                    combo = f"{tagged[i][0]}-{tagged[j][0]}"
                    combinations.append(stemmer.stem(combo))
    return combinations

# Example output: ["کتاب-کتابخانه", "علمی-مقاله"]
