def volume(r):
    v = 4/3 * 3.14 * r**3
    print('O volume da esfera é {:.2f}'.format(v))

r = float(input('Digite o valor do raio da esfera: '))
volume(r)
