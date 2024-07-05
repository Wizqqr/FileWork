def allContacts(filename):
    with open(filename, "r", encoding='utf-8') as f:
        contacts = f.read()
    return contacts

def add_phoneNum(filename):
    name = input("Your name: ")
    surname = input("Your surname: ")

    with open(filename, "a", encoding='utf-8') as f:
        f.write(f"{name} {surname}\n")
    print("Name and Surname are saved")

def change_phoneNum(filename):
    contacts = allContacts(filename)
    if not contacts.strip():
        print("Список контактов пуст")
        return

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")


    line_number = int(input("Введите номер строки, которую хотите заменить: "))

    if 1 <= line_number <= len(lines):
        new_value = input("Введите новое значение для выбранной строки: ")
        lines[line_number - 1] = new_value + "\n"

        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print("Замена выполнена успешно.")
    else:
        print("Некорректный номер строки.")

def delete_phoneNum(filename):
    contacts = allContacts(filename)
    if not contacts.strip():
        print("Список контактов пуст")
        return

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

    line_number = int(input("Введите номер строки, которую хотите удалить: "))

    if 0 <= line_number <= len(lines):
        del lines[line_number - 1]
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print("Контакт был успешно удален! ")
    else:
        print("Пользователь не найден")

def main():
    filename = "numbers.txt"

    while True:
        print("Справочник")
        print("1. Добавить номер телефона")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_phoneNum(filename)
        elif choice == "2":
            change_phoneNum(filename)
        elif choice == "3":
            delete_phoneNum(filename)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 4.")

if __name__ == "__main__":
    main()
