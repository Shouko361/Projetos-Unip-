def isnumber(value):
    # Tentativa de mudar o tipo para float
    try:
         float(value)
    # Caso de erro, retorna False
    except ValueError:
         return False
    return True
