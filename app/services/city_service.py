import requests

def existcity(name):

    url = f"https://nominatim.openstreetmap.org/search?q={name}&format=json"

    headers = {
        "User-Agent": "weather-cli-app"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Erro na requisição")
        return None

    dados = response.json()

    if len(dados) == 0:
        print("Cidade não encontrada")
        return None

    namecity = dados[0]["name"]
    lat = dados[0]["lat"]
    lon = dados[0]["lon"]

    return namecity, lat, lon