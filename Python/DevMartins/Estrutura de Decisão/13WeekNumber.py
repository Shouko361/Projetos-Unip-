# Estrutura de repetição para erros controlada pelo usuario
i = 0
while i == 0:
    i = 1

    # Entrada de dados pelo usuario
    wn = int(input('Insira um numero de 1 a 7 para ver um dia da semana: '))

    # Exibição de dados de acordo com as variaveis
    if wn == 1:
        print('Domingo é o 1º dia da semana')
    elif wn == 2:
        print('Segunda-feira é o 2º dia da semana')
    elif wn == 3:
        print('Terça-feira é o 3º dia da semana')
    elif wn == 4:
        print('Quarta-feira é o 4º dia da semana')
    elif wn == 5:
        print('Quinta-feira é o 5º dia da semana')
    elif wn == 6:
        print('Sexta-feira é o 6º dia da semana')
    elif wn == 7:
        print('Sabado é o 7º dia da semana')
    else:
        i = int(input('Numero invalido, para tentar novamente aperte 0 e confirme, para sair aperte qualquer tecla e confirme: '))




### DICIONARIO DE VARIAVEIS
# i = Contador para estrutura de repetição para erros controlada pelo usuario para
# wn = Dia da semana