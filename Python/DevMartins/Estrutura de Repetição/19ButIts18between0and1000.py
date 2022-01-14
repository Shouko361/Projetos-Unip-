# Declaração de valores de variaveis
i = True
num = []

# Aviso para o usuario
print('Digite 0 para sair')

# Estrutura de repetição
while i == True:
    # Entrada de dados pelo usuario
    n1 = int(input("Insira um numero: "))
    
    # Estrutura condicional para aceitar apenas valores entre 0 e 1000
    if n1 >= 0 and n1 <= 1000:

        # Atribuição de valores a lista num (Append = Acrescentar)
        if n1 != 0:
            num.append(n1)
        # Caso condição não coincida, pare (break = parar)
        else:
            break
    
    # Caso condição não coincida exibe aviso para usuario
    else:
        print("Só serão aceitos valores entre 0 e 1000")

# Exibição de resultados
print(f"Menor numero: {min(num)}")
print(f"Maior numero: {max(num)}")


### DICIONARIO DE VARIAVEIS
# i = variavel booleana para estrutura de repetição
# num = lista de valores adicionados pelo usuario a partir da variavel n1
# n1 = entrada de dados pelo usuario que serão adicionados a lista num