

def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())
print(count_occurrences("Hello World", "l"))  # Output: 3
print(count_occurrences("Python Programming", "P"))  # Output: 2
print(count_occurrences("Banana", "z"))  # Output: 0