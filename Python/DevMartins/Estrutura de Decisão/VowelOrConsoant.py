# Entrada de dados pelo usuario
letra = input('Digite uma letra: ')

# Verificação se variavel "letra" possui apenas letras (caso não, linha 12)
if letra.isalpha():
    
    # Estrutra condicional de acordo com dados da variavel "letra"
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('É uma vogal')
    else:
        print('É uma consoante')
else:
    print('Isto não é uma letra')

### DICIONARIO DE VARIAVEIS
# letra = letra