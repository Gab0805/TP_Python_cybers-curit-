"""
Creer un fichier connexion_db : dans ce fichier
creer une fonction de connexion à la votre base de données
"""

import mysql.connector

# connexion à la base de données

def connect_db():
    connects = mysql.connector.connect(
    host='localhost',
    user='root',
    password = '',
    database = 'etudiant_db'
)

    return connects