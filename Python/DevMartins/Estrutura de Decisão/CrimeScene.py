# Declaração de variaveis e instruções para o usuario
i = 0
sim = 0
print('Responda as perguntas com S para SIM e N para NÃO')

# Estrutura de repetições e decisões misturadas com entrada de dados pelo usuario
while i == 0:
    i = 1
    print('Você telefonou para a vitima?')
    p1 = input('')
    if p1 == 'S':
        sim += 1
    elif p1 != 'N':
        print('Resposta incorreta!')
        i = 0

i = 0

while i == 0:
    i = 1
    print('Você esteve no local do crime?')
    p1 = input('')
    if p1 == 'S':
        sim += 1
    elif p1 != 'N':
        print('Resposta incorreta!')
        i = 0

i = 0

while i == 0:
    i = 1
    print('Você mora perto da vítima?')
    p1 = input('')
    if p1 == 'S':
        sim += 1
    elif p1 != 'N':
        print('Resposta incorreta!')
        i = 0

i = 0

while i == 0:
    i = 1
    print('Você devia para a vítima?')
    p1 = input('')
    if p1 == 'S':
        sim += 1
    elif p1 != 'N':
        print('Resposta incorreta!')
        i = 0

i = 0

while i == 0:
    i = 1
    print('Você já trabalhou com a vítima?')
    p1 = input('')
    if p1 == 'S':
        sim += 1
    elif p1 != 'N':
        print('Resposta incorreta!')
        i = 0

# Exibição de resultados de acordo com as variaveis
if sim == 0 or sim == 1:
    print('Inocente!')
elif sim == 2:
    print('Suspeito!')
elif sim == 3 or sim == 4:
    print('Cumplice!')
elif sim == 5:
    print('Assassino!')

### DICIONARIO DE VARIAVEIS
# i = variavel para estrutura de repetição
# sim = variavel para contagem de respostas "sim"
# p1 = pergunta 1
# p2 = pergunta 2
# p3 = pergunta 3
# p4 = pergunta 4
# p5 = pergunta 5