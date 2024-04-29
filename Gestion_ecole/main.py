from etudiant import Etudiant
from etudiant import create, update, list, delete
from menu import display_menu
import etudiant

def main():
    try:
        #display_menu()
  
        while(True):
            option = int(input("Quelle option voulez vous choisir: "))

            if option == 1:
                code_permanent = input("Donnez votre code permanent :")
                prenom = input("Donnez votre prénom :")
                nom = input("Donnez votre nom de famille :")
                specialite = input("Donnez votre spécialité :")
                date_naissance= input("Donnez votre date de naissance :")
                create(code_permanent,nom,prenom,specialite,date_naissance) 
            
            elif option == 2:
                code_permanent = input("Donnez le code permanent de l'étudiant à supprimer:")
                delete(code_permanent)

            elif option == 3:
                code_permanent = input("Donnez le code permanent de l'étudiant:")
                specialite= input("Donnez la nouvelle spécialité de l'étudiant:")
                #nom = input("Donnez le nom complet de l'utilisateur:")
                update(code_permanent, specialite)  
            
            elif option == 4:
                 list()

            elif option == 5:
                break   

    except ValueError:
        print("Option invalide")  

main()      
