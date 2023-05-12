from random import randint

def tirar_dado():
    return randint(1, 6)

def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def es_multiplo(n, nx):
    if n % nx == 0:
        return True
    else:
        return False
