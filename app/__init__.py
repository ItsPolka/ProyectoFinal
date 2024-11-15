# Inicializa la aplicación Flask, configura SQLAlchemy y establece las 
# configuraciones necesarias para conectarse a la base de datos World.
from flask import Flask, render_template

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)

    # Define la ruta de inicio
    @app.route('/')  # Decorador para definir la ruta raíz
    def index():
        # Datos que se pasarán al template
        data = {
            'titulo': 'World Database Project',
            'bienvenida': 'Prueba'
        }
        # Renderiza el template 'index.html' pasando los datos del diccionario `data`
        return render_template('index.html', data=data)

    # Define el manejador para la página de error 404
    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        # Renderiza el template '404.html' en caso de que la página no sea encontrada
        return render_template('404.html'), 404

    return app  # Retorna la instancia de la aplicación