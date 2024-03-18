"""
Créez une classe ListePersonnes qui contient une liste d'objets de
type Personne.

"""

class Personne :  # définition de la claaae Personne
    def __init__(self, nom, age) :
        self.nom = nom
        self.age = age

class ListePersonne : # définition de la classe ListePersonne
    def __init__(self) :
        self.personne = []
