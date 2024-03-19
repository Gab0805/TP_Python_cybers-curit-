class Course:
    def __init__(self, nom, credits) -> None:
        self.nom = nom
        self.credits = credits

    # Getters and setters
    @property
    def nom(self):
        return self.__nom
    @property
    def credits(self):
        return self.__credits

    @nom.setter
    def nom(self, nom):
        self.__nom = nom   
    
    @credits.setter
    def credits(self, value):
        #if not isinstance(value, float):
         #   raise ValueError("Crédit ne peut etre qu'un nombre décimal") 
        if value>=0:
            self.__credits = value
        else:
            print("Le nombre de credit doit etre positif !")     