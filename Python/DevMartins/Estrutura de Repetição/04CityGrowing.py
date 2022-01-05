# Declaração de valores
countryA = 80000
countryB = 200000
years = 0

# Estrutura de repetição para calculo matematico
while countryA < countryB:
    aumentoA = countryA*(3/100)
    countryA = countryA + aumentoA
    aumentoB = countryB*(1.5/100)
    countryB = countryB + aumentoB
    years = years + 1

# Exibição de resultados
print(f'Sera necessario {years} anos para que o Pais A ultrapasse a população do Pais B')

### DICIONARIO DE VARIAVEIS
# countryA = População do Pais A
# countryB = População do Pais B
# aumentoA = Numero do aumento da população do Pais A no ano atual em que a repetição estiver rodando
# aumentoB = Numero do aumento da população do Pais B no ano atual em que a repetição estiver rodando
# years = anos contados