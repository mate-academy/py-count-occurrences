def demonstrate_mutability():
    # 1. Незмінні об'єкти (Immutable)
    print("--- Immutable Objects (int) ---")
    age = 18
    old_id = id(age)
    print(f"Початковий age: {age}, id: {old_id}")

    age += 1  # Створюється новий об'єкт
    new_id = id(age)
    print(f"Змінений age: {age}, id: {new_id}")
    print(f"Чи змінився id? {old_id != new_id} (Так, бо це новий об'єкт)\n")

    # 2. Змінні об'єкти (Mutable)
    print("--- Mutable Objects (list) ---")
    my_list = [1, 2, 3]
    list_id = id(my_list)
    print(f"Початковий список: {my_list}, id: {list_id}")

    my_list.append(4)  # Об'єкт змінюється на місці
    print(f"Змінений список: {my_list}, id: {id(my_list)}")
    print(f"Чи залишився id тим самим? {list_id == id(my_list)} (Так)\n")

    # 3. Передача у функцію
    print("--- Function behavior ---")

    def modify_objects(lst, string):
        lst.append("new_element")
        string += " appended text"
        print(f"Всередині функції - список: {lst}")
        print(f"Всередині функції - рядок: {string}")

    fruits = ["apple", "banana"]
    text = "Hello"

    print(f"До функції: fruits={fruits}, text='{text}'")
    modify_objects(fruits, text)
    print(f"Після функції: fruits={fruits}, text='{text}'")
    print("Результат: Список змінився поза функцією, а рядок — ні.")


if __name__ == "__main__":
    demonstrate_mutability()
