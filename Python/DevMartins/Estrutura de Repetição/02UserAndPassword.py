# # Declaração de booleana para repetição
i = True

# Estrutura de repetição para entrada de dados pelo usuario
while i == True:
    user = str(input('Insira um usuario: '))
    password = str(input('Insira uma senha: '))
    if user != password:
        i = False
    else:
        print('O nome de usuario não pode ser igual a senha!')



### DICIONARIO DE VARIAVEIS
# i = valor booleano para estrutura de repetição
# user = entrada de nome de usuario pelo usuario
# password = entrada de senha pelo usuario