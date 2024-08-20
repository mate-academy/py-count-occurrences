def count_occurrences(phrase: str, letter: str) -> int:

    letter_count = 0
    for i in phrase:
        if i == letter.lower():
            letter_count += 1
    return letter_count


phrase = input("Enter a phrase:").lower()
letter = input("Enter a letter:").lower()

count_occurrences(phrase, letter)
