import mysql.connector as mysql

connect_db = mysql.connect(
host= "localhost",
user= "root",
password= "",
database= "ecole"

)

cursor = connect_db.cursor() # curseur qui permet d'accéder à la bd

def insertion(): # insertion dans la table etudiant
    sql_insert = "INSERT INTO ETUDIANT (code_permanent,nom,prenom,date_naissance,specialite) VALUES ('jit111','jin','talla','1998-01-09','info')"
    cursor.execute(sql_insert)
    connect_db.commit()

def afficher():
    sql_afficher = "SELECT * FROM ETUDIANT" # ou "SELECT (code_permanent,nom,prenom,date_naissance,specialite) FROM ETUDIANT"
    cursor.execute(sql_afficher)
    etudiants = cursor.fetchall() # récupération des données 

    print (etudiants)
    exit()
    for etudiant in etudiants: # affichage 
        print(etudiant)

insertion()
afficher()

    
    
   
        
        



