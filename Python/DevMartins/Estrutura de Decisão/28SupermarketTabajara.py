# Declaração de variaveis e entrada de dados pelo usuario
card = False
desconto = 0
print('Insira o tipo de carne')
tipodecarne = str(input('FD para File Duplo, A para Alcatra e P para picanha: '))
pesodecarne = float(input('Insira o peso em Kg de carne: '))

# Estrutura condicional para criação de variaveis atraves realização de operação matematica de acordo com variaveis
if tipodecarne == 'FD':
    tipodecarnef = 'File Duplo'
    if pesodecarne <= 5:
        valortotal = pesodecarne*4.9
    else:
        valortotal = pesodecarne*5.8
elif tipodecarne == 'A':
    tipodecarnef = 'Alcatra'
    if pesodecarne <= 5:
        valortotal = pesodecarne*5.9
    else:
        valortotal = pesodecarne*6.8
elif tipodecarne == 'P':
    tipodecarnef = 'Picanha'
    if pesodecarne <= 5:
        valortotal = pesodecarne*6.9
    else:
        valortotal = pesodecarne*7.8

# Entrada de dados e estrutra condicional de acordo com variaveis
print('Insira o tipo de pagamento')
tipodepagamento = str(input('D para Dinheiro e C para cartão: '))
if tipodepagamento == 'C':
    print('A compra foi feita pelo cartão Tabajara?')
    cardconfirmation = str(input('S para Sim e N para Não: '))
    if cardconfirmation == 'S':
        card = True
    else:
        print('Credito ou Debito?')
        DouC = str(input('Insira C para Credito e D para Debito: '))
        if DouC == 'C':
            tipodepagamentof = 'Cartão de Credito'
            valorapagar = valortotal-desconto
        elif DouC == 'D':
            tipodepagamentof = 'Cartão de Debito'
            valorapagar = valortotal-desconto
elif tipodepagamento == 'D':
    tipodepagamentof = 'Dinheiro'
    valorapagar = valortotal-desconto

if card == True:
    desconto = valortotal*(5/100)
    valorapagar = valortotal-desconto
    tipodepagamentof = 'Cartão Tabajara'

# Exibição de resultados de acordo com variaveis
print('CUPOM FISCAL')
print(f'Tipo de carne:       {tipodecarnef}')
print('Quantidade de carne: {:.2f}Kg'.format(pesodecarne))
print('Preço total:         R${:.2f}'.format(valortotal))
print(f'Tipo de pagamento:   {tipodepagamentof}')
print('Valor do desconto:   R${:.2f}'.format(desconto))
print('Valor a pagar:       R${:.2f}'.format(valorapagar))



### DICIONARIO DE VARIAVEIS
# card = variavel booleana para confirmação se o metodo de pagamento sera no cartão ou nao
# desconto = variavel para alocar o valor de desconto calculado
# tipodecarne = tipo de carne selecionada pelo usuario
# pesodecarne = peso de carne selecionado pelo usuario
# tipodecarnef = formatação de string para melhor exibição da variavel tipodecarne
# valortotal = valor bruto da compra
# tipodepagamento = entrada de dado para estrutura de decisão sobre o tipo de pagamento optado pelo cliente
# cardconfirmation = confirmação se (apenas no caso de o tipo de pagamento ser tipo C) o cartão a ser utilizado é o cartão Tabajara (cartão do supermercado)
# DouC = Debito ou Credito, entrada de dado pelo usuario para o programa saber se o cartão a ser utilizado sera de debito ou credito (apenas no caso de card == false)
# tipodepagamentof = formatação de string para melhor exibição da variavel tipodepagamento
# valorapagar = valor final o qual o usuario devera pagar