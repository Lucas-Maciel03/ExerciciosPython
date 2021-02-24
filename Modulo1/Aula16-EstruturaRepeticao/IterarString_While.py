"""
Iterando Strings com laço While
obs: o laco while nao é muito recomendado para essa tarefa
mais usado é o laço for
ITERAR É O ATO DE PERCORRER TODOS OS ELEMENTOS DE SUA STRING LISTA ETC..

# Indices
# 0123456789.............33
"""
frase = 'O rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
copy = ''
while contador < tamanho:
    print(contador, frase[contador])
    copy += frase[contador]
    contador += 1
print(copy)