# Entrada de dados pelo usuario e calculo baseado nos dados de entrada
tamanho = float(input('Insira o tamanho em MB do arquivo a ser baixado: '))
speed = float(input('Insira a velocidade da internet em Mbps: '))
segundos = tamanho/speed
minutos = (segundos/60)
segundos = int(segundos%60)

# Estrutura de decisão baseada nos dados e calculos da variavel "minutos"
if minutos >= 1:
    print(f'O seu download ira demorar aproximadamente {minutos} minuto(s) e {segundos} segundo(s)')
else:
    print(f'O seu download ira demorar aproximadamente {segundos} segundo(s)')


### DICIONARIO DE VARIAVEIS
# tamanho = tamanho do download em MB
# speed = velocidade da internet em Mbps
# segundos = calculo de tamanho dividido por speed
# minutos = calculo de conversao de tempo da variavel segundos de segundos para minutos