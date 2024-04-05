import re


def criar_login():
    print("Crie sua conta seguindo os passos a seguir\n")

    forma_de_login = str(input("Como gostaria de se registrar: "
                               "\n1. EMAIL"
                               "\n2. Nome de Usuário"
                               "\n3. CPF"
                               "\n4. RG"
                               "\nOpção: "))

    if forma_de_login == '1' or forma_de_login == 'email':
        email = str(input("Email (xxxxx@yyy.zzz): "))
        email = verificar_email_valido(email)

    elif forma_de_login == '2' or forma_de_login == 'nome de usuario':
        print("\n- Nomes de usuário devem apenas conter caracteres alfabéticos e numéricos. A única exceção para caractere especial é o caractere “_”\n")
        usuario = str(input("Nome de usuário: "))
        usuario = verificar_nome_usuario_valido(usuario)

    elif forma_de_login == '3' or forma_de_login == 'cpf':
        cpf = str(input("CPF (XXX.XXX.XXX-XX ou XXXXXXXXXXX): "))
        cpf = verificar_cpf_valido(cpf)

    elif forma_de_login == '4' or forma_de_login == 'rg':
        rg = str(input("RG (XX.XXX.XXX-X ou XXXXXXXXX): "))
        rg = verificar_rg_valido(rg)

    print("\n- Senha deverá conter ao menos 12 caracteres e ser composta por pelo menos 2 caracteres de cada tipo."
          "\n\tNumérico: 0-9"
          "\n\tAlfabético maiúsculo: A-Z"
          "\n\tAlfabético minúsculo: a-z"
          "\n\tEspeciais: !@#$%&*()[]{};,.:/\|\n")
    senha = str(input("Senha: "))
    senha = verificar_senha_valida(senha)


def verificar_senha_valida(senha):
    valida = False
    numeros = 0
    maiusculas = 0
    minusculas = 0
    caracteres_especiais = 0

    for i in senha:
        if i.isdigit():
            numeros += 1
        elif i.isupper():
            maiusculas += 1
        elif i.islower():
            minusculas += 1
        elif i in '!@#$%&*()[]{};,.:/|':
            caracteres_especiais += 1

    if numeros >= 2 and maiusculas >= 2 and minusculas >= 2 and caracteres_especiais >= 2 and len(senha) >= 12:
        valida = True

    if not valida:
        print(
            "Senha inválida! Sua senha deve conter ao menos 12 caracteres e ser composta por pelo menos 2 caracteres de cada tipo.")
        senha = str(input("Senha: "))
        return verificar_senha_valida(senha)
    else:
        print("Senha válida!")
        return senha


def verificar_email_valido(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print("Email válido.")
    else:
        print("Formato de email inválido.")
        email = input("Digite novamente seu email, neste formato (xxxxx@yyy.zzz): ")
        return verificar_email_valido(email)
    return email


def verificar_nome_usuario_valido(usuario):
    for i in usuario:
        if not (i.isalnum() or i == "_"):
            print("Nome de usuário inválido! Por favor, use apenas letras, números e underscores(\"_\").")
            usuario = input("Digite um novo nome de usuário: ")
            return verificar_nome_usuario_valido(usuario)

    print("Nome de usuário válido!")
    return usuario


def verificar_cpf_valido(cpf):
    if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
        print("CPF válido.")
    else:
        print("Formato de CPF inválido.")
        cpf = input("Digite novamente seu cpf, neste formato (XXX.XXX.XXX-XX ou XXXXXXXXXXX): ")
        return verificar_cpf_valido(cpf)
    return cpf


def verificar_rg_valido(rg):
    if re.match(r'^\d{2}\.\d{3}\.\d{3}-\d{1}$|^\d{9}$', rg):
        print("RG válido.")
    else:
        print("Formato de RG inválido.")
        rg = input("Digite novamente seu RG, neste formato (XX.XXX.XXX-X ou XXXXXXXXX): ")
        return verificar_rg_valido(rg)
    return rg


def validar_login():
    pass
