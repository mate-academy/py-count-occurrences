def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    count = 0
    for char in phrase_lower:
        if char == letter_lower:
            count += 1
    return count
print(count_occurrences("Thierry", "r"))  # Output: 2
print(count_occurrences("Yorka", "Y"))  # Output: 1
print(count_occurrences("Tcheck_vi", "z"))  # Output: 0
