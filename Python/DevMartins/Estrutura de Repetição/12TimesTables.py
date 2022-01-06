# Entrada de valores pelo usuario, declaração de variaveis para repetições e exibição de resultados de entrada de dados
x = int(input('Insira o numero do qual voce deseja saber a tabuada: '))
i = 1
print(f'Tabuada de {x}:')

# Calculo matematico com exibição de resultados
for i in range(11):
    print(f'{x} x {i} = {x*i}')

### DICIONARIO DE VARIAVEIS
# x = Numero a ser multiplicado inserido pelo usuario
# i = Contador de 1 a 10 para multiplicação