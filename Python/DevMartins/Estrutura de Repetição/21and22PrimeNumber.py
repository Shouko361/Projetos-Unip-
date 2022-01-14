# Entrada de dados pelo usuario, declaração de variaveis de listas e integers
n1 = int(input('Digite um numero inteiro para saber se é primo: '))
cont = 0
div = []

# Estrutura de repetição finita
for i in range(n1):
    # Condicional se o numero na contagem houver final 0 na divisão é adicionado na lista div
    if n1%(i+1) == 0:
        cont += 1
        div.append(i+1)
    else:
        cont

# Exibição de dados a partir de estrutura condicional dependente de resultados de variaveis
if cont == 2:
    print (f"O numero {n1} é primo e é divisivel por {div}")
else:
    print (f"O numero {n1} não é primo pois é divisivel por {div}")





### DICIONARIO DE VARIAVEIS
# n1 = Entrada de dado pelo usuario
# cont = contagem para estrutra condicional para exibição de resultados
# div = lista onde é armazenado os numeros divisiveis pelo n1 (entrada pelo usuario)