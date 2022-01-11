# Declaração de variaveis para contagem do calculo
anterior = 0
proximo = 0

# Estrutura de repetição
while proximo < 500:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo = proximo + 1



### DICIONARIO DE VARIAVEIS
# anterior = numero anterior recebido na variavel proximo
# proximo = numero proximo a ser exibido 