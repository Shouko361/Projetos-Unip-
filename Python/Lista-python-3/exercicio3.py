primeirp = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeirp + (10 - 1) * razao

for c in range(primeirp, decimo + razao, razao):
    print(c, end=' -> ')
    
print('Fim')