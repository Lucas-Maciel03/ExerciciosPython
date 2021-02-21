login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
compLogin = 'adm'
compSenha = '123a'
if(login == compLogin and senha == compSenha):
    print('Bem vindo ao sistema')
else:
    print('Usuario nao cadastrado')