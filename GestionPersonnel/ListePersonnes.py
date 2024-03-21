"""
Créez une classe ListePersonnes qui contient une liste d'objets de
type Personne.

"""

class Personne : # définition de la claaae Personne
    def __init__(self, nom, age) :
        self.nom = nom
        self.age = age

class ListePersonne : # définition de la classe ListePersonne
    def __init__(self) :
        self.personnes = []

"""
Ajoutez une méthode ajouter_personne(nom, age) pour ajouter une nouvelle personne à la liste. 
"""

def ajout_personne(self, personne) : # méthode pour ajouter une nouvelle personne à la liste
    nouv_personne = Personne(personne)
    self.personne.append(nouv_personne)

"""
Ajoutez une méthode afficher_personnes() pour afficher les détails de toutes les personnes dans la liste.
"""
#from Personne import Personne

def afficher_personne(self) : # méthode permettant d'afficher les détails des personnes dans la liste.
    for person in self.personne :
        print(f"Nom : {person.nom}, Age : {person.age}")

"""
Ajoutez une méthode rechercher_personne(nom) à la classe ListePersonnes qui recherche une personne 
par son nom et affiche ses détails si elle est trouvée.

"""

def rechercher_personne(self, nom) :  # cette méthode permet de rechercher un personne par son nom et affiche ses détails si elle est trouvée.