def count_occurrences(phrase: str, letter: str) -> int:
    phrase_lower = phrase.lower()
    letter_lower = letter.lower()
    if letter_lower == "":
        return 0
    else:
        return phrase_lower.count(letter_lower)


print(count_occurrences("Thierry", "r"))  # Output: 2
print(count_occurrences("Yorka", "Y"))  # Output: 1
print(count_occurrences("Tcheck_vi", "z"))  # Output: 0
