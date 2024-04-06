from login import *
from cadastro import *


def titulo():
    print("Seja Bem-vindo(a) ao programa!")


titulo()

lista_de_logins = [("user1", "abcABC123!@#"), ("user2", "abcABC123!@#")]
lista_de_usuarios = [{"login": "Teste", "senha": "123-abc-ABC!", "role": "admin"}]

# USUARIO ADMINISTRADOR
# USER: Teste
# SENHA: 123-abc-ABC!

while True:
    #   CRIANDO O LOGIN
    login, senha = criar_login()
    lista_de_logins.append((login, senha))
    print("\nConta criada com sucesso!\n")

    #   CADASTRANDO O USUARIO
    menu_cadastro_de_usuario(lista_de_usuarios, lista_de_logins)
