alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"

lti = dict(zip(alphabet, range(1, len(alphabet) + 1)))
itl = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    res = ""

    for i, letter in enumerate(message):
        res += itl[(lti[letter] + lti[key[i % len(key)]] - 1) % 34]

    return res


def decrypt(message, key):
    res = ""

    for i, letter in enumerate(message):
        res += itl[(lti[letter] - lti[key[i % len(key)]] - 1) % 34]

    return res


def main():
    message = "ИНФОРМАТИВНЫЙ_СИГНАЛ"
    test = "ЩУЕФЖЭЁГОЩЮАЫЕЗЩИЯЁВ"
    key = "ПЕРЕЦ"

    print("«Шифрование методом гаммирования»")
    message = input("Текст:\n→ ")
    key = input("Ключ:\n→ ")
    action = int(input("[1] Зашифровать:\n[2] Расшифровать:\n→ "))

    if action == 1:
        result = encrypt(message, key)
    elif action == 2:
        result = decrypt(message, key)

    print(f"Результат:\n{result}")


if __name__ == '__main__':
    main()
