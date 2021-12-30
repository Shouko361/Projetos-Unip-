# Entrada de dados pelo usuario
year = int(input('Insira um ano do mundo em que vivemos: '))

# Calculo feito dependendo das variaveis
if year % 4 == 0 and year % 100 != 0:
    print('Você inseriu um ano bissexto!')
else:
    print('Você inseriu um ano comum')

### DICIONARIO DE VARIAVEIS
# year = ano