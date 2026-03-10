from app import connection


def add_city(name, lat, lon):

    database = connection()
    cursor = database.cursor()

    cursor.execute("SELECT nome FROM cidade WHERE nome = %s", (name,))
    exists = cursor.fetchall()

    if exists:
        print("Essa cidade já existe")
        cursor.close()
        database.close()
        return None

    sql = "INSERT INTO cidade(nome, lat, lon) VALUES (%s, %s, %s)"

    city = (name, lat, lon)

    cursor.execute(sql, city)
    database.commit()

    cursor.close()
    database.close()

    return "cidade cadastrada com sucesso"


def list_city():

    database = connection()
    cursor = database.cursor()

    sql = "SELECT * FROM cidade"

    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    database.close()

    return data


def delete_city(id):

    database = connection()
    cursor = database.cursor()

    sql = "DELETE FROM cidade WHERE id = (%s)"

    cursor.execute(sql, (id,))
    database.commit()

    cursor.close()
    database.close()

    data = "deletado com sucesso"

    return data


def search_city(name):

    database = connection()
    cursor = database.cursor()

    sql = "SELECT nome, id, lat, lon FROM cidade WHERE nome = %s"
    cursor.execute(sql, (name,))

    result = cursor.fetchone()

    cursor.close()
    database.close()

    if result is None:
        print("cidade não encontrada")
        return None

    name, id, lat, lon = result

    return name, id, lat, lon