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
imc = peso / (altura*altura)

print('nome:', nome)
print('Altura:', altura)
print('Peso:', peso)
print('Idade:', idade)
print('Maior de idade:', e_maior)
print('IMC:', imc)
print(nome, 'tem', idade, 'anos de idade e seu IMC é:', imc)