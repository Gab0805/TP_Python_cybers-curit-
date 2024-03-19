"""
Filtrage des personnes par âge :● Ajoutez une méthode filtrer_personnes_par_age(min_age, max_age) 
à la classe ListePersonnes qui affiche les détails des personnes dont l'âge est compris entre min_age et max_age.

"""

def filter_petsonne_par_age(self, min_age, max_age) :
    for person in self.personne :
        if min_age <= person.age <= max_age :
            print(f"Nom : {person.nom}, Âge : {person.age}")