class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._courses = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("L'âge doit être un entier.")
        self._age = value

    @property
    def courses(self):
        return self._courses

    def add_course(self, course):
        if not isinstance(course, Course):
            raise ValueError("Le cours ajouté n'est pas une instance de la classe Course.")
        self._courses.append(course)

    def display_info(self):
        course_info = ", ".join([f"{course.name} ({course.credits} crédits)" for course in self._courses])
        return f"Nom : {self.name}\nAge : {self.age}\nCours suivis : {course_info}\n"


class Course:
    def __init__(self, name, credits):
        self._name = name
        self._credits = credits

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, value):
        if not isinstance(value, int):
            raise ValueError("Les crédits doivent être un entier.")
        self._credits = value


# Création des cours
math_course = Course("Mathématiques", 4)
history_course = Course("Histoire", 3)
science_course = Course("Science", 5)
french_course = Course("Français", 3)

# Création des étudiants
alice = Student("Alice", 20)
bob = Student("Bob", 22)

# Modification des attributs avec les setters
alice.name = "Alice Smith"
alice.age = 21
math_course.name = "Mathématiques Avancées"
math_course.credits = 5

# Ajout des cours aux étudiants
alice.add_course(math_course)
alice.add_course(history_course)
bob.add_course(science_course)
bob.add_course(french_course)

# Affichage des informations des étudiants
print("Etudiant 1 :")
print(alice.display_info())

print("Etudiant 2 :")
print(bob.display_info())

# Tentative de modification invalide pour tester les setters
try:
    alice.age = "vingt-et-un"
except ValueError as e:
    print(f"Erreur : {e}")