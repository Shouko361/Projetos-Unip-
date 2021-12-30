# Entrada de dados pelo usuario
n1 = float(input('Insira aqui a primeira nota do aluno: '))
n2 = float(input('Insira aqui a segunda nota do aluno: '))

# Calculo da media e exibição de resultados de acordo com as variaveis
media = (n1+n2)/2

if media <= 10 and media >= 9:
    concept = 'A'
    print(f'A media foi de {media} e o aluno obteve por fim o conceito "{concept}"')
    print('O aluno foi APROVADO')
elif media < 9 and media >= 7.5:
    concept = 'B'
    print(f'A media foi de {media} e o aluno obteve por fim o conceito "{concept}"')
    print('O aluno foi APROVADO')
elif media < 7.5 and media >= 6:
    concept = 'C'
    print(f'A media foi de {media} e o aluno obteve por fim o conceito "{concept}"')
    print('O aluno foi APROVADO')
elif media < 6 and media >= 4:
    concept = 'D'
    print(f'A media foi de {media} e o aluno obteve por fim o conceito "{concept}"')
    print('O aluno foi REPROVADO')
elif media < 4 and media >= 0:
    concept = 'E'
    print(f'A media foi de {media} e o aluno obteve por fim o conceito "{concept}"')
    print('O aluno foi REPROVADO')
else:
    print('Notas inseridas erroneamente')





### DICIONARIO DE VARIAVEIS
# n1 = nota 1
# n2 = nota 2
# media = media (nota 1 + nota 2) / 2
# concept = conceito, nota final (em letra) do aluno