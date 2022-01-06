# Entrada de dados pelo usuario e declaração de variaveis
base = int(input("Insira a base: "))
exp = int(input("Insira o expoente: "))
potencia = 1
i = 1

# Estrutura de repetição com calculo matematico
while i <= exp:
    potencia = potencia*base
    i = i + 1

# Exibição de resultados
print(base,"^",exp,"=",potencia)

### DICIONARIO DE VARIAVEIS
# base = numero base do calculo de potencia
# exp = numero expoente do calculo de potencia
# potencia = variavel para repetir calculo de numero base (ex: 1ª vez(potencia = potencia * base) 2ª vez(potencia = potencia * base) 3ª vez(potencia = potencia * base))
#                                                         (ex: 1ª vez(    1    =     1    *   5 ) 2ª vez(    5    =     5    *   5 ) 3ª vez(   25    =    25    *   5 ))
# i = contador para estrutura de repetição