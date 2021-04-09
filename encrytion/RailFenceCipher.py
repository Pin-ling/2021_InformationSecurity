def RailFenceCipher (key: int, plainText: str):
    ciphertext = ""
    textMatrix = [[] for i in range(0,key)]
    index = 0
    while (index < len(plainText)):
        i = 0
        while i < key - 1 and index < len(plainText):
            textMatrix[i] += plainText[index]
            index += 1
            i += 1
        i = 0
        while i < key - 1 and index < len(plainText):
            textMatrix[key - i - 1] += plainText[index]
            index += 1
            i += 1
    for row in textMatrix:
        for text in row:
            ciphertext += text
    return ciphertext

while True:
    try:
        k = int(input())
        s = input()
        print(RailFenceCipher(k, s))
    except:
        break