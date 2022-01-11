# Definição de valores de variaveis para estrutura de repetição e contagem
i = 1
e = 0
o = 0

# Estrutura de repetição
# Enquanto i for menor que 10, numbers ira ficar pedindo numeros ao usuario, i recebera +1 e numbers sera calculado para checagem
# se é par ou impar, caso seja par, e (even) recebera +1, caso seja par, o (odd) recebera +1, e então a estrutura se repete
while i <= 10:
    numbers = float(input('Insira um numero: '))
    i += 1
    if numbers % 2 == 0:
        numbers = e
        e += 1
    else:
        numbers = o
        o += 1

# Exibição de resultados
print(f"A quantidade de números pares é {e}")
print(f"A qtd de números ímpares é {o}")



### DICIONARIO DE VARIAVEIS
# i = variavel int para estrutura de repetição
# e = even, par, contagem de valores pares
# o = odd, impar, contagem de valores impares
# numbers = numeros inseridos pelo usuario para calculo de par ou impar