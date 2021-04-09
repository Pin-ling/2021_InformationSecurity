def VigenereCipher(key: str, message: str):
    ciphertext = ""
    for i in range(0, len(message)):
        text = 0
        if (ord(message[i]) - 97) < 0:      # uppercase
            text += ord(message[i]) - 65
        else:                               # lower case
            text += ord(message[i]) - 97
        if (ord(key[i % len(key)]) - 97) < 0:   # uppercase
            text += ord(key[i % len(key)]) - 65
        else:                                   # lower case
            text += ord(key[i % len(key)]) - 97
        text %= 26
        ciphertext += chr(text + 97)
    return ciphertext

while True:
    try:
        k = input()
        s = input()
        print(VigenereCipher(k,s))
    except:
        break