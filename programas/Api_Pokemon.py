import requests

url_base = 'https://pokeapi.co/api/v2/'

def obter_informacoes_pokemon(nome_pokemon):
    url = url_base + f"pokemon/{nome_pokemon.lower()}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return None

def listar_tipos_pokemon():
    url = url_base + "type"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        tipos = [tipo['name'] for tipo in dados['results']]
        return tipos
    else:
        return None

def obter_informacoes_tipo(tipo_pokemon):
    url = url_base + f"type/{tipo_pokemon.lower()}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        return None

def exibir_estatisticas_pokemon(nome_pokemon):
    dados_pokemon = obter_informacoes_pokemon(nome_pokemon)
    if dados_pokemon:
        print(f"\nEstatísticas de {dados_pokemon['name'].capitalize()}:")
        for stat in dados_pokemon['stats']:
            print(f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}")
    else:
        print("Pokémon não encontrado.")

while True:
    print("\nEscolha uma opção:")
    print("1 - Consultar informações de um Pokémon")
    print("2 - Listar tipos de Pokémon")
    print("3 - Exibir estatísticas de um Pokémon")
    print("4 - Informações sobre um tipo de Pokémon")
    print("0 - Sair")
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        nome_pokemon = input("Digite o nome do Pokémon: ")
        dados_pokemon = obter_informacoes_pokemon(nome_pokemon)
        if dados_pokemon:
            print(f"\nNome: {dados_pokemon['name'].capitalize()}")
            print(f"Altura: {dados_pokemon['height']}")
            print(f"Peso: {dados_pokemon['weight']}")
            print("Habilidades:")
            for habilidade in dados_pokemon['abilities']:
                print(f"- {habilidade['ability']['name'].capitalize()}")
        else:
            print("Pokémon não encontrado.")

    elif opcao == '2':
        tipos = listar_tipos_pokemon()
        if tipos:
            print("\nTipos de Pokémon disponíveis:")
            for tipo in tipos:
                print(f"- {tipo.capitalize()}")
        else:
            print("Erro ao obter tipos de Pokémon.")

    elif opcao == '3':
        nome_pokemon = input("Digite o nome do Pokémon para ver as estatísticas: ")
        exibir_estatisticas_pokemon(nome_pokemon)

    elif opcao == '4':
        tipo_pokemon = input("Digite o tipo de Pokémon para ver informações: ")
        dados_tipo = obter_informacoes_tipo(tipo_pokemon)
        if dados_tipo:
            print(f"\nInformações sobre o tipo {dados_tipo['name'].capitalize()}:")
            print("Pokémons deste tipo:")
            for pokemon in dados_tipo['pokemon']:
                print(f"- {pokemon['pokemon']['name'].capitalize()}")
        else:
            print("Tipo de Pokémon não encontrado.")

    elif opcao == '0':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, digite novamente.")
