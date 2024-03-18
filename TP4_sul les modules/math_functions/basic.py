"""
Dans basic.py, définissez une fonction factorielle qui prend un entier en entrée
et retourne sa factorielle.
"""


def factorielle(n):
    if n==1 or 0:  # Si n est égale à 1 ou 0
        return 1   # alors sa factorielle est égale à 1
    else:
        return n*factorielle(n-1) # Sinon factorielle (n) = n*factorielle(n-1)