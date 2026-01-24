def count_occurrences(phrase: str, letter: str) -> int:
    return phrase.lower().count(letter.lower())


if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    letter = input("Enter a letter to count: ")
    occurrences = count_occurrences(phrase, letter)
    print(f'The letter "{letter}" occurs {occurrences} times in the phrase.')

print(count_occurrences("Meu nome é Gustavo", "g"))  # Expected output: 1
print(count_occurrences("Minha gata é laranja", "a"))
