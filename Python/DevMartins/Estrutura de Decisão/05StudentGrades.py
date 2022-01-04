# Entrada de dados pelo usuario, calculo de media e formatação de float
n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
n3 = float(input('Insira a terceira nota do aluno: '))
media = (n1 + n2 + n3)/3
mediaf = "{:.2f}".format(media)

# Exibição de resultados
if media == 10:
    print(f'Media {mediaf}! Aprovado com distinção')
elif media >= 7:
    print(f'Media {mediaf}! Aprovado')
elif media < 7:
    print(f'Media {mediaf}! Reprovado')





### DICIONARIO DE VARIAVEIS
# n1 = nota 1 do aluno
# n2 = nota 2 do aluno
# n3 = nota 3 do aluno
# media = calculo da media do aluno de acordo com as variaveis
# mediaf = formatação do float "media" para se limitar a apenas duas casas decimais