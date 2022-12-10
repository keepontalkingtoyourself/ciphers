import itertools


def encrypt(block, seq):
    res = ''
    for sym in seq:
        res += block[int(sym)-1]
    return res


def decrypt(block, seq):
    res = [0]*len(seq)
    for i, sym in enumerate(seq):
        res[int(sym)-1] = block[i]
    return ''.join(res)


def decode(ctext, ptext):
    l = len(ctext)
    for perms in itertools.permutations(range(1, l+1)):
        seq = ''.join([str(i) for i in perms])
        code = encrypt(ptext, seq)
        if code == ctext:
            print(seq)


def main():
    print("Шифрование методом перестановки с фиксированным периодом")
    action = int(
        input("[1] Зашифровать:\n[2] Расшифровать:\n[3] Узнать ключ\n→ "))

    if action == 1:
        text = input("Текст:\n→ ")
        key = input("Ключ:\n→ ")
        p = input("Период:\n→ ")
        idx = 0
        p = int(p)

        if len(text) % 6 != 0:
            text += "*" * ((len(text) // 6 + 1) * 6 - len(text))

        l = len(text)

        res = ''
        while idx < l-p+1:
            block = encrypt(text[idx:idx+p], key)
            res += block
            idx += p

        res = res.replace("*", "")
        # res += text[len(res):]

        print(f"Результат:\n{res}")

    elif action == 2:
        text = input("Текст:\n→ ")
        key = input("Ключ:\n→ ")
        p = input("Период:\n→ ")
        idx = 0
        p = int(p)
        l = len(text)
        res = ''
        while idx < l-p+1:
            block = decrypt(text[idx:idx+p], key)
            res += block
            idx += p

        res += (len(text) - len(res)) * "*"

        print(f"Результат:\n{res}")
        print("\nВАЖНО: подставь правильное окончание вместо ***")

    elif action == 3:
        ptext = input("Исходный текст:\n→ ")
        ctext = input("Зашифрованный текст:\n→ ")
        p = input("Период:\n→ ")

        p = int(p)
        decode(ctext[:p], ptext[:p])
        decode(ctext[p:p*2], ptext[p:p*2])


if __name__ == '__main__':
    main()
