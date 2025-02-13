from collections import defaultdict

def select_keywords(combinations, top_n=5):
    frequency = defaultdict(int)
    for combo in combinations:
        frequency[combo] += 1
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:top_n]

# Example output: [("پردازش-زبان", 8), ("کلیدواژه-متن", 6)]
