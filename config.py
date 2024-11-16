#Incluye la configuración de la base de datos y otras configuraciones de Flask necesarias.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy ()


#Se crea el onjeto de la base de datos usando el constructor de SQLAlchemy
def init_db(app):
    db.init_app(app)
    
    
