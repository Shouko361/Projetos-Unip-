# Importação funções matematicas externas para o codigo
import math

# Entrada de dados pelo usuario
print('O programa calcula uma equação de segundo grau, na forma "ax² + bx + c = 0"')
a = float(input('Insira o valor da variavel a: '))
b = float(input('Insira o valor da variavel b: '))
c = float(input('Insira o valor da variavel c: '))

# Calculo matematico de acordo com as variaveis
if a == 0:
    print('De acordo com os dados recebidos, a equação não é de 2º grau')
else:
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('De acordo com os dados recebidos, a equação não possui raizes reais')
    elif delta == 0:
        print('A equação possui apenas uma raiz real')
        x2 = 2*a
        x = -b/x2
        print(f'A raiz final da equação é {x}')
    else:
        print('A equação possui duas raizes reais')
        raizdelta = math.sqrt(delta)
        x2 = 2*a
        xpositive = (-b+raizdelta)/x2
        xnegative = (-b-raizdelta)/x2
        print(f'A raiz com delta positivo final da equação é {xpositive}')
        print(f'A raiz com delta negativo final da equação é {xnegative}')





### DICIONARIO DE VARIAVEIS
# a = variavel 1 (numero)
# b = variavel 2 (numero)
# c = variavel 3 (numero)
# delta = delta da equação
# raizdelta = resultado da raiz quadrada de delta
# x2 = numerador da divisão da formula de bhaskara
# x = formula de bhaskara
# xpositive = formula de bhaskara com calculo de adição presente no denominador
# xnegative = formula de bhaskara com calculo de subtração presente no denominador