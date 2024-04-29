import database
from employes.employe import Employe
#from employe import Employe

class EmployeDao:
    connexion = database.connect_db
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls,emp:Employe):
        sql= """ INSERT INTO employes(nom,prenom,matricule,foction,departement)
                VALUES(%s,%s,%s,%s,%s)
             """
        params = (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.departement)
        EmployeDao.cursor.execute(cls, params)
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()

        return f"l'employé dont le matricule est {emp.matricule} est ajouté avec succès"
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM employes"
        EmployeDao.cursor.execute(sql)
        employes = EmployeDao.cursor.fetchall()
        EmployeDao.cursor.close()
        return employes

    @classmethod
    def list_one(cls,matricule):
        sql = "SELECT * FROM employes WHERE matricule = %s"
        EmployeDao.cursor.execute(sql, (matricule,))
        employes = EmployeDao.cursor.fetchall()
        EmployeDao.cursor.close()
        return employes
    
    @classmethod
    def test()


