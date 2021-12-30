# Entrada de dados pelo usuario
l1 = float(input('Insira o primeiro lado do triângulo: '))
l2 = float(input('Insira o segundo lado do triângulo: '))
l3 = float(input('Insira o terceiro lado do triângulo: '))

# Confirmação se os valores batem com o proposito do codigo
if l1+l2 > l3:
    triangle = True
else:
    triangle = False

# Exibição de resultados baseados nas variaveis
if triangle ==  True:
    if l1 == l2 and l1 == l3:
        print('Você possui um Triângulo Equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Você possui um Triângulo Isóceles')
    else:
        print('Você possui um Triângulo Escaleno')
else:
    print('Você não possui um Triângulo')



### DICIONARIO DE VARIAVEIS
# l1 = lado 1
# l2 = lado 2
# l3 = lado 3
# triangle = booleano que confirma se o triangulo é realmente um triangulo