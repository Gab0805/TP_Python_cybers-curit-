from gestionPersonnel import ListePersonnes
from personne import Personne
import database as db


def choix_options():
    while True:
        print("1. Ajouter une personne: ")
        print("2. Afficher la liste de personnes: ")
        print("3. Chercher une personne ")
        print("4. filtrer la liste selon l'age ")
        print("5. Appuyez sur q pour quitter: ")

        choix = input("Veuillez choisir l'une des options ci-dessus: ")
 
        if choix == "1":
            nom  = input("Donnez le nom de la personne à ajouter: ")
            age = input("Donnez l'âge de la personne: ")
            personne_a_rajouter  = Personne(nom, age)
            afficher_message = ListePersonnes.ajouter_personne(personne_a_rajouter)
            print(afficher_message)
       

        elif choix == "2":
            personnes, afficher_message = ListePersonnes.afficher_personnes()
            if personnes:
                for pers in personnes:
                    print(f"Nom : {pers[0]}, Age : {pers[1]}")
            else:
                print(afficher_message)
        
        
        elif choix == '3':
            nom = input("Entrez le nom de la personne à rechercher : ")
            resultats, afficher_message = ListePersonnes.rechercher_personne(nom)
            if resultats:
                    print(f"Nom : {resultats[0]}, Age : {resultats[1]}")
            else:
                print(afficher_message)

        elif choix == '4':
            min_age = input("Entrez l'âge minimum : ")
            max_age = input("Entrez l'âge maximum : ")
            resultat, afficher_message = ListePersonnes.filtre_age(int(min_age), int(max_age))
            if resultat:
                for pers in resultat:
                    print(f"Nom : {pers[0]}, Age : {pers[1]}")
            else:
                print(afficher_message)


        elif choix == '5':
            print("Au revoir !")
            return
        else:
            print("Choix invalide, veuillez réessayer.")



    






