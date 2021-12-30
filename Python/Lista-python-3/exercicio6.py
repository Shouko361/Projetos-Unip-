minimo = int(input("Mínimo: "))
maximo = int(input("Máximo: "))

for num in range(minimo, maximo + 1):

    sum = 0

    n = len(str(num))

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)