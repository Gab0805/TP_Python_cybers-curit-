#import Librairie as Librairie
from Livre import Livre
from Librairie import Librairie


# Menu : choix
"""
Creation livre
Ajout livre dans librairie
chercher un livre
supprimer un livre
Afficher tous les livres
"""
# Fonction options ... la saisie on demande au user des infos de livres pour ajouter 'a la librairie (inclure contrôle de saisie)


def choix_options():
    print("1. Créer un livre: ")
    print("2. Chercher un livre: ")
    print("3. Supprimer un livre: ")
    print("4. Afficher tous les livres: ")
    print("5. Appuyez sur q pour quitter: ")
    choix = input("Veuillez choisir parmi les options suivantes: ")
    return choix

def saisie():
    librairie = Librairie()
    while True:
        option = choix_options()
        if option == "1":
            titre  = input("Donnez le titre du livre: ")
            auteur = input("Donnez l'auteur du livre: ")
            genre  = input("Donnez le genre ou la catégorie du livre: ")
            prix   = int(input("Donnez le prix du livre: ")) # Controle de saisie a venir
            livre  = Livre(titre, auteur, genre, prix)
            librairie.ajouter_livre(livre)

        elif option == "2":
            titre  = input("Donnez le titre du livre que vous cherchez: ")
            librairie.chercher_livre(titre)
        elif option == "3":
            titre  = input("Donnez le titre du livre que vous désirez supprimer: ")
            librairie.supprimer_livre(titre)
        elif option == "4":
            librairie.afficher_librairie()
        elif option.lower() == "q":
            break
        else:
            print("Choix invalide !")

    

saisie()