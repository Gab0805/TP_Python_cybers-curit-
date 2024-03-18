"""
Création d'un module Python
Créez un fichier nommé operations.py.
Dans ce fichier, définissez une fonction addition qui prend deux nombres en
entrée et retourne leur somme.
Définissez également une fonction multiplication qui prend deux nombres en
entrée et retourne leur produit.

"""

def addition (nb1, nb2): # addition prend deux nombres
    return nb1+nb2       # et retourne leur somme

def multiplication (nb1, nb2): # multiplication prend deux nombres
    return nb1*nb2             # et retourne leur produit

"""
# controle de saisie 
while True:  
    try:
        a = float(input("Donnez un nombre: "))
        b = float(input("Donnez un nombre: "))
        print (f"la somme des deux nombres {a} et {b} est:", addition(a,b))
        print (f"le produit des deux nombres {a} et {b} est:", multiplication(a,b))
        break
    except ValueError:
        print("Erreur, vous avez entré un caractére")

"""

