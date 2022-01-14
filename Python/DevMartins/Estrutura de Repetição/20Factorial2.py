# Entrada de dados pelo usuario e declaração de variaveis
while True:

    n = int(input("Fatorial de: "))
    if n <= 16:
        result = 1
        x = 1

        # Estrutura de repetição para calculo de valor fatoria desejado pelo usuario
        while x <= n:
            result = result * x
            x += 1

        # Eibição de resultados
        print(f"O fatorial de {n} é {result}")
    else:
        print("Só são validas entradas de fatorial inteiras e menores que 16")


### DICIONARIO DE VARIAVEIS
# n = numero de entrada pelo usuario para o calculo do valor fatorial
# result = resultado final do valor fatorial de acordo com a variavel n inserida pelo usuario
# x = contador para repetição e calculo de fatorial