from login import validar_login_e_senha


def cadastrar_usuario(lista_usuarios, lista_de_loginss):
    print("Para cadastrar um novo usuário, precisamos verificar se você é um administrador\nPreencha as informacoes"
          "a seguir")
    login_de_quem_esta_cadastrando = input("Seu Login: ")
    senha_de_quem_esta_cadastrando = input("Sua senha: ")

    for i in lista_usuarios:
        if i['login'] == login_de_quem_esta_cadastrando and i['senha'] == senha_de_quem_esta_cadastrando:
            if i['role'] != 'admin':
                print("Você não tem permissão para cadastrar novos usuários.")
            else:
                print("Insira os dados do usuário que deseja cadastrar")
                login_do_usuario = input("Login do usuário: ")
                senha_do_usuario = input("Digite a senha: ")

                if validar_login_e_senha(login_do_usuario, senha_do_usuario, lista_de_loginss):
                    role = input("Digite a role a ser setada (admin ou user): ")
                    if role not in ['admin', 'user']:
                        print("Role inválida. Usuário não cadastrado.")
                    else:
                        novo_usuario = {'login': login_do_usuario, 'senha': senha_do_usuario, 'role': role}
                        lista_usuarios.append(novo_usuario)
                        print("Usuário cadastrado com sucesso.")
                else:
                    print("Usuário não cadastrado.")
