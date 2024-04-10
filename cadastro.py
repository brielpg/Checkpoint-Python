from login import validar_login_e_senha


def cadastrar_usuario(lista_usuarios, lista_de_logins, login, status):
    if status:
        for i in lista_usuarios:
            if i['login'] == login:
                if i['role'] == 'admin':
                    print("Insira os dados do usuário que deseja cadastrar")
                    login_do_usuario = input("Login do usuário: ")
                    senha_do_usuario = input("Digite a senha: ")

                    if validar_login_e_senha(login_do_usuario, senha_do_usuario, lista_de_logins):
                        role = input("Digite a role a ser setada (admin ou user): ")
                        if role not in ['admin', 'user']:
                            print("Role inválida. Usuário não cadastrado.")
                        else:
                            novo_usuario = {'login': login_do_usuario, 'senha': senha_do_usuario, 'role': role}
                            lista_usuarios.append(novo_usuario)
                            print("Usuário cadastrado com sucesso.")
                    else:
                        print("Usuário não cadastrado.")
                elif i['role'] == 'user':
                    print("Você não tem permissão para cadastrar novos usuários.")


def encontrando_um_id_para_o_usuario(lista_usuarios):
    for id_index, i in enumerate(lista_usuarios, 1):
        i['user_id'] = id_index
    print("ID adicionado para os usuários")
