import mysql.connector as mysql  #cette methode n'est pas très sécuritaire. Voir database.py pour un meilleur

# fonction de conexion a la base de données
def connect_db():
    connexion = mysql.connect(
    user ="root",
    password ="",
    host="localhost",
    database="ecole"

)
    return connexion

# une fonction d'insertion d'un étudiant
def insert_db(code_permanent,nom,prenom,date_naissance,specialite):
    var_insert = "INSERT INTO ETUDIANT (code_permanent,nom,prenom,date_naissance,specialite) VALUES (%s,%s,%s,%s,%s)"
    connection_bd= connect_db()
    cursor = connection_bd.cursor()
    parametre_insert = (code_permanent,nom,prenom,date_naissance,specialite)
    cursor.execute(var_insert, parametre_insert)
    connection_bd.commit()

    

# une fonction pour afficher tous les etudiants.
def afficher_db():
    code_permanent = input("donner le code permanent: ")
    nom = input("donner le nom: ")
    prenom = input("donner le prénom: ")
    date_naissance = input("donner la date de naissance: ")
    specialite = input("donner la spécialité: ")

    insert_db(code_permanent,nom,prenom,date_naissance,specialite)

afficher_db()






