from random import randint
import practica_git_1 as funciones_numericas

tiradas = []
for i in range(4):  # Realiza 4 tiradas de dados y las almacena en una lista, mostrándola por pantalla
    tirada = funciones_numericas.tirar_dado()
    tiradas.append(tirada)
print(f'Tus tiradas: {tiradas}')

for x in tiradas:  # Muestra si cada tirada es par o impar
    if funciones_numericas.es_par(x):
        print(f'{x} es par!')
    else:
        print(f'{x} es impar!')

print(f'Y además ...')

for a in tiradas:  # Además, genera un número aleatorio entre 1 y 100 para cada tirada y comprueba si es múltiplo
    n = randint(1, 100)
    if funciones_numericas.es_multiplo(n, a):
        print(f'{n} es múltiplo de {a}!')

