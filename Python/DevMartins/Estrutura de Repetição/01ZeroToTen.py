# Declaração de booleana para repetição
i = True

# Estrutura de repetição para entrada de dados pelo usuario
while i == True:
    x = int(input('Insira um valor de 0 a 10: '))
    if x >= 0 and x <= 10:
        i = False
    else:
        print('Digite um valor valido!')
        i = True

### DICIONARIO DE VARIAVEIS
# i = valor booleano para estrutura de repetição
# x = numero de entrada pelo usuario