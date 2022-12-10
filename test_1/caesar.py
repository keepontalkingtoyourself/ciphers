alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt(message, key):
    res = ""
    for s in message:
        res += alphabet[(key + alphabet.find(s)) % len(alphabet)]
    return res


def get_key(plain_text, encrypted_text):
    return (alphabet.find(encrypted_text[0]) - alphabet.find(plain_text[0]) + 33) % 33


def main():
    print("«Шифр Цезаря")
    action = int(input("[1] Шифровки:\n[2] Расшифровки:\n[3] Найти ключ:\n→ "))

    if action == 1:
        message = input("Текст:\n→ ")
        print()
        for key in range(34):
            print(key, encrypt(message, key))

    elif action == 2:
        message = input("Зашифрованный текст:\n→ ")
        print()
        for key in range(33, -1, -1):
            print(33 - key, encrypt(message, key))

    elif action == 3:
        plain_text = input("Исходный текст:\n→ ")
        encrypted_text = input("Зашифрованный текст:\n→ ")
        print()
        print(f"Результат:\n{get_key(plain_text, encrypted_text)}")


if __name__ == '__main__':
    main()
