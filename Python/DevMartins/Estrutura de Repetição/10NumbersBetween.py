x = True

# Estrutura de repetição
while x == True:

    # Entrada de dados pelo usuario
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    
    # Estrutura condicional com estrutura de repetição dentro de si
    if n1 < n2:
        i = n1
        while i < n2:
            i = i + 1
            print(i)
        x = False
    elif n2 < n1:
        i = n2
        while i < n1:
            i = i + 1
            print(i)
        x = False
    elif n1 == n2:
        print('Não ha intervalos entre numeros iguais')
        x = False
    else:
        print('Insira um valor valido!')

    
### DICIONARIO DE VARIAVEIS
# x = valor booleano para estrutura de repetição
# n1 = numero
# n2 = numero
# i = Valor inteiro para exibiçã de resultados e estrutura de repetição