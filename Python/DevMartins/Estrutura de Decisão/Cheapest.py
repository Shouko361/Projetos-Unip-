# Entrada de dados de tipo float pelo usuario
print('Não se esqueça de separar os centavos com um ponto (.)')
n1 = float(input('Insira o valor do primeiro produto: '))
n2 = float(input('Insira o valor do segundo produto: '))
n3 = float(input('Insira o valor do terceiro produto: '))

# Estrutura condicional para verificação de produto mais barato baseado nos dados das variasveis "n1", "n2" e "n3"
if n1 < n2 and n1 < n3:
    print(f'O primeiro produto, com o valor de {n1}, é o produto mais barato')
elif n2 < n1 and n2 < n3:
    print(f'O segundo produto, com o valor de {n2}, é o produto mais barato')
elif n3 < n1 and n3 < n2:
    print(f'O terceiro produto, com o valor de {n3}, é o produto mais barato')
elif n1 == n2 and n2 == n3:
    print('O valor de todos os produtos são iguais')
else:
    print('Tem certeza que voce colocou valor de produtos ai?')


### DICIONARIO DE VARIAVEIS
# n1 = numero 1
# n2 = numero 2
# n3 = numero 3