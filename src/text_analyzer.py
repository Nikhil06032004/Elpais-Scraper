import re
from collections import Counter


def analyze_repeated_words(titles):
    """
    Analyze repeated words across translated titles.
    Prints words appearing more than 2 times.
    """

    print("\n==============================")
    print("Repeated Words Analysis (More than 2 occurrences)")

    all_words = []

    for title in titles:
        words = re.findall(r'\b[a-zA-Z]+\b', title.lower())
        all_words.extend(words)

    counter = Counter(all_words)

    repeated_found = False

    for word, count in counter.items():
        if count > 2:
            print(f"{word} → {count} times")
            repeated_found = True

    if not repeated_found:
        print("No words repeated more than twice.")
