import mysql.connector as mysql  #cette methode n'est pas très sécuritaire. Voir database.py pour un meilleur

connexion = mysql.connect(
    user ="root",
    password ="",
    host="localhost",
    database="ecole"

)

requete = connexion.cursor()
requete.execute("select * from etudiant")
resultat_bd = requete.fetchall()

#print(resultat_bd)

print("\n-----------------------------------------------------------------")

for recherche in resultat_bd:
    print(recherche)

print("\n-----------------------------------------------------------------")

