"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. EX.
Bom dia 0-11, boa Tarde 12-17, Boa noite 18-23
"""

horario = int(input('Digite horario: '))

if horario >= 0 and horario < 12:
    print('0-11 Bom Dia')
elif horario >= 12 and horario < 18:
    print('12-17 Boa Tarde')
elif horario >= 18 and horario < 24:
    print('18-23 Boa Noite')
else:
    print('horario inexistente')