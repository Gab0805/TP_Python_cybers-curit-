import mysql.connector as mysql
connexion = mysql.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "ecole"
)

requete = connexion.cursor()
requete.execute("select * from etudiant")
resultat_requete = requete.fetchall()
print(resultat_requete)