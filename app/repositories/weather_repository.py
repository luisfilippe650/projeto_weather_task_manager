from app.database.connection import connection

def savehistoric(id, temp, desc):

    database = connection()
    cursor = database.cursor()

    date = (id,temp,desc)

    sql ='insert into historico_clima(cidade_id,temperatura,descricao) values (%s,%s,%s)'

    cursor.execute(sql,date)
    database.commit()

    cursor.close()
    database.close()

def viewhistoric():

    database = connection()
    cursor = database.cursor()

    sql = 'select * from historico_clima'

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    database.close()

    return result
