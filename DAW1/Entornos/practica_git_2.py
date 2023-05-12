import practica_git_1 as funciones_numericas

tiradas = []
for i in range(4):
    tirada = funciones_numericas.tirar_dado()
    tiradas.append(tirada)
    print(f'Tus tiradas: {tiradas}')

for x in tiradas:
    if funciones_numericas.es_par(x):
        print(f'{x} es par!')
    else:
        print(f'{x} es impar!')
