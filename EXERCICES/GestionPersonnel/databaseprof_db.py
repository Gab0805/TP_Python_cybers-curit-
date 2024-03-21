import mysql.connector as mysql

#initialisation de la connexion a la bd
def connect_db():
    db = mysql.connect(
        host= "localhost",
        user= "root",
        password= "",
        database= "ecole"

    )

    cursor = db.cursor() # curseur qui permet d'accéder à la bd
    return cursor

#Insertion
def insertion(): # insertion dans la table etudiant
    sql_insert = "INSERT INTO ETUDIANT (code_permanent,nom,prenom,date_naissance,specialite) VALUES (%s,%s,%s,%s,%s)"
    cursor = connect_db()
    infos = (cursor.lastrowid, code_permanent,nom,prenom,date_naissance,specialite)
    cursor.execute(sql_insert, infos)







"""
def afficher():
    sql_afficher = "SELECT * FROM ETUDIANT" # ou SELECT (code_permanent,nom,prenom,date_naissance,specialite) FROM ETUDIANT
    cursor.execute(sql_afficher)
    etudiants = cursor.fetchall() # récupération des données 

    print (etudiants)
    exit()
    for etudiant in etudiants: # affichage 
        print(etudiant)

insertion()
afficher()

"""