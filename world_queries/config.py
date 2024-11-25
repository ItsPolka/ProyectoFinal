#Incluye la configuración de la base de datos y otras configuraciones de Flask necesarias.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

global db 
db = SQLAlchemy()


#Se crea el objeto de la base de datos usando el constructor de SQLAlchemy
def init_db(app):
    db.init_app(app)