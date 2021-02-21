"""
Operadores Relacionais - Condição IF,ELIF, ELSE
== igualdade
> maior que  >= maior ou igual
< menor que  <= menor ou igual
!= diferente
"""
print('Exemplo 1')
nome = input('Informe nome: ')
idade = int(input('Informe idade: '))
idade_minima = 18

if(idade >= idade_minima):
    print(f'{nome} pode realizar o emprestimo')
else:
    print(f'{nome} NAO pode realizar o emprestimo')

print('\nExemplo 2')
nome = input('Informe nome: ')
idade = int(input('Informe idade: '))
idade_menor = 20
idade_maior = 30

if(idade >= idade_menor and idade <= idade_maior):
    print(f'{nome} pode realizar o emprestimo')
else:
    print(f'{nome} NAO pode realizar o emprestimo')

print('\nExemplo 3')
if(2==3):
    print('valores iguais')
elif(2>3):
    print('valores diferentes')
elif(2<3):
    print('2 é menor que 3')
else:
    print('fim')