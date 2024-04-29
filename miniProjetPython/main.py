from personne import Personne
from gestionPersonnel import ListePersonnes
from menu_Personne import choix_options
from File_attente import File
from File_dao import FileAttente
from menu_FileAttente import menu_file
from reservation import SalleCinema
from reservation_dao import ReservationDao
from menu_salle import menu_salle


def main_menu():
    while True:
        print("\nMenu Principal")
        print("1. Gestion de la file d'attente")
        print("2. Gestion de la liste")
        print("3. Gestion des réservations")
        print("4. Quitter")
        choix = input("Entrez votre choix (1-4): ")

        if choix == '1':
            menu_file()
        elif choix == '2':
            choix_options()
        elif choix == '3':
            menu_salle()
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

main_menu()