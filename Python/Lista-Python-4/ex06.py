linhas = 5
colunas = 20
borda = 'M'
preenchimento = '-'

for i in range (linhas):
    for j in range(colunas):
        if 0 < i < linhas - 1 and 0 < j < colunas - 1:
            print (preenchimento, end='')

        else:
            print(borda, end='')

    print()