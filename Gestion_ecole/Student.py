class Student:
    def __init__(self, nom, age) -> None:
        self.nom = nom
        self.age = age
        self.courses = []

    # getters and setters
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom):
        self.__nom = nom

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError("L'age ne peut etre qu'un nombre entier")
        self.__age = age
    
    def add_courses(self, course):
        self.courses.append(course)

    def infos(self):
        print("--------------------------------------------------------")
        print(f"Nom : {self.__nom}")
        print(f"Age : {self.__age}")
        # Parcourir la liste des cours.
        print("Liste des cours : ")
        i = 1
        for course in self.courses:
            print(f"{i}. {course.nom}, crédits: {course.credits}")
            i+=1
        print("--------------------------------------------------------")    


    def details(self):
        course_info = ", ".join([f"{course.nom} ({course.credits} crédits)" for course in self.courses])
        return f"Nom : {self.nom}\nAge : {self.age}\nCours suivis : {course_info}\n"
