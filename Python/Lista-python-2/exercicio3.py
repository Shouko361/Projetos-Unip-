salário = float(input("Digite seu salário: "))
pc_aumento = 0.15

if salário > 1250:
    pc_aumento = 0.10
    
aumento = salário * pc_aumento

print(f"Seu aumento será de: R$ {aumento:7.2f}")