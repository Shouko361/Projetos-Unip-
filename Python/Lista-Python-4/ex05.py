numero = ''
soma = 0
frase = input('Digite uma frase contendo números: ')
for c in frase:
    if c.isnumeric():
        numero += c
    elif numero != '':
        soma += int(numero)
        numero = ''
if numero != '':
    soma += int(numero)

print(f'A soma dos números presentes na frase é igual a {soma}')
