def count_occurrences(phrase: str, letter: str) -> int:
    number = 0
    for i in phrase:
        if letter.lower() == i.lower() and letter != '':
            number += 1
    return number

if __name__ == "__main__":
    count_occurrences('hello', ' ')
    count_occurrences("letter", "t")
    count_occurrences("abc", "a")
    count_occurrences("ABC", "a")
    count_occurrences("abc", "d")
    count_occurrences("abc ", "aa")

