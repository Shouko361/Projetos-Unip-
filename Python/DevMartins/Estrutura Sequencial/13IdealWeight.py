from myLibrary import isnumber

# Declaração de variaveis para definição de valores booleanos do While
erroaltura = '0'
errosexo = '0'

# Inicio da estrutura while para variavel "altura"
while erroaltura == '0':

    # Mudança de valor da variavel "erroaltura" para quebra de estrutura de repetição
    erroaltura = '1'

    altura = input('Insira sua altura: ')

    # Verificação de dados inseridos pelo usuario na variavel "altura" (se obtiver erro, linha 35)
    if isnumber(altura) == True:
    
        # Inicio da estrutra While para entrada da variavel "sexo"
        while errosexo == '0':
            errosexo = '1'
            alturaf = float(altura)
            sexo = input('Insira o seu sexo (H para homem e M para mulher): ')

            # Verificação e exibição de resultados de acordo com os dados da variavel "sexo" (se obtiver erro, linha 32)
            if sexo == 'H':
                idealWeight = (72.7*alturaf)-58
                print(f'Seu peso ideal é de {idealWeight} Kg')
            elif sexo == 'M':
                idealWeight = (62.1*alturaf)-44.7
                print(f'Seu peso ideal é de {idealWeight} Kg')
            else:
                print('Entrada de sexo invalida')
                errosexo = input('Para tentar novamente pressione 0. Para sair pressione qualquer botão: ')
    else:
        print('Entrada de altura invalida')
        erroaltura = input('Para tentar novamente pressione 0. Para sair pressione qualquer botão: ')



### DICIONARIO DE VARIAVEIS
# erroaltura = cadeia de loop para caso haja erro pelo usuario
# errosexo = cadeia de loop para caso haja erro pelo usuario
# altura = entrada de dado da altura do usuario
# sexo = entrada de dado do sexo do usuario
# idealWeight = calculo de peso ideal para o usuario