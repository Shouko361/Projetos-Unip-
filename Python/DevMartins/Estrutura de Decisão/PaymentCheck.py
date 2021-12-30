# Entrada de dados pelo usuario
mfh = float(input('Insira aqui o valor pago por hora do funcionario: '))
mfm = float(input('Insira aqui as horas trabalhadas por mes do funcionario: '))

# Calculo de acordo com os dados das variaveis
salb = mfh*mfm
inss = salb*(10/100)
fgts = salb*(11/100)

if salb <= 900:
    pir = 0
elif salb <= 1500:
    pir = 5
elif salb <= 2500:
    pir = 10
elif salb > 2500:
    pir = 20

ir = salb*(pir/100)
td = inss+ir

sall = salb-td

# Exibição dos resultados
print(f'Salário Bruto: ({mfh}*{mfm})   :R${salb}')
print(f'(-) IR ({pir}%)                  :R${ir}')
print(f'(-) INSS (10%)               :R${inss}')
print(f'FGTS (11%)                   :R${fgts}')
print(f'Total de descontos           :R${td}')
print(f'Salário Liquido              :R${sall}')




### DICIONARIO DE VARIAVEIS
# mfh = Valor pago por hora do funcionario
# mfm = Horas trabalhadas por mes do funcionario
# salb = Salario Bruto
# inss = INSS
# fgts = FGTS
# pir = Porcentagem do Imposto de Renda
# ir = Imposto de Renda
# td = Total de descontos
#sall = Salario Liquido