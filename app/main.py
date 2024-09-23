def count_occurrences(phrase: str, letter: str) -> int:
    return sum([1 for i in range(len(phrase))
                if phrase[i].lower() == letter.lower()])
