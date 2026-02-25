from typing import Iterator

def fetch_numbers(iterator: Iterator, number: int) -> list:
    result = []
    for _ in range(number):
        result.append(next(iterator))
    return result
