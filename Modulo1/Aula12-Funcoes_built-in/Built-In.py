"""
Funcoes (isnumeric, isdigit, isdecimal)
verificam se uma variavel recebida pelo input(str)
pode ser convertida para numero int ou float
"""
num1 = input('Digite numero: ')
num2 = input('Digite Numero: ')
# as funcoes checam se a variavel possui numeros positivos(de 0 p/ acima)
# nao checam variavei q possuem '.' 2.5, 3.4 etc...
print(num2.isnumeric())

# uma maneira de corrigir isso é atraves do try - exception
num1 = input('Digite numero: ')
num2 = input('Digite Numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')