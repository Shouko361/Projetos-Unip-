# Declaração de variaveis e entrada de dados pelo usuario
morango = float(input('Insira a quantidade em Kg de morangos: '))
maca = float(input('Insira a quantidade em Kg de maçãs: '))
totalkg = morango + maca
totalmaca = 0
totalmorango = 0
mora5kg = 2.5
maca5kg = 1.8
morad5kg = 2.2
macad5kg = 1.5

# Estrutura condicional de calculos baseados nas variaveis
if morango <= 5:
    totalmorango = morango*mora5kg
else:
    totalmorango = morango*morad5kg
if maca <= 5:
    totalmaca = maca*maca5kg
else:
    totalmaca = maca*macad5kg

# Calculo de valor final
totalvalor = totalmaca+totalmorango

# Estrutura condicional para exibição de dados e calculos de acordo com as variaveis
if totalkg > 8 or totalvalor > 25:
    desconto = totalvalor*(10/100)
    valorfinal = totalvalor - desconto
    round(valorfinal, 2)
    print('Com esta compra você ganhou o desconto de 10%! O valor final é de {:.2f}'.format(valorfinal))
else:
    round(totalvalor, 2)
    print('O valor final é de {:.2f}'.format(totalvalor))

### DICIONARIO DE VARIAVEIS
# morango = Entrada do numero de Kg de morango comprado
# maca = Entrada do numero de Kg de maçã comprada
# totalkg = calculo do peso total (morango + maça)
# totalmaca (primeira aparição) = declaração de variavel para o caso de o valor inserido ser zero
# totalmaca (segunda aparição) = operação matematica para calcular o valor final a ser pago apenas pelas maçãs
# totalmorango (primeira aparição) = declaração de variavel para o caso de o valor inserido ser zero
# totalmorango (segunda aparição) = operação matematica para calcular o valor final a ser pago apenas pelas morangos
# mora5kg = valor do kg do morango para pesos menores que 5kg
# maca5kg = valor do kg da maça para pesos menores que 5kg
# morad5kg = valor do kg do morango para pesos maiores que 5kg
# macad5kg = valor do kg da maça para pesos maiores que 5kg
# totalvalor = total do valor a ser pago (caso não haja desconto, conta-se como valor final)
# desconto = calculo do desconto para o usuario caso haja desconto
# valorfinal = valor final a ser pago com desconto aplicado