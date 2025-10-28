def count_occurrences(phrase: str, letter: str) -> int:

    answer = 0
    for char in phrase.lower():
        if char in letter.lower():
            answer += 1
    return answer
