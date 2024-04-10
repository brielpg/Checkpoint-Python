import json


def salvar_banco_dados(lista_usuarios):
    with open('banco_dados.json', 'w', encoding='utf-8') as file:
        json.dump(lista_usuarios, file, ensure_ascii=False, indent=4)
