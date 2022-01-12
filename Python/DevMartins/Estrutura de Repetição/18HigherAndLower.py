qnt = int(input("Insira a quantidade de numeros a serem inseridos: "))
higher = 0
lower = 0

while qnt != 0:
    n1 = int(input("Insira um numero: "))
    if (n1 > higher):
        higher = n1
    elif (n1 < lower):
        lower = n1
    qnt -= 1

print(f'O maior numero é {higher} e o menor numero é {lower}')