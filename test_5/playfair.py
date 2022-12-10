
def cipher1(Matrix, char1, char2):
    idx1 = Matrix.index(char1)
    idx2 = Matrix.index(char2)
    idxs1 = [idx1//6, idx1 % 6]
    idxs2 = [idx2//6, idx2 % 6]

    if idxs1[0] == idxs2[0]:
        res1 = [idxs1[0], (idxs1[1]+1) % 6]
        res2 = [idxs2[0], (idxs2[1]+1) % 6]
    elif idxs1[1] == idxs2[1]:
        res1 = [(idxs1[0]+1) % 6, idxs1[1]]
        res2 = [(idxs2[0]+1) % 6, idxs2[1]]
    else:
        if idxs1[0] < idxs2[0] and idxs1[1] < idxs2[1]:
            res1 = [idxs1[0], idxs2[1]]
            res2 = [idxs2[0], idxs1[1]]
        elif idxs1[0] > idxs2[0] and idxs1[1] < idxs2[1]:
            res1 = [idxs2[0], idxs1[1]]
            res2 = [idxs1[0], idxs2[1]]
        elif idxs1[0] < idxs2[0] and idxs1[1] > idxs2[1]:
            res1 = [idxs2[0], idxs1[1]]
            res2 = [idxs1[0], idxs2[1]]
        else:
            res1 = [idxs1[0], idxs2[1]]
            res2 = [idxs2[0], idxs1[1]]

    return res1, res2


def cipher2(Matrix, char1, char2):
    idx1 = Matrix.index(char1)
    idx2 = Matrix.index(char2)
    idxs1 = [idx1//6, idx1 % 6]
    idxs2 = [idx2//6, idx2 % 6]

    if idxs1[0] == idxs2[0]:
        res1 = [idxs1[0], (idxs1[1]-1) % 6]
        res2 = [idxs2[0], (idxs2[1]-1) % 6]
    elif idxs1[1] == idxs2[1]:
        res1 = [(idxs1[0]-1) % 6, idxs1[1]]
        res2 = [(idxs2[0]-1) % 6, idxs2[1]]
    else:
        if idxs1[0] < idxs2[0] and idxs1[1] < idxs2[1]:
            res2 = [idxs1[0], idxs2[1]]
            res1 = [idxs2[0], idxs1[1]]
        elif idxs1[0] > idxs2[0] and idxs1[1] < idxs2[1]:
            res2 = [idxs2[0], idxs1[1]]
            res1 = [idxs1[0], idxs2[1]]
        elif idxs1[0] < idxs2[0] and idxs1[1] > idxs2[1]:
            res2 = [idxs2[0], idxs1[1]]
            res1 = [idxs1[0], idxs2[1]]
        else:
            res2 = [idxs1[0], idxs2[1]]
            res1 = [idxs2[0], idxs1[1]]

    return res1, res2


def encrypt(message, key):
    Alphabet = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,')
    Matrix = []
    key = list(key)
    ciphertext = ''

    for el in key:
        if el in Alphabet:
            Matrix.append(el)
            Alphabet.remove(el)
    Matrix.extend(Alphabet)
    # print(Matrix)

    l = len(message)

    for i in range(0, l-1, 2):
        char1, char2 = message[i], message[i+1]

        if char1 == char2:
            message = message[:i+1] + 'Ъ' + message[i+1:]
            char2 = 'Ъ'

        res1, res2 = cipher1(Matrix, char1, char2)

        ciphertext += Matrix[res1[0]*6 + res1[1]]
        ciphertext += Matrix[res2[0]*6 + res2[1]]

    if len(message) % 2 != 0:
        res1, res2 = cipher1(Matrix, message[-1], 'Ъ')
        ciphertext += Matrix[res1[0]*6 + res1[1]]
        ciphertext += Matrix[res2[0]*6 + res2[1]]

    return ciphertext


def decrypt(message, key):
    '''
            Similar to ciphering but while we can reverse
            res1 and res2 in the outer else case and get a
            correct result (hence the change), the special
            cases need to be shifted the opposite way
    '''

    Alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_.,'
    Alphabet = list(Alphabet)
    Matrix = []
    key = list(key)
    plaintext = ''

    for el in key:
        if el in Alphabet:
            Matrix.append(el)
            Alphabet.remove(el)
    Matrix.extend(Alphabet)

    l = len(message)

    for i in range(0, l, 2):
        char1, char2 = message[i], message[i+1]
        res1, res2 = cipher2(Matrix, char1, char2)

        plaintext += Matrix[res1[0]*6 + res1[1]]
        plaintext += Matrix[res2[0]*6 + res2[1]]

    if plaintext[-1] == "Ъ":
        plaintext = plaintext[:-1]

    return plaintext


def main():
    print("Шифр Плейфейера")
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
