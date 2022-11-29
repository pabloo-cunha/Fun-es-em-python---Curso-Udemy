"""
2 - Criar 5 funções: uma para um cadastro, outra para realizar o login, outra
para mudar a senha, outra para realizar logout e ainda uma para definir qual
opção o usuário deseja escolher.
Utilize um loop while para sair do sistema apenas se o usuário desejar (criar a
opção 'sair').
Atente-se às regras:
- Só é possível realizar um cadastro se não houver nenhum anterior.
- Só é possível realizar login se houver um cadastro.
- Só é possível realizar login se o usuário informar corretamente username e
senha.
- Só é possível alterar a senha se o usuário estiver logado.
- Só é possível alterar a senha se o usuário informar corretamente a senha
atual.
- Só é possível realizar logout se o usuário estiver logado.
"""
login = False
cadastroFeito = False
op = 0
username = ''
senha = ''

def intro():
    global op
    global cadastroFeito
    global login
    while op != 5:
        print('1 - Cadastro\n2 - Login\n3 - Mudar senha\n4 - Logout\n5 - Sair')
        op = int(input('_____Opções:'))
        
        if op == 1:
            if not cadastroFeito: #Se não existir nenhum cadastro anterior
                cadastro()
            else:
                print('_____Usuario já existe!_____')
        elif op == 2:
            if cadastroFeito:
                loginSistema()
            else:
                print('_____Usuario não cadastrado_____')
        elif op == 3:
            if cadastroFeito:
                mudarSenha()
            else:
                print('_____Usuario não cadastrado_____')
        elif op == 4:
            if login:
                logout()
            else:
                print('_____Precisa estar logado!_____')
        elif op == 5:
            return 0
        
def cadastro():
    global username
    global senha
    global cadastroFeito
    username = input('_____Digite seu nome de usuario: ')
    senha = input('_____Digite sua senha: ')
    cadastroFeito = True
    print('_____Cadastro realizado com sucesso_____')
    return intro() #chama função intro de novo

def loginSistema():
    global username
    global senha
    global login
    if not login:
        testeUsuario = input('_____Username: ')
        testeSenha = input('_____Senha:')
        
        if testeUsuario == username and testeSenha == senha:
            login = True
    if login:
        print('_____Você está logado_____')
    else:
        print('_____Username ou senha incorretos_____')
    
    return intro()

def mudarSenha():
    global senha
    global login
    if login:
        testeSenha = input('_____Senha atual: ')
        
        if testeSenha == senha:
            senha = input('_____Digite sua nova senha: ')
            print('_____Senha alterada com sucesso_____')
        else:
            print('_____Senha atual incorreta_____')
    else:
        print('_____Necessario está logado_____')
    return intro()

def logout():
    global login
    login = False
    print('_____deslogado_____')
    return intro()

intro() #chama função pela primeira vez iniciando o sistema.