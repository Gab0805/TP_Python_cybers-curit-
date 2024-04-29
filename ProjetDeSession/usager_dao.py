import database as db
from flask import Flask
import bcrypt
#import flask_bcrypt as bcrypt
from usager import Usager

class UsagerDao:
    connexion = db.connexion_db()
    cursor = connexion.cursor()
    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, usr:Usager):
       
        sql = "INSERT INTO table_usagers (nom_complet, username, password, email, status) VALUES (%s, %s, %s, %s, %s)"
        params = (usr.nom_complet, usr.username, usr.password,usr.email,usr.status)
        try:
            UsagerDao.cursor.execute(sql,params)
            UsagerDao.connexion.commit()
            message = "Success"
        except Exception as exc:
            message = "Error"
        return message
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM table_usagers"
        UsagerDao.cursor.execute(sql)
        user = UsagerDao.cursor.fetchall()
        
        return user
    
    @classmethod
    def get_one(cls,username,password):
        sql = "SELECT * FROM table_usagers WHERE username=%s"
        try:
            UsagerDao.cursor.execute(sql, (username,))
            user = UsagerDao.cursor.fetchone()
            if user:
                if bcrypt.check_password_hash(user[3], password):
                    message = "Success"
        except Exception as ex:
            message = "Error"
            user = []
        return (message,user)
    
    @classmethod
    def get_by_username(cls, username):
        sql = "SELECT * FROM table_usagers WHERE username = %s"
        try:
            UsagerDao.cursor.execute(sql, (username,))
            user = UsagerDao.cursor.fetchone()
            message = "Success"
        except Exception as ex:
            message = "Error"
            user = []
        return (message, user)
    
    @classmethod
    def edit_user_status(cls, user_id,  new_status):
        sql = "UPDATE table_usagers SET status=%s WHERE id=%s"
        
        try:
            UsagerDao.connexion.cursor()
            UsagerDao.cursor.execute(sql, (new_status, user_id))
            UsagerDao.connexion.commit()
            message =  "Success"
        except Exception as ex:
            UsagerDao.connexion.rollback()
            message =  "Error"
        return message
    
    def delete_user(user_id):
        sql = "DELETE FROM table_usagers WHERE id = %s"
        try:
            UsagerDao.connexion.cursor()
            UsagerDao.cursor.execute(sql, (user_id,))
            UsagerDao.connexion.commit()
            message = "Success"
        except Exception as ex:
            UsagerDao.connexion.rollback()
            message = "Error"
        return message