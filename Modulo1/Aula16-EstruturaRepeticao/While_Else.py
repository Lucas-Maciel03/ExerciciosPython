"""
While/else
Contadores
Acumuladores
"""
contador = 1
acumulador = 1

while contador < 5:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else:
    print('Fim do loop')
