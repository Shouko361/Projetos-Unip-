# Entrada de dados pelo usuario
n1 = float(input('Insira o primeiro numero aqui: '))
n2 = float(input('Insira o segundo numero aqui: '))

# Estrutura Condicional baseada nas variaveis "n1" e "n2"
if n1 > n2:
    print(f'O maior numero é {n1}')
elif n2 > n1:
    print(f'O maior numero é {n2}')
elif n1 == n2:
    print(f'Ambos numeros são iguais')
else:
    print('Erro!')

### DICIONARIO DE VARIAVEIS
# n1 = numero 1
# n2 = numero 2