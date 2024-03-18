"""
Ajoutez une méthode afficher_personnes() pour afficher les détails de toutes les personnes dans la liste.
"""
#from Personne import Personne

def afficher_personne(self) : # méthode permettant d'afficher les détails des personnes dans la liste.
    for person in self.personne :
        print(f"Nom : {person.nom}, Age : {person.age}")
