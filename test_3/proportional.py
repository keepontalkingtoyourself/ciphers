from bs4 import BeautifulSoup

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"


def parse(text):
    soup = BeautifulSoup(text, "html.parser")
    allSpans = soup.findAll("span")
    data = []
    for span in allSpans:
        data.append(span.text)

    return data


def clean_data(data):
    res = {}
    last_letter = ""

    for el in data:
        if el in alphabet:
            res[el] = []
            last_letter = el
        elif el.isnumeric():
            res[last_letter].append(el)

    return res


def encrypt(message, code_table):
    res = ""
    letter_cnt = dict(zip(alphabet, [0] * len(alphabet)))

    for letter in message:
        res += code_table[letter][letter_cnt[letter] % len(code_table[letter])]
        letter_cnt[letter] += 1

    return res


def decrypt(message, code_table):
    res = ""
    message = [message[i:i+3] for i in range(0, len(message), 3)]

    for num in message:
        for letter in alphabet:
            if num in code_table[letter]:
                res += letter
    return res


def main():
    data = []
    with open("table.txt", "r", encoding="utf8") as html_table:
        text = html_table.read()
        data = parse(text)

    code_table = clean_data(data)

    print("Пропорциональный шифр")
    message = input("Текст:\n→ ")
    action = int(input("[1] Зашифровать:\n[2] Расшифровать:\n→ "))

    if action == 1:
        result = encrypt(message, code_table)
    elif action == 2:
        result = decrypt(message, code_table)

    print(f"Результат:\n{result}")


if __name__ == '__main__':
    main()
