alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, key):
    encrypted = ""
    split_message = [
        message[i: i + len(key)] for i in range(0, len(message), len(key))
    ]

    for each_split in split_message:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] +
                      letter_to_index[key[i]]) % len(alphabet)
            encrypted += index_to_letter[number]
            i += 1

    return encrypted


def decrypt(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i: i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            number = (letter_to_index[letter] -
                      letter_to_index[key[i]]) % len(alphabet)
            decrypted += index_to_letter[number]
            i += 1

    return decrypted


def main():
    assert encrypt("ТЕЛЕКОММУНИКАЦИОННЫЕ_СЕТИ",
                   "ГОЛУБИКА") == "ХУЧШЛЧЧМЦЬФЮБЯУОРЬЁШАЪПТЛ"

    assert decrypt("ХУЧШЛЧЧМЦЬФЮБЯУОРЬЁШАЪПТЛ",
                   "ГОЛУБИКА") == "ТЕЛЕКОММУНИКАЦИОННЫЕ_СЕТИ"

    print("«Шифр Виженера»")
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
