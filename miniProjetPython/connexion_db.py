import mysql.connector as mysql

connexion = mysql.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "lespersonnes"
)

requete = connexion.cursor()
requete.execute("select * from personnes")
resultat_requete = requete.fetchall()
print(resultat_requete)