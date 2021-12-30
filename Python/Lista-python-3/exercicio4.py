n = int(input("Quantos números: "))
i = 0
a = 0
b = 0
c = 0
d = 0

while i < n:
    numero = int(input("Insira número:"))
    i = i + 1
    print(i)
    if numero < 0:
        break
    if numero >= 0 and numero <= 25:
        a = a + 1
    if numero >= 26 and numero <= 50:
        b = b + 1
    if numero >= 51 and numero <= 75:
        c = c + 1
    if numero >= 76 and numero <= 100:
        d = d + 1

print("Intervalo1: ",a)
print("Intervalo2: ",b)
print("Intervalo3: ",c)
print("Intervalo4: ",d)