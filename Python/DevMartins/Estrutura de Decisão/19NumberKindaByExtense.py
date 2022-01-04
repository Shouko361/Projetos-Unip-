# Entrada de dados pelo usuario e obtenção de tamanho da variavel
number = input("Digite um numero igual ou menor que 999: ")
qtNumero = len(number)

# Exibições de resultados dependentes das variaveis
if qtNumero == 3:
    centena = number[0]
    dezena = number[1]
    unidade = number[2]
    if number[0] == 0:
        print('Impossivel calcular centena de valor zero')
    elif number[0] == 1:
        if number[1] == 0:
            if number[2] == 0:
                print(f'{centena} Centena')
            elif number[2] == 1:
                print(f'{centena} Centena e {unidade} unidade')
            else:
                print(f'{centena} Centena e {unidade} unidades')
        elif number[1] == 1:
            if number[2] == 0:
                print(f'{centena} Centena e {dezena} dezena')
            elif number[2] == 1:
                print(f'{centena} Centena e {dezena} dezena e {unidade} unidade')
            else:
                print(f'{centena} Centena e {dezena} dezena e {unidade} unidades')
        else:
            if number[2] == 0:
                print(f'{centena} Centena e {dezena} dezenas')
            elif number[2] == 1:
                print(f'{centena} Centena e {dezena} dezenas e {unidade} unidade')
            else:
                print(f'{centena} Centena e {dezena} dezenas e {unidade} unidades')
    else:
        if number[1] == 0:
            if number[2] == 0:
                print(f'{centena} Centenas')
            elif number[2] == 1:
                print(f'{centena} Centenas e {unidade} unidade')
            else:
                print(f'{centena} Centenas e {unidade} unidades')
        elif number[1] == 1:
            if number[2] == 0:
                print(f'{centena} Centenas e {dezena} dezena')
            elif number[2] == 1:
                print(f'{centena} Centenas e {dezena} dezena e {unidade} unidade')
            else:
                print(f'{centena} Centenas e {dezena} dezena e {unidade} unidades')
        else:
            if number[2] == 0:
                print(f'{centena} Centenas e {dezena} dezenas')
            elif number[2] == 1:
                print(f'{centena} Centenas e {dezena} dezenas e {unidade} unidade')
            else:
                print(f'{centena} Centenas e {dezena} dezenas e {unidade} unidades') 

elif qtNumero == 2:
    dezena = number[0]
    unidade = number[1]
    if dezena[0] == 0:
        print('Impossivel calcular dezena de valor zero')
    elif dezena[0] == 1:
        if number[0] == 0:
            print(f'{dezena} Dezena')
        elif number[1] == 1:
            print(f'{dezena} Dezena e {unidade} unidade')
        else:
            print(f'{dezena} Dezena e {unidade} unidades')
    else:
        if number[0] == 0:
            print(f'{dezena} Dezenas')
        elif number[1] == 1:
            print(f'{dezena} Dezenas e {unidade} unidade')
        else:
            print(f'{dezena} Dezenas e {unidade} unidades')

elif qtNumero == 1:
    unidade = number[0]
    if number[0] == 0:
        print('Impossivel calcular unidade de valor zero')
    elif number[0] == 1:
        print(f'{unidade} Unidade')
    else:
        print(f'{unidade} Unidades')

else:
    print('Erro: Um numero fora dos parametros requeridos foi inserido!')


### DICIONARIO DE VARIAVEIS
# number = numero inserido pelo usuario
# qtNumero = quantidade de caracteres da variavel number
# centena = representa o valor das centenas inserida pelo usuario em number
# dezena = representa o valor das dezenas inserida pelo usuario em number
# unidade = representa o valor das unidades inserida pelo usuario em number