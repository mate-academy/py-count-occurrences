def count_occurrences(phrase: str, letter: str) -> int:
    # write your code here
    if len(letter) != 1:
        raise ValueError("The letter parameter must be a single character."
                        )
        return phrase.lower().count(letter.lower())
