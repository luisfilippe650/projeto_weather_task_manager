import requests

def weathernow(lat,lon):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    response = requests.get(url)

    dados = response.json()

    temperature = dados["current_weather"]["temperature"]
    code = dados["current_weather"]["weathercode"]

    weather_code_map = {
        0: "Céu limpo",

        1: "Poucas nuvens",
        2: "Parcialmente nublado",
        3: "Nublado",

        45: "Neblina",
        48: "Neblina com gelo",

        51: "Garoa leve",
        53: "Garoa moderada",
        55: "Garoa forte",

        61: "Chuva leve",
        63: "Chuva moderada",
        65: "Chuva forte",

        71: "Neve leve",
        73: "Neve moderada",
        75: "Neve forte",

        80: "Pancadas de chuva leves",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva fortes",

        95: "Tempestade",
        96: "Tempestade com granizo",
        99: "Tempestade forte com granizo"
    }

    weather = weather_code_map.get(code,"Clima desconhecido")

    #ira retorna primeiro temperatura e depois o tempo
    return temperature, weather
