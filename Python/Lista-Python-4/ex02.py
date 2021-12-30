def idade(x):
    if x >= 5 and x <=7:
        print('Infantil A')

    elif x >= 8 and x <=10:
        print('Infantil B')

    elif x >= 11 and x <= 13:
        print('Juvenil A')

    elif x >= 14 and x <= 17:
        print('Juvenil B')

    elif x >= 18:
        print('Adulto')



x = int(input('Diga sua idade: '))
idade(x)