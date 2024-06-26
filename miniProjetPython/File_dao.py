import database as db
from File_attente import File

class FileAttente:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_personne_en_attente(cls, fil:File):
        sql_ajout = "INSERT INTO fileattente (nom, prioritaire) VALUES (%s,%s)"
        params = (fil.nom, bool(fil.prioritaire))
        try:
            FileAttente.cursor.execute(sql_ajout, params)
            FileAttente.connexion.commit()
            etat = "prioritaire" if fil.prioritaire else "normale"
            message = f"{fil.nom} a été ajouté(e) à la file d'attente comme une personne {etat}."
        except Exception as ex:
            print(f"Erreur lors de l'ajout à la file d'attente: ")
        return message
    
    @classmethod        
    def ajouter_personne_prioritaire(cls,fil:File):
        fil.prioritaire = True
        return FileAttente.ajouter_personne_en_attente(fil)

    @classmethod
    def supprimer_personne_de_attente(cls):
        sql_prioritaire = "SELECT id, nom FROM FileAttente WHERE prioritaire = TRUE ORDER BY id ASC LIMIT 1"
        sql_non_prioritaire = "SELECT id, nom FROM FileAttente WHERE prioritaire = FALSE OR prioritaire IS NULL ORDER BY id ASC LIMIT 1"
        sql_suppression = "DELETE FROM fileattente WHERE id = %s"
        try:
            FileAttente.cursor.execute(sql_prioritaire)
            personne = FileAttente.cursor.fetchone()
            if not personne:
                FileAttente.cursor.execute(sql_non_prioritaire)
                personne = FileAttente.cursor.fetchone()
            elif personne:
                id_personne, nom_personne = personne
                FileAttente.cursor.execute(sql_suppression, (id_personne,))
                FileAttente.connexion.commit()
                message = f"{nom_personne} a été supprimé(e) de la file d'attente."
        
        except Exception as ex:
            message = f"Erreur lors de la suppression de la file d'attente: "
        return message