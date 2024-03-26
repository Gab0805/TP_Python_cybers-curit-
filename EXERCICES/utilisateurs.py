import mysql.connector as mysql

"""
    CRUD: - Create -> Création d'un utilisateur     -> INSERT INTO
          - Read   -> lister les utilisateurs       -> SELECT
          - Update -> Mise à jour d'un utilisateur  -> UPDATE --- WHERE ID=
          - Delete -> Suppression d'un utilisateur  -> DELETE --- WHERE ID=
          
          UPDATE users set nom='DIALLO' WHERE ID=1
          DELETE users WHERE ID=1


"""

# On crée une foction de connexion à la base de données MySQL
def connexion_db():
    connexion = mysql.connect(
        user='root',
        password='5033677oki',
        host='localhost',
        database='ecole'
    )
    return connexion

connexion = connexion_db()

# Cration d'un utilisateur
def create_user(email, password, nom):
    
    cursor = connexion.cursor()

    sql = "INSERT INTO users(email, password, nom) VALUES(%s,%s,%s)"
    cursor.execute(sql, (email,password,nom))
    connexion.commit()

    return (nom, email)

# Lister utilisateur
def read_users():
    cursor = connexion.cursor()

    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    for user in users:
        print(user)

# update user
# UPDATE `ecole`.`users` SET `password` = '12345' WHERE (`id` = '1');        
def update_user(ID, email, password, nom):
    cursor = connexion.cursor()

    sql = "UPDATE users SET email=%s, password=%s, nom=%s WHERE id=%s"
    cursor.execute(sql, (email, password, nom, ID))
    connexion.commit()


# DELETE USER
def delete_user(ID):
    cursor = connexion.cursor()

    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (ID,))
    connexion.commit()



# main
email = input("Donnez votre adresse mail :")
password = input("Donnez votre mot de passe :")
nom = input("Donnez votre nom complet :")
user = create_user(email,password,nom)  
#delete_user(4)
update_user(1,'test@test.co','1233467','Amadou Diallo')
read_users()
#print(user)