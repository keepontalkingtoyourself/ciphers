alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def chiper(message, key):
    message = message.replace("Й", "И")
    message = message.replace("Ё", "Е")

    result = ""

    for i, letter in enumerate(message):
        result += index_to_letter[letter_to_index[letter]
                                  ^ letter_to_index[key[i % len(key)]]]
    return result


def main():
    assert chiper("ИНФОРМАТИВНЫЙ_СИГНАЛ",
                  "ПЕРЕЦ") == "ЖКЭИЫЕЕЯОШВ_ЗЫЕЖЖГЕ_"

    assert chiper("ЖКЭИЫЕЕЯОШВ_ЗЫЕЖЖГЕ_",
                  "ПЕРЕЦ") == "ИНФОРМАТИВНЫИ_СИГНАЛ"

    print("«Шифр Вернама»")
    message = input("Текст:\n→ ")
    key = input("Ключ:\n→ ")
    action = int(input("[1] Зашифровать:\n[2] Расшифровать:\n→ "))

    if action == 1:
        result = chiper(message, key)
    elif action == 2:
        result = chiper(message, key)

    print(f"Результат:\n{result}")


if __name__ == '__main__':
    main()
