# Declaração de variaveis booleanas
day = False
month = False
year = False

# Entrada de dados pelo usuario e conversão das variaveis strings para integers
a, b, c = input('Insira uma data no formato DD/MM/AAAA: ').split("/")
aint = int(a)
bint = int(b)
cint = int(c)

# Exibição de resultados de acordo com as variaveis
if aint <= 31 and aint >= 1:
    day = True
    if bint <= 12 and bint >= 1 and day == True:
        month = True
        if cint > 0 and day == True and month == True:
            year = True
            print('Data valida')
        else:
            print('Data invalida')
    else:
        print('Data invalida')
else:
    print('Data invalida')




# DICIONARIO DE VARIAVEIS
# day = dia
# month = mes
# year = ano
# a = entrada do dia pelo usuario em formato de string
# b = entrada do mes pelo usuario em formato de string
# c = entrada do ano pelo usuario em formato de string
# aint = conversão da variavel "a" de string para integer
# bint = conversão da variavel "b" de string para integer
# cint = conversão da variavel "c" de string para integer