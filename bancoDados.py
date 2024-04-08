import json


def salvar_banco_dados(lista_usuarios):
    with open('banco_dados.json', 'w') as file:
        json.dump(lista_usuarios, file, indent=4)
