"""
 Creer un fichier etudiant : dans ce fichier  
creer une classe Etudiant dont les attributs sont :
     - code_permanent
     - nom
     - prenom
     - specialite
     - date_naissance
     - Creer la methode __init__()
"""
import connexion_db as db
connexion = db.connect_db()
cursor = connexion.cursor()

class Etudiant:

    def __init__(self, code_permanent, nom, prenom, specialite, date_naissance):
        self.__code_permanent = code_permanent
        self.__nom = nom
        self._prenom = prenom
        self.__specialite = specialite
        self.__date_naissance = date_naissance

    # Generer les getters and setters de tous les attributs
    @property
    def code_permanent(self):
        return self.__code_permanent

    @code_permanent.setter
    def code_permanent(self, value):
        self.__code_permanent = value

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def specialite(self):
        return self.__specialite

    @specialite.setter
    def specialite(self, value):
        self.__specialite = value

    @property
    def date_naissance(self):
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        self.__date_naissance = value

# Creer les methodes CRUD (create(), list(), delete(), update()) dans votre classe
    
# création d'un objet étudiant dans la table appelée table_etudiants
def create(code_permanent,nom,prenom,specialite,date_naissance):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO table_etudiants (code_permanent,nom,prenom,specialie,date_naissance)
        VALUES (%s, %s, %s, %s, %s)
    """, (code_permanent,nom,prenom,specialite,date_naissance)
    )
    db.commit()

# affichage de la table des étudiants, appelée table_etudiants
def list():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM table_etudiants")
    for (code_permanent, nom, prenom, specialite, date_naissance) in cursor:
        print(f"Code permanent: {code_permanent}, Nom: {nom}, Prénom: {prenom}, Spécialité: {specialite}, date de naissance: {date_naissance}")

# mettre à jour la table des étudiants en modifiant la spcécialité d'un utilisateur
def update(code_permanent,specialite): 
    cursor = db.cursor()
    cursor.execute("""
        UPDATE table_etudiants
        SET specialite = %s           # on modifie la specialité de l'étudiant
        WHERE code_permanent = %s     # sachant son code permanent
    """, (specialite, code_permanent)
    )
    db.commit()    

# suppression d'un étudiant
def delete(code_permanent):
    cursor = db.cursor()
    cursor.execute("""
        DELETE FROM table_etudiants  # on supprime de la table_etudiantss
        WHERE code_permanent = %s       # l'utilisateur ayant le code_permanent
    """, (code_permanent,)
    )
    db.commit()   


