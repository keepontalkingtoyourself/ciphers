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
    action = int(input("[1] Показать все шифровки:\n[2] Найти ключ:\n→ "))

    if action == 1:
        message = input("Текст:\n→ ")
        for key in range(34):
            print(key, encrypt(message, key))
    elif action == 2:
        plain_text = input("Исходный текст:\n→ ")
        encrypted_text = input("Зашифрованный текст:\n→ ")
        print(get_key(plain_text, encrypted_text))


if __name__ == '__main__':
    main()
