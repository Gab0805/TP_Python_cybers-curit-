import database as db
from evenement import Evenement


class EvenementDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def ajouter_evenement(cls, evt:Evenement):
        sql = "INSERT INTO table_evenements (nom, date, emplacement, prix, images, description) VALUES (%s, %s, %s, %s, %s, %s )"
        params = (evt.nom, evt.date, evt.emplacement, evt.prix, evt.images, evt.description)
        try:
            EvenementDao.connexion.cursor()
            EvenementDao.cursor.execute(sql, params)
            EvenementDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            EvenementDao.connexion.rollback()
            message = "Error"
        return message

    @classmethod
    def lister_evenements(cls):
        sql = "SELECT * FROM table_evenements"
        try:
            EvenementDao.connexion.cursor()
            EvenementDao.cursor.execute(sql)
            events = EvenementDao.cursor.fetchall()
            message = "Success"
        except Exception as ex:
            return [], "Error"
        return events
        

    @classmethod
    def modifier_evenement(cls, event_id, evt:Evenement):
        sql = "UPDATE table_evenements SET nom=%s, date=%s, emplacement=%s, prix=%s, images=%s, description=%s WHERE id=%s"
        params = (evt.nom, evt.date, evt.emplacement, evt.prix, evt.images, evt.description, event_id)
        try:
            EvenementDao.connexion.cursor()
            EvenementDao.cursor.execute(sql, params)
            EvenementDao.connexion.commit()
            message =  "Success"
        except Exception as ex:
            EvenementDao.connexion.rollback()
            message =  "Error"
        return message
        

    @classmethod
    def supprimer_evenement(cls, event_id):
        sql = "DELETE FROM table_evenements WHERE id = %s"
        
        try:
            EvenementDao.connexion.cursor()
            EvenementDao.cursor.execute(sql, (event_id,))
            EvenementDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            EvenementDao.connexion.rollback()
            message =  "Error"
        return message
        