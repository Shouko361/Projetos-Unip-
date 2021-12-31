i = True
gas = 2.5
alcool = 1.9

while i == True:
    i = False
    litro = float(input('Insira o numero de litros vendido: '))
    print('Insira o tipo de combustivel')
    tipo = str(input('G para gasolina e A para Alcool: '))

    if litro <= 20 and tipo == 'G':
        brute = litro*gas
        discount = (4/100)*brute
        value = brute - discount
        print(f'O valor a ser pago é de {value}')
    elif litro > 20 and tipo == 'G':
        brute = litro*gas
        discount = (6/100)*brute
        value = brute - discount
        print(f'O valor a ser pago é de {value}')
    elif litro <= 20 and tipo == 'A':
        brute = litro*alcool
        discount = (3/100)*brute
        value = brute - discount
        print(f'O valor a ser pago é de {value}')
    elif litro > 20 and tipo == 'A':
        brute = litro*alcool
        discount = (5/100)*brute
        value = brute - discount
        print(f'O valor a ser pago é de {value}')
    else:
        print('Erro! Os valores foram inseridos incorretamente, tente novamente.')
        i = True