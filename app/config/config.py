from app.services.city_service import existcity
from app.services.weather_service import weathernow
from app.repositories.city_repository import addcity,deletecity,listcity,searchcity
from app.repositories.weather_repository import viewhistoric, savehistoric

#finalizada
def add(name):

    namecity, lat, lon = existcity(name)

    if namecity == None:
        return None

    #vai printar a mensagem que salvou corretamente

    return print(addcity(namecity,lat,lon))

#finalizada
def list():

    return print(listcity())

#finalizada
def delete(id):

    return print(deletecity(id))


def waether(name):

    name, id,lat,lon = searchcity(name)

    temperature, weather = weathernow(lat,lon)

    savehistoric(id,temperature,weather)

    return print(f"na cidade {name}, atualmente esta com o clima {weather} e com a temperatura {temperature}")

def historic():

    result = viewhistoric()

    return print(result)






