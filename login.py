import re


def criar_login():
    print("Crie sua conta seguindo os passos a seguir\n")

    while True:
        forma_de_login = str(input("Como gostaria de se registrar: "
                                   "\n1. Email"
                                   "\n2. Nome de Usuário"
                                   "\n3. CPF"
                                   "\n4. RG"
                                   "\nOpção: ")).lower()

        if forma_de_login == '1' or forma_de_login == 'email':
            email = str(input("Email (xxxxx@yyy.zzz): "))
            email = verificar_email_valido(email)
            login = email
            break

        elif forma_de_login == '2' or forma_de_login == 'nome de usuario':
            print("\n- Nomes de usuário devem apenas conter caracteres alfabéticos e numéricos. A única exceção para"
                  "caractere especial é o caractere “_”\n")
            usuario = str(input("Nome de usuário: "))
            usuario = verificar_nome_usuario_valido(usuario)
            login = usuario
            break

        elif forma_de_login == '3' or forma_de_login == 'cpf':
            cpf = str(input("CPF (XXX.XXX.XXX-XX ou XXXXXXXXXXX): "))
            cpf = verificar_cpf_valido(cpf)
            login = cpf
            break

        elif forma_de_login == '4' or forma_de_login == 'rg':
            rg = str(input("RG (XX.XXX.XXX-X ou XXXXXXXXX): "))
            rg = verificar_rg_valido(rg)
            login = rg
            break

        else:
            print("Valor Inválido, tente novamente\n")

    print("\n- Senha deverá conter ao menos 12 caracteres e ser composta por pelo menos 2 caracteres de cada tipo."
          "\n\tNumérico: 0-9"
          "\n\tAlfabético maiúsculo: A-Z"
          "\n\tAlfabético minúsculo: a-z"
          "\n\tEspeciais: !@#$%&*()[]{};,.:/\|\n")

    senha = str(input("Senha: "))
    senha = verificar_senha_valida(senha)

    return login, senha


#                           #
#       VERIFICACOES        #
#                           #
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
        print("Senha inválida! Sua senha deve conter ao menos 12 caracteres e ser composta por pelo menos 2 caracteres "
              "de cada tipo.")
        senha = str(input("Senha: "))
        return verificar_senha_valida(senha)
    else:
        print("Senha válida!")
        return senha


def verificar_email_valido(email):
    # Explicacao da expressao regular:
    # 1. ^: Início da string, $: Final da string, +: Indica que deve haver pelo menos um desses caracteres na sequência;
    # 2. [a-zA-Z0-9._%+-] corresponde aos caracteres aceitos que podem ser letras maiúsculas ou minúsculas (de A a Z),
    #                     dígitos numéricos ou qualquer um dos caracteres especiais;
    # 3. @[a-zA-Z0-9.-] deve ter um @ seguido de alguma sequencia de caracteres citados acima;
    # 4. \.[a-zA-Z]{2,} deve haver um . seguido de alguma sequencia de caracteres citados acima.

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
    # Explicacao da expressao regular:
    # 1. ^: Início da string, $: Final da string;
    # 2. \d{3}  Indica que deve haver 3 dígitos numéricos;
    # 3. \.     Indica que deve haver um ponto ".";
    # 4. -      Indica que deve haver um hífen "-";
    # 5. \d{2}  Indica que deve haver 2 dígitos numéricos;
    # 6. |      Indica que há dois padroes separados por "|", e um dos dois deve ser correspondido;
    # 7. \d{11} Indica que deve haver 11 dígitos numéricos;

    if re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$', cpf):
        print("CPF válido.")
    else:
        print("Formato de CPF inválido.")
        cpf = input("Digite novamente seu cpf, neste formato (XXX.XXX.XXX-XX ou XXXXXXXXXXX): ")
        return verificar_cpf_valido(cpf)
    return cpf


def verificar_rg_valido(rg):
    # Explicacao da expressao regular:
    # 1. ^: Início da string, $: Final da string;
    # 2. \d{2}  Indica que deve haver 2 dígitos numéricos;
    # 3. \.     Indica que deve haver um ponto ".";
    # 4. -      Indica que deve haver um hífen "-";
    # 5. \d{3}  Indica que deve haver 3 dígitos numéricos;
    # 6. \d     Indica que deve haver 1 dígito numérico;
    # 7. |      Indica que há dois padroes separados por "|" , e um dos dois deve ser correspondido;
    # 8. \d{9}  Indica que deve haver 9 dígitos numéricos;

    if re.match(r'^\d{2}\.\d{3}\.\d{3}-\d$|^\d{9}$', rg):
        print("RG válido.")
    else:
        print("Formato de RG inválido.")
        rg = input("Digite novamente seu RG, neste formato (XX.XXX.XXX-X ou XXXXXXXXX): ")
        return verificar_rg_valido(rg)
    return rg


