import database as db
from paiement import Paiement

class PaiementDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def ajout_paiement(self, pmt:Paiement):
        sql = "INSERT INTO paiement (nom_complet, telephone, email, carte_credit) VALUES (%s,%s,%s,%s)"
        params = (pmt.nom_complet, pmt.telephone,pmt.email,pmt.carte_credit)
        try:
            PaiementDao.cursor.execute(sql,params)
            PaiementDao.connexion.commit()
            message = "Success"
        except Exception as ex :
            message = "Error"
        return message