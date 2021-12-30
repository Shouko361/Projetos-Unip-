lado1 = float(input('Primeiro lado:'))
lado2 = float(input('Segundo lado:'))
lado3 = float(input('Terceiro lado:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os lados escritos PODEM formar um triângulo ', end='')
    if lado1 == lado2 == lado3:
        print('equilátero!')

    elif lado1 != lado2 != lado3:
        print('escaleno!')

    else:
        print('isósceles!')

else:
    print('Os lados escritos NÃO PODEM formar um triângulo!')