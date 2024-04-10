import requests
from login import login_com_senha_protegida


def encontrando_pokemon_usuario(lista_usuarios):
    login, senha, status = login_com_senha_protegida(lista_usuarios)

    for i in lista_usuarios:
        if i["login"] == login:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i["user_id"]}')
            if response.status_code == 200:
                dados_pokemon_usuario = {}

                dados_pokemon_usuario["name"] = response.json()["name"]

                habilidades = []
                for j in response.json()["abilities"]:
                    nome_habilidade = j["ability"]["name"]
                    url_habilidade = j["ability"]["url"]
                    response_habilidade = requests.get(url_habilidade)

                    if response_habilidade.status_code == 200:
                        dados_habilidade = response_habilidade.json()
                        nomes = [(flavor["language"]["name"], flavor["name"]) for flavor in dados_habilidade["names"]]
                        efeitos = [effect["effect"] for effect in dados_habilidade["effect_entries"]]
                        flavors = [flavor["flavor_text"] for flavor in dados_habilidade["flavor_text_entries"]]
                        habilidades.append({"nomes": nomes, "efeitos": efeitos, "flavors": flavors})

                dados_pokemon_usuario["abilities"] = habilidades

                i["poke_human"] = dados_pokemon_usuario
                print("Dados do pokémon adicionados ao usuário com sucesso!")
