"""
Ajoutez une méthode rechercher_personne(nom) à la classe ListePersonnes qui recherche une personne 
par son nom et affiche ses détails si elle est trouvée.

"""

def rechercher_personne(self, nom) :  # cette méthode permet de rechercher un personne par son nom et affiche ses détails si elle est trouvée.
    for person in self.personne :
        if person.nom == nom:
            print(f"Personne trouvée - Nom : {person.nom}, Âge : {person.age}")
        else: print(f"Aucune personne n'a été trouvée avec le nom {nom}")