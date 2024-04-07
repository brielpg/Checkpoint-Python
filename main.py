from login import *
from cadastro import *
from nPrimo import *


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
lista_de_usuarios = [{"login": "Teste", "senha": "123-abc-ABC!", "role": "admin"}]

# USUARIO ADMINISTRADOR
# USER: Teste
# SENHA: 123-abc-ABC!

while True:
    print("Seja Bem-vindo(a) ao programa!\n")

    #   1. CRIANDO O LOGIN
    login, senha = criar_login()
    lista_de_logins.append((login, senha))
    print("\nConta criada com sucesso!\n")

    #   2. CADASTRANDO O USUARIO
    #   3. ATUALIZANDO LOGIN E SENHA
    #   4. ENCONTRANDO N PRIMO
    menu(lista_de_usuarios, lista_de_logins)

    #   5. PROTEGENDO SENHA
    proteger_senha()
