# Entrada de dados pelo usuario
n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))
n3 = float(input('Insira o terceiro numero: '))

# Estrutura de condições para imprimir os numeros em ordem descrescente de acordo com os dados inseridos pelo usuario
if n1 < n2 and n1 < n3 and n2 < n3:
    print(f"Os números na ordem descrescente são: {n1}, {n2}, {n3}")
elif n1 < n2 and n1 < n3 and n3 < n2:
    print(f"Os números na ordem descrescente são: {n1}, {n3}, {n2}")
elif n2 < n1 and n2 < n3 and n1 < n3:
    print(f"Os números na ordem descrescente são: {n2}, {n1}, {n3}")
elif n2 < n1 and n2 < n3 and n3 < n1:
    print(f"Os números na ordem descrescente são: {n2}, {n3}, {n1}")
elif n3 < n1 and n3 < n2 and n1 < n2:
    print(f"Os números na ordem descrescente são: {n3}, {n1}, {n2}")
elif n3 < n1 and n3 < n2 and n2 < n1:
    print(f"Os números na ordem descrescente são: {n3}, {n2}, {n1}")

### DICIONARIO DE VARIAVEIS
# n1 = numero 1
# n2 = numero 2
# n3 = numero 3