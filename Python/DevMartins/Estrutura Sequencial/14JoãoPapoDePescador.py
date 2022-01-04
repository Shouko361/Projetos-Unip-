from myLibrary import isnumber

# Declaração de valor para estrutra de repetição While
i = '0'

while i == '0':
    
    # Mudança de valor para quebra da estrutura While ao fim
    i = '1'

    peso = input('Insira o peso da pesca de peixes: ')

    # Verificação de entrada de valores na variavel "peso" (caso de erro, linha 24) e operações matematicas para verificação de possievl multa
    if isnumber(peso) == True:
        pesof = float(peso)
        excesso = pesof-50
        multa = excesso*4

        # Exibição de resultados resultantes das operações anteriores para possivel multa
        if multa > 0:
            print(f'O valor da multa a ser pago é de R${multa}')
        else:
            print('Não houve multa relativa ao peso da pesca!')
    else:
        print('O valor digitado não é um valor valido.')
        i = input('Digite 0 para realizar a operação novamente. Digite qualquer botão para sair: ')



### DICIONARIO DE VARIAVEIS
# i = cadeia de loop condicional caso o usuario cometa um erro
# peso = peso da pesca de peixes em KG
# pesof = conversao da variavel peso de string para float
# excesso = calculo matematico para obter o excesso de peixes pescados
# multa = calculo da multa de acordo com o excesso