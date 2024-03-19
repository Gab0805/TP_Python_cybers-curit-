from Student import Student
from Course import Course

etudiant1 = Student("Armel", 40)
etudiant2 = Student("Bijou", 30)

math = Course("Math",4)
sciences = Course("sciences",5)
histoire = Course("histoire",3)
francais = Course("francais",4)
informatique = Course("informatique",6)
algo =Course("algo",3)

etudiant1.add_courses(math)
etudiant1.add_courses(algo)
etudiant1.add_courses(informatique)

etudiant1.infos()

etudiant2.add_courses(sciences)
etudiant2.add_courses(math)
etudiant2.add_courses(francais)
etudiant2.add_courses(informatique)
print(etudiant2.details())