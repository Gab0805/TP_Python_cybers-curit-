import mysql.connector

# connexion à la base de données
connexion_bd = mysql.connector.connect(
    host='localhost',
    user='root',
    password = '',
    database = 'crudpython_bd'

)
# création d'un utilisateur dans la table appelée table_utilisateurs
def crea_utilisateur(code_permanent,nom,prenom,date_naissance,specialite):
    cursor = connexion_bd.cursor()
    cursor.execute("""
        INSERT INTO table_utilisateurs (code_permanent,nom,prenom,date_naissance,specialite)
        VALUES (%s, %s, %s, %s, %s)
    """, (code_permanent,nom,prenom,date_naissance,specialite)
    )
    connexion_bd.commit()

#crea_utilisateur("nine08052001", "laforet", "jean", "08-05-2000", "gestionnaire")
#crea_utilisateur("defi01029202", "dia", "moussa", "01-02-1992", "commerçant")

# affichage de la table des utilisateurs, appelée table_utilisateurs
def afficher_utilisateur():
    cursor = connexion_bd.cursor()
    cursor.execute("SELECT * FROM table_utilisateurs")
    for (code_permanent, nom, prenom, date_naissance, specialite) in cursor:
        print(f"Code permanent: {code_permanent}, Nom: {nom}, Prénom: {prenom}, date de naissance: {date_naissance}, Spécialité: {specialite}")

# mettre à jour la table des utilisateurs en modifiant la spcécialité d'un utilisateur
def update_utilisateur(code_permanent,specialite): 
    cursor = connexion_bd.cursor()
    cursor.execute("""
        UPDATE table_utilisateurs
        SET specialite = %s           # on modifie la specialité de l'utilisateur
        WHERE code_permanent = %s     # sachant son code permanent
    """, (specialite, code_permanent)
    )
    connexion_bd.commit()
    
# suppression d'un utilisateur
def supprimer_utilisateur(code_permanent):
    cursor = connexion_bd.cursor()
    cursor.execute("""
        DELETE FROM table_utilisateurs  # on supprime de la table_utilisateurs
        WHERE code_permanent = %s       # l'utilisateur ayant le code_permanent
    """, (code_permanent,)
    )
    connexion_bd.commit()

crea_utilisateur("mado11129902", "wade", "alain", "11-12-1999", "pilote") # ajout d'un utilisateur

print("\n affchage de la table des utilisateurs:")
afficher_utilisateur()

#update_utilisateur("nine08052001", "directeur") # mise à jour des utilisateurs
    
supprimer_utilisateur("defi01029202") # suppression de l'utilisateur dont le code permanent est defi01029202

print("\n affchage de la table des utilisateurs après suppresion:")
afficher_utilisateur()



