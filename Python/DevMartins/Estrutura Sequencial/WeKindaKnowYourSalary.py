# Entrada de dados pelo usuario e conversão de dados de string para float
monthhours = input('Quantas horas voce trabalha por mês? ')
moneyforhour = input('Quantos você ganha por hora trabalhada? ')
monthhoursf = float(monthhours)
moneyforhourf = float(moneyforhour)

# Operação para saber o salario referido ao mes de acordo com dados inseridos nas variaveis "monthhours" e "moneyforhour"
salary = moneyforhourf*monthhoursf

# Exibição do resultado resultante da operação presente na variavel "salary"
print(f'O seu salario referido ao mês é de {salary}')



### DICIONARIO DE VARIAVEIS
# monthhours = horas trabalhadas por mes
# moneyforhour = dinheiro recebdio por hora
# monthhourf = conversao da variavel monthhours de string para float
# moneyforhourf = conversao da variavel moneyforhour de string para float
# salary = calculo matematico para saber o salario final