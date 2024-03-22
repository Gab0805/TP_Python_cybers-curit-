import mysql.connector as mysql

#initialisation de la connexion a la bd
def connect_db():
    db = mysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "ecole"

    )

    return db

#Insertion
def insertion(code_permanent,nom,prenom,date_naissance,specialite): # insertion dans la table etudiant
    sql_insert = "INSERT INTO ETUDIANT (code_permanent,nom,prenom,date_naissance,specialite) VALUES (%s,%s,%s,%s,%s)"
    db = connect_db()
    cursor = db.cursor()
    parametre = (code_permanent,nom,prenom,date_naissance,specialite)
    cursor.execute(sql_insert, parametre)
    db.commit()
    
# tester l'insertion
code_permanent = input("donner le code permanent: ")
nom = input("donner le nom: ")
prenom = input("donner le prénom: ")
date_naissance = input("donner la date de naissance: ")
specialite = input("donner la spécialité: ")

insertion(code_permanent,nom,prenom,date_naissance,specialite)







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