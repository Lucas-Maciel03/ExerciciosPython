"""
Estrutura de repetição WHILE
utilizado para realizar ações enquanto
uma condição for verdadeira
"""
x = 0
while x < 10:
    if x == 3:
        #x = x + 1
        continue  # nada abaixo disso sera executado, pula pra o proximo loop
        break  # para o loop imediatamente
    print(x)
    x = x + 1

print('Acabou')