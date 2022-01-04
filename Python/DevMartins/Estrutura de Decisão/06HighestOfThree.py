# Entrada de dados do tipo float pelo usuario
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
n3 = float(input('Insira o terceiro numero: '))

# Estrutura condicional baseada nas variaveis "n1", "n2" e "n3"
# (Verificação de qual numero é o maior (Caso não seja numero, linha 16))
if n1 > n2 and n1 > n3:
    print(f'{n1} é o maior numero')
elif n2 > n1 and n2 > n3:
    print(f'{n2} é o maior numero')
elif n3 > n1 and n3 > n2:
    print(f'{n3} é o maior numero')
elif n1 == n2 and n2 == n3:
    print('Todos os numeros são iguais')
else:
    print('Tem certeza que voce colocou numeros ai?')


### DICIONARIO DE VARIAVEIS
# n1 = numero 1
# n2 = numero 2
# n3 = numero 3