def generateKeyMatrix(key: str):
    letters = []
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']
    for i in key:
        if i not in letters:
            letters.append(i)
    for i in alphabet:
        if i not in letters:
            letters.append(i)

    keyMatrix = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(letters[i * 5 + j])
        keyMatrix.append(row)

    return keyMatrix

def encryptPlayfairCipher(keyMatrix, letter1, letter2):
    row1, col1, row2, col2 = 0, 0 ,0 ,0
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == letter1:
                row1 = i
                col1 = j
            if keyMatrix[i][j] == letter2:
                row2 = i
                col2 = j
    if row1 == row2:
        return keyMatrix[row1][(col1 + 1) % 5] + keyMatrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return keyMatrix[(row1 + 1) % 5][col1] + keyMatrix[(row2 + 1) % 5][col2]
    else:
        return keyMatrix[row1][col2] + keyMatrix[row2][col1]


def PlayfairCipher(key: str, message: str):
    plainText = message.replace('J','I')    # I & J 視為相同
    newKey = key.replace('J','I')
    keyMatrix = generateKeyMatrix(newKey)
    ciphertext = ''
    current = 0
    while(current < len(plainText)):
        if current == len(plainText) - 1:   # 最後只剩一個
            ciphertext += encryptPlayfairCipher(keyMatrix, plainText[current], 'X')
            current += 1
        elif (plainText[current] == plainText[current + 1]):    # pair中的兩個字相同
            ciphertext += encryptPlayfairCipher(keyMatrix, plainText[current], 'X')
            current += 1
        else:
            ciphertext += encryptPlayfairCipher(keyMatrix, plainText[current], plainText[current + 1])
            current += 2
    return ciphertext

while True:
    try:
        k = input()
        s = input()
        k = k.upper()
        s = s.upper()
        print(PlayfairCipher(k, s))
    except:
        break