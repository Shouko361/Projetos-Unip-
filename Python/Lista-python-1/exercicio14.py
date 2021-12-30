dias = int(input("Dias:"))
horas = int(input("Horas:"))
minutos = int(input("Minutos:"))
segundos = int(input("Segundos:"))
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print("Convertido em segundos é igual a %10d segundos." % total_em_segundos)