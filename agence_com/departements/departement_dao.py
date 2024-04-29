import database

class DepartementDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        
        