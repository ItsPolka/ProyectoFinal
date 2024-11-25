# Inicializa la aplicación Flask, configura SQLAlchemy y establece las 
# configuraciones necesarias para conectarse a la base de datos World.
from flask import Flask, render_template
from .views import views
from config import db


def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)
    app.register_blueprint(views)
    
    #Configura la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/world'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
     # Renderiza el template '404.html' en caso de que la página no sea encontrada
        return render_template('404.html'), 404
    
    return app  # Retorna la instancia de la aplicación