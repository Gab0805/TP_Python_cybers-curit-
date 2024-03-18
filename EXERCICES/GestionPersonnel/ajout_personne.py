"""
Ajoutez une méthode ajouter_personne(nom, age) pour ajouter une nouvelle personne à la liste. 
"""
from Personne import Personne

def ajout_personne(self, nom, age) :  # méthode pour ajouter une nouvelle personne à la liste
    nouv_personne = Personne(nom, age)
    self.personne.append(nouv_personne)
