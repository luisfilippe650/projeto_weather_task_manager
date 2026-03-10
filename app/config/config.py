from app.services.city_service import existcity
from app.services.weather_service import weathernow
from app.repositories.city_repository import (add_city, delete_city, list_city, search_city)
from app.repositories.weather_repository import view_historic, save_historic



#funcao add irá chamar a função add_city do arquivo repositories/city_repository e tem a finalidade de verificar a existencia da cidade
# se existir ela adiciona á cidade e sua informações
# o retorno é um print com a menssagem de sucesso ao inserir
def add(name):

    namecity, lat, lon = existcity(name)

    if namecity == None:
        return None


    return print(add_city(namecity, lat, lon))


#função list irá chamar a função list_city do arquivo repository/list_city e tem a finalidade de retorna todas cidades adicionadas
def list():

    return print(list_city())


#função delete irá chamar a função delete_city do arquivo repository/delete_city e tem a finalidade de deletar os dados do banco
# a forma de exclusão de dados e via id
# após o sucesso da função irá retorna a mensagem:  deletado com sucesso
def delete(id):

    return print(delete_city(id))

#função tempo irá puxar os dados do search_city onde irá consultar se a cidade colocada está adicionada
#apos isso irá puxar a função weathenow e adicionar os dados obtido para obter o clima
#depois ele irá salva no historico sua consulta
#por fim o retorno de um print com suas informações
def tempo(name):

    nome, id, lat, lon = search_city(name)

    temperature, weather = weathernow(lat, lon)

    save_historic(id, temperature, weather)

    return print(
        f"na cidade {nome}, atualmente esta com o clima {weather} e com a temperatura {temperature}"
    )

#função historic tem á finalidade de retornar o historico de suas pesquisas
#
def historic():

    result = view_historic()

    return print(result)