# Entrada de dados pelo usuario no formato de integer e float
firstInteger = int(input('Adicione um numero inteiro: '))
secondInteger = int(input('Adicione outro numero inteiro: '))
firstReal = float(input('Adicione um numero real: '))

# Opreação matematica (dado da variavel "firstInteger" vezes 2 vezes dado da variavel "secondInteger" dividido por 2)
opA = (firstInteger*2)*(secondInteger/2)

# Operação matematica (dado da variavel "firstInteger" vezes 3 mais dado da variavel "firstReal" )
opB = (firstInteger*3)+firstReal

# Operação matematica (dado da variavel "firstReal" ao cubo)
opC = firstReal**3

# Exibição de resultados das operações matematicas das variaveis "opA", "opB" e "opC"
print(f'O produto do dobro do primeiro numero com metade do segundo numero inserido é {opA}')
print(f'A soma do triplo do primeiro numero com o terceiro numero inserido é {opB}')
print(f'O terceiro numero inserido elevado ao cubo é {opC}')

### DICIONARIO DE VARIAVEIS
# firstInteger = numero inteiro
# secondInteger = numero inteiro
# firstReal = numero real
# opA = operação matematica
# opB = operação matematica
# opC = operação matematica