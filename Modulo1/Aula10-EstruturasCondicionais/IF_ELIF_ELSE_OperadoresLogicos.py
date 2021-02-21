"""
Operadores Logicos
and, or, not (e, ou, nao)
in e not in

se (verdadeiro and verdaeiro) = verdadeiro (and so retorna verdadeiro se os dois valores forem verdade)
if(cond1 and cond2):
    print('verdadeiro')
senao retorna verdadeiro somente quando pelo menos uma condicao for verdadeira
else(cond1 or cond2):
    print("um ou outro")
"""
# operador not pode inverter valor ex: not cond1 era verdadeiro agora passou a valer falso
a = 2
b = 3
if(not b > a):
    print('B é maior do que A')
else:
    print('A é maior do que B')
# operador not é usado pare verificar se uma variavel esta vazia
a = ''
if(not a):
    print('Variavel a esta vazia')
b = 0
if(not b):
    print('Variavel b esta vazia')

# Operador in pode verificar se existem valores especificos presentes em uma variavel
nome = 'lucas'
if('u' in nome):  #se u esta em nome print...
    print('existe a letra no seu nome')
else:
    print('nao existe')

# Operador not in pode verificar se existem valores especificos presentes em uma variavel
nome = 'Paulo'
if('P' not in nome):  #se u nao esta em nome print...
    print('nao existe a letra no seu nome')
else:
    print('Existe')