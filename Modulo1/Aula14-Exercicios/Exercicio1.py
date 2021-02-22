"""
Faça um programa que peça para o usuario digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario nao digite um numero
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite numero: ')

try:
    numero = int(numero)
    res = numero % 2
    if res != 0:
        print(f'{numero} é impar')
    else:
        print(f'{numero} é par')
except:
    print('ERROR')
