from app.database.connection import connection


def add_city(name, lat, lon):

    database = connection()
    cursor = database.cursor()

    cursor.execute("SELECT name FROM cities WHERE name = %s", (name,))
    exists = cursor.fetchall()

    if exists:
        print("Essa cidade já existe")
        cursor.close()
        database.close()
        return None

    sql = "INSERT INTO cities(name, latitude, longitude) VALUES (%s, %s, %s)"

    city = (name, lat, lon)

    cursor.execute(sql, city)
    database.commit()

    cursor.close()
    database.close()

    return "cidade cadastrada com sucesso"


def list_city():

    database = connection()
    cursor = database.cursor()

    sql = "SELECT * FROM cities"

    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    database.close()

    return data


def delete_city(id):

    database = connection()
    cursor = database.cursor()

    sql = "DELETE FROM cities WHERE id = %s"

    cursor.execute(sql, (id,))
    database.commit()

    cursor.close()
    database.close()

    data = "deletado com sucesso"

    return data


def search_city(name):

    database = connection()
    cursor = database.cursor()

    sql = "SELECT name, id, latitude, longitude FROM cities WHERE name = %s"
    cursor.execute(sql, (name,))

    result = cursor.fetchone()

    cursor.close()
    database.close()

    if result is None:
        print("cidade não encontrada")
        return None

    name, id, lat, lon = result

    return name, id, lat, lon