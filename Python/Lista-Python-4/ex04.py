text = input('Texto a ser criptografado: ').upper().replace(' ', '0')

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

s = int(input('Chave: '))
print(encrypt(text, s).replace('f', ' '))
