def count_occurrences(phrase: str, letter: str) -> int:
    # Convert both to lowercase to make the comparison case-insensitive
    phrase = phrase.lower()
    letter = letter.lower()
    
    # Use the built-in count() method to count occurrences
    return phrase.count(letter)
