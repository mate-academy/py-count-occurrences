# app/main.py (Виправлений)

def some_function() -> None:
    print("Start")

    # Змінна x перейменована на описове ім'я
    input_value = 1

    if input_value == 1:
        # Змінна y перейменована на описове ім'я
        result = 5  # W291 виправлено - кінцеві пробіли видалено
        print(result)
