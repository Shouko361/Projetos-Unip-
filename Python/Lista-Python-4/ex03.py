def função(n1, n2, n3,):
    dias = n1*365 + n2*30 * n3
    print('Você tem {} dias de vida!'.format(dias))

n1 = int(input('Qual sua idade? '))
n2 = int(input('Quantos meses você tem de vida? '))
n3 = int(input('E quantos dias? '))

função(n1, n2, n3)