import database as db
from personne import Personne


class ListePersonnes : # définition de la classe ListePersonne
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    
    @classmethod
    def ajouter_personne(self, pers:Personne) :  # méthode pour ajouter une nouvelle personne à la liste

        # Exécution de la requête SQL pour insérer les données dans la table "personnes"
        sql_ajout = """ INSERT INTO personnes(nom, age) 
                        VALUES (%s,%s)
                    """
        values_ajout = (pers.nom, pers.age)

        try: 
            ListePersonnes.cursor.execute(sql_ajout, values_ajout)

            # Validation des modifications dans la base de données
            ListePersonnes.connexion.commit()
            afficher_message = f"La personne {pers.nom} est ajoutée avec succès."

        except Exception as exept:    
            afficher_message = "Il y a une erreur lors de l'ajout." 
            

        return afficher_message

    @classmethod                # méthode pour afficher la liste
    def afficher_personnes(cls):           
        sql_affiche = "SELECT * FROM personnes"

        try:
            ListePersonnes.cursor.execute(sql_affiche)
            pers = ListePersonnes.cursor.fetchall()
            
            afficher_message = "affiché avec Succes"
        except Exception as exept:
            print(exept)
            pers = []
            afficher_message = "Erreur lors de la récupération des données."
        return pers, afficher_message
        

    @classmethod
    def rechercher_personne(cls, nom):  # méthode pour rechercher une personne dans la liste
        sql_recherche = "SELECT nom, age FROM personnes WHERE nom = %s"
        try:
            ListePersonnes.cursor.execute(sql_recherche, (nom,))
            resultat_recherche = ListePersonnes.cursor.fetchone()
            
            afficher_message = "Personne trouvée avec succès"
        except Exception as exept:
            resultats = []
            afficher_message = "Erreur lors de la recherche: "
        return resultats, afficher_message


    @classmethod
    def filtrer_age(cls, min_age, max_age):
        sql = "SELECT nom, age FROM personnes WHERE age BETWEEN %s AND %s"
        try:
            ListePersonnes.cursor.execute(sql, (min_age, max_age))
            resultat = ListePersonnes.cursor.fetchall()
            
            afficher_message = "Success"
        except Exception as ex:
            resultat = []
            afficher_message = "Erreur lors du filtrage par âge."
        return resultat, afficher_message 

    
    

    