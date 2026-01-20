def count_letter(sentence: str, letter: str) -> int:
    """Counts the number of times a letter appears in a sentence."""
    return sentence.lower().count(letter.lower())

def main() -> None:
    sentence = "Hello World, this is a test with several letters E and e"
    letter = "e"
    result = count_letter(sentence, letter)
    print(f"The letter '{letter}' appears {result} times in the sentence:")
    print(sentence)

if __name__ == "__main__":
    main()
