n = int(input('Insira um valor para ser calculado o fatorial: '))
result = 0
count = n

while count == 0:
    x = n
    result = result + (n*x)
    x -= 1

print(result)