def validar_login_e_senha(login, senha, lista_de_logins):
    login_valido = False
    senha_valida = False

    for j, i in enumerate(lista_de_logins):
        if login == i[0]:
            login_valido = True
            if senha == i[1]:
                senha_valida = True
            else:
                print("Login ou senha inválidos.")

    if login_valido and senha_valida:
        return True
    else:
        return False


def atualizar_login_senha(lista_usuarios):
    print("Antes de atualizar seus dados precisamos saber se é você mesmo (ou um administrador)")
    login_do_usuario = input("Seu Login: ")
    senha_do_usuario = input("Sua senha: ")

    for i in lista_usuarios:
        if i['login'] == login_do_usuario and i['senha'] == senha_do_usuario:
            print("Login realizado com sucesso!")

            if i['role'] == "admin":
                trocar_login_usuario = str(input("Login do usuário que deseja alterar: "))
                for n in lista_usuarios:
                    if n['login'] == trocar_login_usuario:
                        alterar_adm = str(input("O que deseja alterar do usuário?"
                                                "\n1- Login"
                                                "\n2- Senha"
                                                "\nOpçao: ")).lower()

                        # LOGIN
                        if alterar_adm == 'login' or alterar_adm == '1':
                            forma_de_login = str(input("Qual formato de login deseja utilizar? "
                                                       "\n1. Email"
                                                       "\n2. Nome de Usuário"
                                                       "\n3. CPF"
                                                       "\n4. RG"
                                                       "\nOpção: ")).lower()

                            if forma_de_login == '1' or forma_de_login == 'email':
                                email = str(input("Email (xxxxx@yyy.zzz): "))
                                email = verificar_email_valido(email)
                                n['login'] = email

                            elif forma_de_login == '2' or forma_de_login == 'nome de usuario':
                                print("\n- Nomes de usuário devem apenas conter caracteres alfabéticos e numéricos."
                                      "A única exceção para caractere especial é o caractere “_”\n")
                                usuario = str(input("Nome de usuário: "))
                                usuario = verificar_nome_usuario_valido(usuario)
                                n['login'] = usuario

                            elif forma_de_login == '3' or forma_de_login == 'cpf':
                                cpf = str(input("CPF (XXX.XXX.XXX-XX ou XXXXXXXXXXX): "))
                                cpf = verificar_cpf_valido(cpf)
                                n['login'] = cpf

                            elif forma_de_login == '4' or forma_de_login == 'rg':
                                rg = str(input("RG (XX.XXX.XXX-X ou XXXXXXXXX): "))
                                rg = verificar_rg_valido(rg)
                                n['login'] = rg

                                # SENHA
                        elif alterar_adm == "senha" or alterar_adm == '2':
                            for j in lista_usuarios:
                                if j['login'] == trocar_login_usuario:
                                    nova_senha_adm = str(input("Digite sua nova senha: "))
                                    nova_senha = verificar_senha_valida(nova_senha_adm)
                                    if nova_senha:
                                        j['senha'] = nova_senha
            else:
                opcao = str(input("O que deseja alterar?"
                                  "\n1. Login"
                                  "\n2. Senha"
                                  "\nOpcao: ")).lower()

                if opcao == '1' or opcao == 'login':
                    forma_de_loginn = str(input("Qual formato de login deseja utilizar? "
                                                "\n1. Email"
                                                "\n2. Nome de Usuário"
                                                "\n3. CPF"
                                                "\n4. RG"
                                                "\nOpção: ")).lower()
                    if forma_de_loginn == '1' or forma_de_loginn == 'email':
                        email = str(input("Email (xxxxx@yyy.zzz): "))
                        email = verificar_email_valido(email)
                        i['senha'] = email

                    elif forma_de_loginn == '2' or forma_de_loginn == 'nome de usuario':
                        print("\n- Nomes de usuário devem apenas conter caracteres alfabéticos e numéricos."
                              "A única exceção para caractere especial é o caractere “_”\n")
                        usuario = str(input("Nome de usuário: "))
                        usuario = verificar_nome_usuario_valido(usuario)
                        i['senha'] = usuario

                    elif forma_de_loginn == '3' or forma_de_loginn == 'cpf':
                        cpf = str(input("CPF (XXX.XXX.XXX-XX ou XXXXXXXXXXX): "))
                        cpf = verificar_cpf_valido(cpf)
                        i['senha'] = cpf

                    elif forma_de_loginn == '4' or forma_de_loginn == 'rg':
                        rg = str(input("RG (XX.XXX.XXX-X ou XXXXXXXXX): "))
                        rg = verificar_rg_valido(rg)
                        i['senha'] = rg

                elif opcao == '2' or opcao == 'senha':
                    alterar_senha = str(input("Digite sua nova senha: "))
                    nova_senha = verificar_senha_valida(alterar_senha)
                    if nova_senha:
                        i['senha'] = nova_senha


def proteger_senha():
    pass
