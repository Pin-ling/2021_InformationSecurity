def CaesarCipher(message: str): # key = 9
    ciphertext = ""
    for i in range(0, len(message)):
        if ord(message[i]) - 65 in range(26):     # uppercase
            text = ord(message[i]) - 65 + 9
            text %= 26
            ciphertext += chr(text + 97)
        elif ord(message[i]) - 97 in range(26):   # lowercase
            text = ord(message[i]) - 97 + 9
            text %= 26
            ciphertext += chr(text + 97)
        else:
            ciphertext += message[i]
    return ciphertext

while True:
    try:
        s = input()
        if len(s) != 0:
            print(CaesarCipher(s))
    except:
        break