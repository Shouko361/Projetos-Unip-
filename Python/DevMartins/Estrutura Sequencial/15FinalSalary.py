# Entrada de dados pelo usuario e conversão de valores de string para float
SalPerHour = input('Insira o valor recebido por hora trabalhada: ')
HourOnMonth = input('Insira quantas horas são trabalhadas por mes: ')
SalPerHourf = float(SalPerHour)
HourOnMonthf = float(HourOnMonth)

# Operações de descontos em porcentagem
salLiquido = SalPerHourf*HourOnMonthf
inss = (salLiquido*8)/100
sindicato = (salLiquido*5)/100
ir = (salLiquido*11)/100

# Exibição dos valores descontados
print(f'+ Salario Bruto: R${salLiquido}')
print(f'- IR (11%): R${ir}')
print(f'- INSS (8%): R${inss}')
print(f'- Sindicato (5%): R${sindicato}')

# Operação e Exibição de valor final com descontos
salLiquido = salLiquido-(inss+sindicato+ir)
print(f'+ Salario Liquido: R${salLiquido}')



### DICIONARIO DE VARIAVEIS
# SalPerHour = Valor recebido por hora trabalhadas
# HourOnMonth = Horas trabalhadas por mes
# SalPerHourf = varivavel SalPerHour de string para float
# HourOnMonthf = varivavel HourOnMonth de string para float
# salLiquido = Calculo do salario bruto
# inss = calclo do inss
# sindicato = calculo do sindicato
# ir = calculo do imposto de renda