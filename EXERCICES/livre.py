class livre :
    def __init__(self, titre, auteur, genre, prix) :
        self.title = titre
        self.author = auteur
        self.genre = genre
        self.price = prix

    # Getters
    def get_titre(self) :
        return self.titre

    def get_auteur(self) :
        return self.auteur

    def get_genre(self) :
        return self.genre

    def get_prix(self) :
        return self.prix

    # Régleurs
    def set_titre(self, titre) :
        self.titre = titre

    def set_auteur(self, auteur) :
        self.auteur = auteur

    def set_genre(self, genre) :
        self.genre = genre

    def set_prix(self, prix) :
        self.prix = prix

    def display_details(self) :
        print( "Titre : {self.titre}, Auteur : {self.auteur}, Genre : {self.genre}, Prix : ${self.prix}")

class Librairie :
    def __init__(self) :
        self.livre = {}

    def ajouter_livre(self, livre) :
        self.livre[livre.get_titre()] = livre

    def supprimer_livre(self, titre) :
        if titre in self.livre :
            del self.livre[titre]
        else :
            print("Livre introuvable dans la collection")

    def recherche_livre(self, titre) :
        if titre in self.recherche_livre :
            self.livre[titre].display_details()
        else :
            print("Livre non trouvé dans la collection.")