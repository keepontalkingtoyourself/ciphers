alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt(message):
    res = ""
    for s in message:
        res += alphabet[-alphabet.find(s) - 1]

    return res


def main():
    message = input("Текст:\n→ ")
    print(f"Результат:\n{encrypt(message)}")


if __name__ == '__main__':
    main()
