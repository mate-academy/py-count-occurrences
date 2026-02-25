from typing import Iterator


class NumberIterator:
    def __init__(self, numbers: list) -> None:
        self.numbers = numbers

    def __iter__(self) -> "NumberIterator":
        self.it = 0
        return self

    def __next__(self) -> int:
        if self.it >= len(self.numbers):
            raise StopIteration
        result = self.numbers[self.it]
        self.it += 1
        return result


def fetch_numbers(iterator: Iterator, number: int) -> list:
    return [next(iterator) for _ in range(number)]
