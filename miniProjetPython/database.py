import mysql.connector as mysql

def connexion_db():
   return mysql.connect(
        user='root',
        host='localhost',
        database='miniprojet',
        password=''   
    )
