def count_occurrences(phrase: str, letter: str) -> int:
    """Count occurrences of a letter in a phrase (case insensitive)."""
    return phrase.lower().count(letter.lower())


if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    letter = input("Enter a letter to count: ")
    occurrences = count_occurrences(phrase, letter)
    print(f'The letter "{letter}" occurs {occurrences} times in the phrase.')
