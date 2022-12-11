def encryptfull(text, rows, cols):
    res = ''
    try:
        for i in range(cols):
            for j in range(rows):
                res += text[i + j*cols]
    except IndexError:
        return res
    else:
        return res


def encryptpartial(text, rows, cols):
    l = len(text)
    r = l // cols
    c = l % cols
    if l <= cols:
        return text
    res = ''
    for i in range(c):
        for j in range(r+1):
            res += text[i + j*cols]  # 1
    for i in range(c, cols):
        for j in range(r):
            res += text[i + j*cols]  # 2
    return res


def decryptpartial(text, rows, cols):
    l = len(text)
    r = l % rows
    c = l // rows
    shift = 0
    res = ''
    if l <= cols:
        return text
    for i in range(c):
        for jj in range(rows):
            if jj < r:
                shift = 0
                wrap = c+1
                j = jj
            else:
                shift = r*(c+1)
                wrap = c
                j = jj-r
            res += text[shift + i + j*wrap]
    for i in range(r):
        res += text[c + i*(c+1)]
    return res


def main():
    print("Шифрование методом перестановки по таблице")
    text = input("Текст:\n→ ")
    cols = input("Кол-во столбцов:\n→ ")
    rows = input("Кол-во строк:\n→ ")
    action = input("[1] Зашифровать:\n[2] Расшифровать:\n→ ")

    rows, cols = int(rows), int(cols)
    l = len(text)
    size = rows*cols
    res = ''

    if action == '1':  # encrypt
        for i in range(0, l - l % size, size):
            res += encryptfull(text[i:i+size], rows, cols)
        if l % size != 0:
            res += encryptpartial(text[l-l % size:], rows, cols)

        print(f"Результат:\n{res}")

    elif action == '2':          # decrypt
        for i in range(0, l - l % size, size):
            res += encryptfull(text[i:i+size], cols, rows)
        if l % size != 0:
            res += decryptpartial(text[l-l % size:], cols, rows)

        print(f"Результат:\n{res}")


if __name__ == '__main__':
    main()
