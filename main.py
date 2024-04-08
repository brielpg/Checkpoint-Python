from login import *
from cadastro import *
from nPrimo import *
from bancoDados import *


def menu(lista_de_usuarios, lista_de_logins):
    while True:
        opcao = input("Oque gostaria de realizar?"
                      "\n1. Cadastrar usuário"
                      "\n2. Atualizar senha"
                      "\n3. Encontrar número primo"
                      "\n4. Sair"
                      "\nOpcao: ")

        if opcao == '1':
            cadastrar_usuario(lista_de_usuarios, lista_de_logins)

        elif opcao == '2':
            atualizar_login_senha(lista_de_usuarios)

        elif opcao == '3':
            N = int(input("Digite um número inteiro maior ou igual a 2: "))
            primo = numero_primo(N)
            print(f"Maior número primo até {N} é {primo}")

        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


lista_de_logins = [("user1", "abcABC123!@#"), ("user2", "abcABC123!@#")]
lista_de_usuarios = [{"login": "Teste1", "senha": "123-abc-ABC!", "role": "admin"},
                     {"login": "Teste2", "senha": "FR4Nc1sc0-_-", "role": "user"},
                     {"login": "Teste3", "senha": "deb3!ABE21_-", "role": "user"}]

# USUARIO ADMINISTRADOR
# USER: Teste1
# SENHA: 123-abc-ABC!

while True:
    print("Seja Bem-vindo(a) ao programa!\n")

    #   1. CRIANDO O LOGIN
    login, senha = criar_login()
    lista_de_logins.append((login, senha))
    print("\nConta criada com sucesso!\n")

    print(lista_de_logins)  # TESTE

    #   2. CADASTRANDO O USUARIO
    #   3. ATUALIZANDO LOGIN E SENHA
    #   4. ENCONTRANDO N PRIMO
    menu(lista_de_usuarios, lista_de_logins)

    print(lista_de_logins)  # TESTE
    print(lista_de_usuarios)  # TESTE

    #   5. PROTEGENDO SENHA
    hash(lista_de_usuarios)

    print(lista_de_usuarios)  # TESTE

    #   6. LOGIN COM SENHA PROTEGIDA
    login_com_senha_protegida(lista_de_usuarios)

    print(lista_de_usuarios)  # TESTE

    #   7. PERSISTINDO O BANCO DE DADOS
    salvar_banco_dados(lista_de_usuarios)
    print("Banco de dados salvo com sucesso.")

    #   8. ENCONTRANDO UM ID PARA O USUARIO
    encontrando_um_id_para_o_usuario(lista_de_usuarios)

    # * salvando novas informacoes no banco de dados *
    salvar_banco_dados(lista_de_usuarios)
    print("Banco de dados atualizado com sucesso.")

    #   9.
    
