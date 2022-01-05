# Declaração de valores
countryA = float(input('Informe a população inicial do Pais A: '))
countryB = float(input('Informe a população inicial do Pais B: '))
percentageA = float(input('Informe a porcentagem inicial de crescimento do Pais A: '))
percentageB = float(input('Informe a porcentagem inicial de crescimento do Pais B: '))
years = 0

# Estrutura de repetição para calculo matematico
while countryA < countryB:
    aumentoA = countryA*(percentageA/100)
    aumentoA = round(aumentoA)
    print(f'O aumento do Pais A no ano {years} sera de {aumentoA} pessoas')
    countryA = countryA + aumentoA
    aumentoB = countryB*(percentageB/100)
    aumentoB = round(aumentoB)
    print(f'O aumento do Pais B no ano {years} sera de {aumentoB} pessoas')
    countryB = countryB + aumentoB
    years = years + 1

# Exibição de resultados
print(f'Sera necessario {years} anos para que o Pais A ultrapasse a população do Pais B')

### DICIONARIO DE VARIAVEIS
# countryA = População do Pais A
# countryB = População do Pais B
# percentageA = Porcentagem de crescimento da população do Pais A
# percentageB = Porcentagem de crescimento da população do Pais B
# aumentoA = Numero do aumento da população do Pais A no ano atual em que a repetição estiver rodando
# aumentoB = Numero do aumento da população do Pais B no ano atual em que a repetição estiver rodando
# years = anos contados