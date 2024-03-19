class Librairie:
    def __init__(self):
        self.livres = {}
    
    def ajouter_livre(self, livre):
        titre = livre.titre # equivalent à livre.get_titre() car maintenant titre est consideré comme proprièté
        self.livres[titre] = livre
    
    def afficher_librairie(self):
        print("-----------------------------------------------")
        for titre,livre in self.livres.items():
            print(f"{titre} -> {livre.auteur}, {livre.genre}, {livre.prix}")
            print("-----------------------------------------------")

    def supprimer_livre(self, titre):
        if titre in self.livres:
            del self.livres[titre]
            print(f"{titre}, ce livre a été bien supprimé de la collection")  
        else:
            print(f"Le livre {titre} n'est pas trouvé")

    def chercher_livre(self, titre):
        titre = titre.lower()
        if titre in self.livres:
            self.livres[titre].afficher_details()
        else:
           print(f"Le livre {titre} n'est pas trouvé")   

    def modifier_livre(self, livre):
        titre = livre.titre.lower() # on transforme le titre en minuscule
        if titre in self.livres: # On cherche le livre qui a pour titre, le titre qui a été fourni dans librairie
            livre_edit = self.livres[titre] # le livre trouvé dans la librairie
            
            livre_edit.auteur = livre.auteur # c'est la meme chose que : livre_edit.set_auteur(auteur)
            livre_edit.genre = livre.genre # livre_edit.set_genre(genre)
            livre_edit.prix = livre.prix
            #print(livre_edit)
            self.ajouter_livre(livre_edit) 
        else:
            print(f"Le livre {livre.titre} n'est pas trouvé dans notre librairie.")    
