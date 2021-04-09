def generateKey (originalkey: str, plainText: str):
    newKey = originalkey
    if (len(originalkey) != len(plainText)):
        for i in range(0,(len(plainText) - len(originalkey))):
            newKey += plainText[i]
    return newKey

def VernamCipher(key: str, plainText: str):
    ciphertext = ""
    for i in range(0, len(plainText)):
        text = 0
        if (ord(key[i]) - 97) < 0:          # cpital letter
            text += ord(key[i]) - 65
        else:
            text += ord(key[i]) - 97
        if (ord(plainText[i]) - 97) < 0:    # cpital letter
            text += ord(plainText[i]) - 65
        else:
            text += ord(plainText[i]) - 97
        text %= 26
        ciphertext += chr(text + 97)
    return ciphertext

while True:
    try:
        k = input()
        s = input()
        print(VernamCipher(generateKey(k, s), s))
    except:
        break