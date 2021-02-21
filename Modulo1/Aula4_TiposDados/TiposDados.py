"""
Tipos de dados
str - String - "oii" 'exemplo'
int - inteiro - 0 1 2 -5 -8 15000
float - real/ponto flutuante - 0.0 10.5 11.5 -8.7
bool - booleano/logico - True or False (verdadeiro ou falso)
"""
# funcao type retorna o tipo de dado que esta armazenado
print('lucas', type('lucas'))
print(12, type(12))
print(5.10, type(5.10))
print(False, type(False))
print(10==10, type(10==10))
print('f'=='F', type('f'=='F'))

print(bool([]))  # verificou uma lista ela estava vazia e printou falso GERALMENTE DADOS VAZIOS SAO AVALIADOS EM FALSE

# FAZENDO TYPECASTING
print('lucas', type('lucas'), bool('lucas'))  # lucas do tipo string no ptimeiro type exibe str
# no segundo type exibe true pois foi feito casting do tipo de dado
print('10', type('10'), type(int('10')))  # convertendo de string para int
