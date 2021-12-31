# Definição de variavel booleana para estrutura de repetição
i = True

# Entrada de dados dentro de estrutura de repetição
while i == True:
    value = int(input('Digite o valor para saque: '))
    if value < 10 or value > 600:
        print('Valor inválido! Saque disponivel para valores apenas abaixo de R$600 e acima de R$10')
    else:
        i = False

# Calculo matematico
cem = int((value - (value%100))/100)
cinquenta = int((value%100)/50)
dez = int(((value%50)/10))
um = value%10

# Exibição de resultados
if(cem == 1):
    print(f'{cem} nota de R$100')
elif(cem > 1):
    print(f'{cem} notas de R$100')
if(cinquenta == 1):
    print(f'{cinquenta} nota de R$50')
elif(cinquenta > 1):
    print(f'{cinquenta} notas de R$50')
if(dez == 1):
    print(f'{dez} nota de R$10')
elif(dez > 1):
    print(f'{dez} notas de R$10')
if (um == 1):
    print(f'{um} nota de R$1')
elif (um > 1):
    print(f'{um} notas de R$1')





### DICIONARIO DE VARIAVEIS
# i = variavel booleana para estrutura de repetição
# value = valor de saque inserido pelo usuario
# cem = contagem de notas de 100
# cinquenta = contagem de notas de 50
# dez = contagem de notas de 10
# um = contagem de notas de 1