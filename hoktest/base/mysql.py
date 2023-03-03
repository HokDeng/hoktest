import pymysql
def mysql(sql_code):
    db=pymysql.connect(host="",
                       port=5023,
                       user="",
                       password="",
                       database="",
                       charset="utf8")
    try:
        cursor = db.cursor()
        sql = sql_code
        cursor.execute(sql)
        print("Successful")
        db.commit()
        cursor.close()
    except Exception as e:
        print(str(e))
        db.rollback()
        cursor.close()
    results=cursor.fetchone()

    return results