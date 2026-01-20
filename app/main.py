def count_occurrences(phrase: str, letter: str) -> int:
    # Creating a simple empty counter to use later
    letter_count = 0
    # Adding 1 to every occurrence of letters in a phrase with case sensitivity
    letter_count += sum(1 for char in phrase if char.lower() == letter.lower())
    # Returning the result
    return letter_count
