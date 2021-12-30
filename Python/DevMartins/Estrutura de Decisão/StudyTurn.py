#Estrutura de repetição controlada pelo usuaro
i = 0
while i == 0:
    i = 1 

    # Entrada de dados pelo usuario e manipulação dos dados
    print('Insira aqui o seu periodo de estudo')
    print('M para Matutino, V para Vespertino e N para Noturno')
    turn = input('')
    turn = turn.upper()
    name = input('Insira aqui como gostaria de ser chamado: ')

    # Exibição de resultados dependendo dos dados das variaveis
    if turn == 'M':
        print(f'Bom dia {name}!')
    elif turn == 'V':
        print(f'Boa tarde {name}!')
    elif turn == 'N':
        print(f'Boa noite {name}!')
    else:
        print('Valor invalido')
        i = int(input('Para tentar novamente pressione 0 e confirme, para sair pressione outro botão e confirme: '))


### DICIONARIO DE VARIAVEIS
# i = contador para o loop
# turn = turno do usuario
# name = nome do usuario