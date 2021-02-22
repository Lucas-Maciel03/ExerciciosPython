"""
Funcao len é usada para contar caracteres de dados
nao pode ser usado em tipos numericos
sintaxe: contador = len(Variavel)
"""

nome = input('Digite nome: ')
qtd_caractere = len(nome)  # funcao len rece uma string e retorna um int
print(qtd_caractere)  # exibe quantidade de caracteres da variavel nome
print(nome, qtd_caractere, type(qtd_caractere))

print('\nSomando dois carateres')
str1 = input('digite texto: ')
str2 = input('digite texto: ')
print(f'Quantidade de caracteres é {len(str1) + len(str2)}')
