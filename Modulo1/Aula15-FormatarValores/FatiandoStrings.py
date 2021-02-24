"""
Manipulando Strings
* Indices Strings
* Fatiamento de Strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
#positivos [0123456789]
texto =    'Python abc'
#Negativos-[987654321]
texto_novo = texto[2:6]  #[inicio][fim-1] para recortar string
print(texto_novo)

texto_nw = texto[0:6:2]  #[inicio][fim][pulo] para pular casas de 2 em dois ou mais
print(texto_nw)