def count_occurrences(phrase: str, letter: str) -> int:
    letter_count = 0
    for char in phrase:
        if char == letter.lower():
            letter_count += 1
    return letter_count


if __name__ == "__main__":
    user_phrase = input("Enter a phrase:").lower()
    user_letter = input("Enter a letter:").lower()

    result = count_occurrences(user_phrase, user_letter)
    print(f"The letter '{user_letter}' occurs {result} times in the phrase.")

