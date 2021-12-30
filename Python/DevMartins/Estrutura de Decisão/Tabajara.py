# Sistema de loop infinito
while True:

    # Entrada de dados pelo usuario
    sal = float(input('Insira aqui o atual salario do colaborador: '))
   
   # Calculo dependendo do valor de variavel sal
    if sal <= 280:
        aumentopc = 20
        aumento = sal*(aumentopc/100)
        salplus = sal + aumento

    elif sal > 280 and sal <= 700:
        aumentopc = 15
        aumento = sal*(aumentopc/100)
        salplus = sal + aumento
    elif sal > 700 and sal <= 1500:
        aumentopc = 10
        aumento = sal*(aumentopc/100)
        salplus = sal + aumento
    elif sal > 1500:
        aumentopc = 5
        aumento = sal*(aumentopc/100)
        salplus = sal + aumento
    else:
        print('Insira um valor real')

    # Exibição dos resultados
    print(f'O salario antes do reajuste era de R${sal}')
    print(f'O percentual aplicado para este colaborador foi de {aumento}%')
    print(f'O valor de aumento foi de R${aumento}')
    print(f'O salario atual com o aumento é de R${salplus}')
    print('')

### DICIONARIO DE VARIAVEIS
# sal = Salario
# aumentopc = porcentagem do aumento
# aumento = aumento do salario
# salplus = salario com aumento