from login import *
from cadastro import *
from nPrimo import *
from bancoDados import *
from pokeapi import *


def menu(lista_d_usuarios, lista_d_logins):
    while True:
        opcao = input("\nOque gostaria de realizar?"
                      "\n1. Cadastrar usuário"
                      "\n2. Atualizar senha"
                      "\n3. Encontrar número primo"
                      "\n4. Sair"
                      "\nOpcao: ")

        if opcao == '1':
            print("* Para cadastrar um novo usuário, precisamos verificar se você é um administrador."
                  "Preencha as informacoes a seguir!\n")
            login, senha, status = login_com_senha_protegida(lista_d_usuarios)

            cadastrar_usuario(lista_d_usuarios, lista_d_logins, login, status)

        elif opcao == '2':
            print("Antes de atualizar seus dados precisamos saber se é você mesmo (ou um administrador)")
            login, senha, status = login_com_senha_protegida(lista_d_usuarios)

            atualizar_login_senha(lista_d_usuarios, login, status)

        elif opcao == '3':
            N = int(input("Digite um número inteiro maior ou igual a 2: "))
            primo = numero_primo(N)
            print(f"Maior número primo até {N} é: {primo}")

        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Já criei alguns usuários padroes para testes

lista_de_logins = [("user1", "abc"), ("user2", "abcABC123!@#")]
lista_de_usuarios = [{"login": "Gabriel", "senha": "123-abc-ABC!", "role": "admin"},
                     {"login": "Francisco", "senha": "FR4Nc1sc0-_-", "role": "user"},
                     {"login": "Daniel", "senha": "deb3!ABE21_-", "role": "user"}]

# USUARIO ADMINISTRADOR
# USER: Gabriel
# SENHA: 123-abc-ABC!

while True:
    hash(lista_de_usuarios)  # já começo o programa protegendo as senhas existentes, por causa dos usuários testes que
    # já temos criados.

    print("Seja Bem-vindo(a) ao programa!\n")

    #   1. CRIANDO O LOGIN
    login, senha = criar_login()
    lista_de_logins.append((login, senha))
    print("\nConta criada com sucesso!\n")
    print()

    #   2. CADASTRANDO O USUARIO
    #   3. ATUALIZANDO LOGIN E SENHA
    #   4. ENCONTRANDO N PRIMO
    menu(lista_de_usuarios, lista_de_logins)
    print()

    #   5. PROTEGENDO SENHA
    hash(lista_de_usuarios)
    print("Senhas protegidas com sucesso!")
    print()

    #   6. LOGIN COM SENHA PROTEGIDA
    login_com_senha_protegida(lista_de_usuarios)
    print()

    #   7. PERSISTINDO O BANCO DE DADOS
    salvar_banco_dados(lista_de_usuarios)
    print("Banco de dados salvo com sucesso.")
    print()

    #   8. ENCONTRANDO UM ID PARA O USUARIO
    encontrando_um_id_para_o_usuario(lista_de_usuarios)
    salvar_banco_dados(lista_de_usuarios)  # Atualizando novas informacoes no banco de dados *
    print("Banco de dados atualizado com sucesso.")
    print()

    #   9. ENCONTRANDO O POKEMON DO USUARIO
    encontrando_pokemon_usuario(lista_de_usuarios)
    print()

    #   10. ATUALIZANDO BANCO DE DADOS
    salvar_banco_dados(lista_de_usuarios)
    print("Banco de dados atualizado com sucesso.")
    print()
