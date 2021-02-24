"""
Listas - Suportam valores de varios tipos diferentes
Sintaxe: NomeVar = [valores]
fatiamento[ini:fim:passo]
append, insert, pop, del, clear, extend, +
min, max
"""
l1 = [1, 35, 3]
l2 = [4, 52, 6]
l3 = l1 + l2  # concatenando listas
print(l3)
# funcoes
l1.extend(l2)  # l1 extende l2(l1 contem valores das 2 listas)
l3.append(15)  # Função append insere valores no fim da lista
l1.insert(0, 'lucas')  # Função insert insere valores com base no indice
l2.pop()  # remove o ultimo item da lista
del(l3[2:5])  #Exclui itens da lista com base no seu indice

print(max(l2))  #exibe o maior valor da lista
print(min(l2))  #exibe o menor valor da lista
print(l1)
print(l2)
print(l3)

ex = ['lucas', True, 10, 5.5]

for x in ex:
    print('Tipo de variavel {}, seu valor é: {}'.format(type(x), x))