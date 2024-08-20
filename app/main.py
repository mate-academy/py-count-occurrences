# app/main.py

# Задаємо змінні різних типів даних
integer_value = 123
empty_list = []
greeting_message = "Hi!"
number_list = [1, 2]
number_tuple = (1, 2)
boolean_value = True
key_value_dict = {"key": "value"}
pi_value = 3.14

# Створюємо словник з двома ключами: "mutable" та "immutable"
sorted_variables = {
    "mutable": [
        empty_list,  # Список, що можна змінювати
        number_list, # Ще один список
        key_value_dict  # Словник
    ],
    "immutable": [
        integer_value,  # Ціле число
        greeting_message,  # Рядок
        number_tuple,  # Кортеж
        boolean_value,  # Логічне значення
        pi_value  # Дійсне число
    ]
}

# Виводимо результати
print(sorted_variables)
