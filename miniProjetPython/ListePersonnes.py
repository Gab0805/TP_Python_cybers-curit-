"""
Créez une classe ListePersonnes qui contient une liste d'objets de type
Personne.
"""

class ListePersonnes : # définition de la classe ListePersonnes
    def __init__(self) :
        self.personnes = []


"""
Ajoutez une méthode ajouter_personne(nom, age) pour ajouter une nouvelle
personne à la liste
"""

def ajouter_personne(self, personne):
        titre = personne.nom # equivalent à livre.get_titre() car maintenant titre est consideré comme proprièté
        self.personnes[personne] = personne
    
   # def afficher_librairie(self):
   #     print("-----------------------------------------------")
   #     for titre,livre in self.livres.items():
    #        print(f"{titre} -> {livre.auteur}, {livre.genre}, {livre.prix}")
     #       print("---------------------------------------------")