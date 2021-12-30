# Entrada de dados pelo usuario e calculo da media de "n1" e "n2" na variavel "media"
n1 = int(input('Insira a primeira nota do aluno: '))
n2 = int(input('Insira a segunda nota do aluno: '))
media = (n1+n2)/2

# Estrutura condicional baseada na variavel "media"
if media == 10:
    print('Aluno Aprovado com Distinção')
elif media >= 7:
    print('Aluno Aprovado')
elif media < 7:
    print('Aluno Reprovado')


### DICIONARIO DE VARIAVEIS
# n1 = numero 1
# n2 = numero 2
# medai = media do aluno