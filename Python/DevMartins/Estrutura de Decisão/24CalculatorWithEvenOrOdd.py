# Entrada de dados pelo usuario e seleção de operação matematica
n1 = float(input('Insira o primeiro numero aqui: '))
n2 = float(input('Insira o segundo numero aqui: '))
print('Selecione a operação desejada')
print('x para multiplicação')
print('/ para divisão')
print('+ para adição')
print('- para subtração')
op = str(input(''))

# Calculo matematico de acordo com as variaveis e exibição dos resultados
# Estrutura condicional
if op == 'x':
    result = n1*n2
    eoo = result%2
    if eoo == 0:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e par!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e par')
    else:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e impar!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e impar')
if op == '/':
    result = n1/n2
    eoo = result%2
    if eoo == 0:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e par!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e par')
    else:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e impar!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e impar')
if op == '+':
    result = n1+n2
    eoo = result%2
    if eoo == 0:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e par!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e par')
    else:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e impar!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e impar')
if op == '-':
    result = n1-n2
    eoo = result%2
    if eoo == 0:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e par!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e par')
    else:
        if result.is_integer():
            print(f'O resultado foi de {result} que é um numero inteiro e impar!')
        else:
            print(f'O resultado foi de {result} que é um numero decimal e impar')





### DICIONARIO DE VARIAVEIS
# n1 = numero
# n2 = numero
# op = Operador da conta matematica
# result = resultado da operação matematica
# eoo = operação matematica para chegar se result é par ou impar