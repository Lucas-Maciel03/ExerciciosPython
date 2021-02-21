"""
Entrada de Dados - O Input sempre retorna uma string, nao importa seu tipo int float etc

exemplo:
variavel = '5.5'
outra_variavel = (int(float(variavel)))
Primeiro a "variavel" era uma string, depois convertida em float e, por fim, em int. Posteriormente,
salvamos o valor da "variavel" em "outra_variavel". Portanto, o valor final é do tipo int.
"""

nome = input('Qual seu nome? ')
idade = input('qual sua idade? ')

ano_nascimento = 2021 - int(idade)  # Foi feito o casting na variavel idade para poder realizar o calculo
print(f'{nome}, nasceu em {ano_nascimento} e tem {idade} anos')

# Realizando casting ja no input
valor1 = int(input("Digite numero: "))
valor2 = float(input("Digite valor: "))

soma = valor2 + valor1
print(soma)

# Realizando casting apos te pego o valor no input
valor3 = input("\nDigite valor: ")
valor3 = int(valor3)
soma = valor3 + valor1
print(soma)
