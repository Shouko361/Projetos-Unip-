# Entrada de dados de nome do aluno e notas bimestrais
name = input('Nome do aluno: ')
b1 = input('Nota do primeiro bimestre: ')
b2 = input('Nota do segundo bimestre: ')
b3 = input('Nota do terceiro bimestre: ')
b4 = input('Nota do quarto bimestre: ')

# Conversão da entrada de valores (notas bimestrais) de string para float
b1f = float(b1)
b2f = float(b2)
b3f = float(b3)
b4f = float(b4)

# Operação para chegar a media final do aluno
mf = (b1f + b2f + b3f + b4f) / 4

# Exibição de resultados (media final)
print(f'A media final do aluno {name} é: {mf}')

### DICIONARIO DE VARIAVEIS
# name = nome do aluno
# b1 = nota do primeiro bimestre
# b2 = nota do segundo bimestre
# b3 = nota do terceiro bimestre
# b4 = nota do quarto bimestre
# b1f = conversao da variavel b1 de string para float
# b2f = conversao da variavel b2 de string para float
# b3f = conversao da variavel b3 de string para float
# b4f = conversao da variavel b4 de string para float
# mf = calculo para obter a media final do aluno