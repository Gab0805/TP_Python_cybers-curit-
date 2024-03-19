class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.__titre = titre
        self.__auteur = auteur
        self.genre = genre
        self.__prix = prix

    #Titre
    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre
   
    #Auteur 
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur =  auteur

    #Genre
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre 

    #Prix
    def get_prix(self):
        return self.__prix
    def set_prix(self, prix):
        self.__prix = prix

    def afficher_details(self):
        print(self.get_titre())
        print(self.get_auteur())  
        print(self.get_genre())  
        print(self.get_prix())