class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.titre = titre # set_titre(titre)
        self.auteur = auteur 
        self.genre = genre
        self.prix = prix

    #Titre - accès à lecture
    @property # property nous renseigne que l'attribut titre est maintenant privé   
    def titre(self):
        return self.__titre # ici on garde les deux tirets bas.
   
    # titre - accès à la modification.
    @titre.setter
    def titre(self, titre):
        self.__titre = titre
   
    #Auteur
    @property     
    def auteur(self):
        return self.__auteur
    
    @auteur.setter
    def auteur(self, auteur):
        self.__auteur =  auteur

    #Genre
    @property    
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    #Prix  ----   Brouiller les attribut --- algorithme de bruillage  -----
    @property    
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, prix):
        if not isinstance(prix, float): # True ou False
            # Générer une BaseException() ou ValueError
            raise ValueError("Le prix ne peut etre qu'un nombre entier ou décimal")
        self.__prix = prix
        

    def afficher_details(self):
        print(self.titre())
        print(self.auteur())  
        print(self.genre())  
        print(self.prix())