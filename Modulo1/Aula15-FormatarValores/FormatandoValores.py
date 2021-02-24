"""
Formatando valores com modificadores
:s - Strings
:d - inteiro
:f - ponto flutuante
:.(numero)f - quantidade de casas decimais(float)
: (caractere) (> ou < ou ^)(quantidade) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num = 1
print(f'{num:0>10}')  # vai exibir 9 zeros antes do numero 1 (0000000001)
print(f'{num:0<10}')  # vai exibir 9 zeros depois do numero 1 (1000000000)
print(f'{num:0>10.2f}')  # vai exibir 6 zeros antes do numero 1 um . e 2 dois zero dps para cocmpletar 10 casas (0000001.00)

nome = 'Lucas Farias'
print(len('###################'))
print(f'{nome:#^50}')

nome = nome.ljust(15, '@')  # completa com @ ate 15 caracteres, ljust (esqueda) rjust(direita)
print(nome)

print('minus: ', nome.lower())  # Tranforma string em minusculo
print('maius: ', nome.upper())  # Transforma string em maiusculo
print('form: ', nome.title())  # Primeiras letras maiusculas
print('case: ', nome.casefold())  # volta pra origem sem nenhuma modificação
