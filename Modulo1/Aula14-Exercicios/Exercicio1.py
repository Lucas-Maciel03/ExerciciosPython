"""
Faça um programa que peça para o usuario digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um numero
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite numero: ')

if(numero.isdigit()):
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')
else:
    print('Isso nao é um numero')
