"""
comando (pass) comando Elipsis (...)
sao usados para deixar uma parte do codiugo em branco
para que posteriormente possa ser escrito comandos lá
"""
valor = False
if valor:
    # Caso nao escreva nada aqui iria dar erro, porem foi corrigido com comando pass
    pass  # pass funciona como placeholder
elif valor:
    ...  #exemplo de elipsis
else:
    print('falso')
