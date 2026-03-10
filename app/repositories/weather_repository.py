from app import connection


def save_historic(id, temp, desc):

    database = connection()
    cursor = database.cursor()

    data = (id, temp, desc)

    sql = "INSERT INTO historico_clima(cidade_id, temperatura, descricao) VALUES (%s, %s, %s)"

    cursor.execute(sql, data)
    database.commit()

    cursor.close()
    database.close()


def view_historic():

    database = connection()
    cursor = database.cursor()

    sql = "SELECT * FROM historico_clima"

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    database.close()

    return result