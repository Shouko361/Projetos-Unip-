# Declaração de booleana para repetição
i = True

# Estrutra de repetição para entrada de dados pelo usuario dentro dos parametros
while i == True:
    name = str(input('Insira seu nome: '))
    if len(name) >= 3:
        age = int(input('Insira a sua idade: '))
        if age >= 0 and age <= 150:
            sal = float(input('Insira o seu salario: '))
            if sal > 0:
                print('Insira o seu sexo')
                sex = str(input('F para Feminino e M para Masculino: '))
                sex = str.upper(sex)
                if sex == 'M' or sex == 'F':
                    print('Insira o seu estado civil')
                    civil = str(input('S para Solteiro, C para Casado e V para Viuvo: '))
                    civil = str.upper(civil)
                    if civil == 'S' or civil == 'C' or civil == 'V':
                        print('Dados validados!')
                        i = False
                    else:
                        i = True
                        print('Insira um estado civil valido!')
                else:
                    print('Insira um sexo valido!')
                    i = True
            else:
                print('Insira um salario valido!')
                i = True
        else:
            print('Insira uma idade valida!')
            i = True
    else:
        print('Insira um nome valido!')
        i = True



### DICIONARIO DE VARIAVEIS
# i = valor booleano para estrutura de repetição
# name = nome do usuario
# age = idade do usuario
# sal = salario do usuario
# sex = sexo do usuario
# civil = estado civil do usuario