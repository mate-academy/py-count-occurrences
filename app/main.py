def count_occurrences(phrase: str, letter: str) -> int:
    """
        Підраховує кількість символів letter зустрічається у phrase.

        Args:
            phrase (str): Рядок, у якому шукаємо.
            letter (str): Символ або підрядок для пошуку.

        Returns:
            int: Кількість входжень letter у phrase (без урахування регістру).
        """
    return phrase.lower().count(letter.lower())
