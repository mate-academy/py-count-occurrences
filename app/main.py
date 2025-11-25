def count_occurrences(phrase: str, letter: str) -> int:
    """
            Cuenta la ocurrencia de una letra (insensible a
            mayúsculas/minúsculas) dentro de una frase.

            Esta función convierte tanto la frase como la letra a minúsculas
            antes de contar, asegurando que la comparación sea insensible a
            la capitalización.

            Args:
                phrase (str): La cadena de texto donde se buscará la letra.
                letter (str): El carácter único a buscar dentro de la frase.
                              Debe ser una cadena de un solo carácter.

            Returns:
                int: El número de veces que 'letter' aparece en 'phrase'.

            Raises:
                TypeError: Si alguno de los argumentos no es de tipo str.
                ValueError: Si el argumento 'letter' tiene una longitud
                diferente a 1.

            Ejemplo:
                >>> count_occurrences("Banana", "a")
                3
                >>> count_occurrences("Geología", "O")
                2
    """

    if not isinstance(phrase, str) or not isinstance(letter, str):
        raise TypeError("Ambos argumentos deben ser strings (str).")

    if len(letter) != 1:
        raise ValueError("El argumento 'letter', debe ser un único carácter.")

    return (phrase.lower().count(letter.lower()))
