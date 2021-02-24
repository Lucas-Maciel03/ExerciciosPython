"""
Estrutura Repetição For in
iterando Strings com for
Função range(start=0, stop, step=1)
Funcao range nao depende do for para funcionar, ma spodem ser usadas juntas
"""
texto = 'Python'
# para letra em texto faca
for letra in texto:
    print(letra)

for x in range(0, 10, 2):
    print(x)

# Mudando uma string
nova = ''
for letra in texto:
    if letra == 't':
        #continue  #nao quero que a letra T seja alterada
        nova = nova + letra.upper()
    elif letra == 'h':
        #break  # quero que o programa seja parado imediatamente
        nova += letra.upper()
    else:
        nova += letra
print(nova)