from math import factorial

fatorial = int(input('Qual fatorial deseja?'))
N = fatorial
F = 1

while N > 0:
    print(' {} '.format(N), end='')
    print(' x ' if N > 1 else ' = ', end='')
    F *= N
    N -= 1

print(F)