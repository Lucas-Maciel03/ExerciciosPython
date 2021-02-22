"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, boa Tarde 12-17, Boa noite 18-23
"""

horario = input('Digite horario: ')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Digite horario entre 0 e 23')
    elif horario < 12:
        print('0-11 Bom Dia')
    elif horario < 18:
        print('12-17 Boa Tarde')
    else:
        print('18-23 Boa Noite')

else:
    print('Pfv digite um numero entre 0 e 23')