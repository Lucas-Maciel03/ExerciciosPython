nome = 'Lucas Farias'
idade = 18
altura = 1.72
peso = 55.0
ano_atual = 2020
ano_nascimento = ano_atual - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e pesa {peso:.2f}KG.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}')

print('\nPRINTANDO COM O .FORMAT')
print('{} tem {} anos, {:.2f} de altura e pesa {:.2f}KG'.format(nome, idade, altura, peso))
print('O IMC de {} é {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, ano_nascimento))