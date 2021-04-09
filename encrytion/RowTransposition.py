def RowTransposition(key: str, message: str):
    text = message.replace(' ','')
    ciphertext = ""
    order = []
    for i in range(len(key)):
        order.append(0)
    for i in range(len(key)):
        index = ord(key[i]) - 48 - 1
        order[index] = i
    for orderNum in order:
        index = orderNum
        while(index < len(text)):
            ciphertext += text[index].lower()
            index += len(key)
    return ciphertext


while True:
    try:
        k = input()
        s = input()
        print(RowTransposition(k, s))
    except:
        break