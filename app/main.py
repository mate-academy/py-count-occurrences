def count_occurrences(phrase: str, letter: str) -> int:
    count = 0
    for chart in phrase:
        if chart.lower() == letter.lower():
            count += 1
    return count
