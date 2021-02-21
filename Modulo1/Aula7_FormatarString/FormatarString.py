"""
Os nomes das variaveis devem iniciar com letras, podem conter numeros,
separar com _ ou usar letra maiuscula, letra minuscula.
ex: nome, nome_Aluno, nomeAluno
"""

nome = 'lucas'
idade = 18
altura = 1.72
e_maior = idade > 17
peso = 55
imc = peso / altura**2

print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)
#utilizando fstrings para formatar saida de dados digitar palavra 'f' antes das aspas
print(f'{nome} tem {idade} anos de idade e seu IMC é: {imc:.2f}')  #para formatar duas casas decimais usar <nomevar>:.2f
print('{} tem {} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))  #com .format para formatar
print('{2} tem {1} anos de idade e seu IMC é: {0}'.format(nome, idade, imc))  #0.nome, 1.idade, 2.imc
print('{nm} tem {id} anos idade e seu IMC é: {i}'.format(nm=nome, id=idade, i=imc))  #parametros enomeados

