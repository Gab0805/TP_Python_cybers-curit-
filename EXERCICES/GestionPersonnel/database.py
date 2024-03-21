import mysql.connector as mysql

connection_params ={
'host': "localhost",
'user': "root",
'password': "",
'database': "ecole"
}

with mysql.connector.connect(**connection_params) as db :
# faire quelque chose d'utile avec la connexion
    with db.cursor() as cursor: #cursor est un alias, on aurait pu mettre nimporte quoi
        sql = "SELECT * FROM ETUDIANT"
        cursor.execute(sql)
        etudiants = cursor.fetchall()
        print(etudiants)
        sql_insert = "INSERT INTO ETUDIANT ('code_permanent','nom','prenom','specialte')"
        db.commit()

