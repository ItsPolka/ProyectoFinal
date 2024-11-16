#VIEWS
#Este archivo meneja las rutas de Flask, llamando a funciones de consulta y pasando los resultados a templates.
from flask import render_template
from flask import Blueprint

views = Blueprint('views', __name__)

    # Define la ruta de inicio
@views.route('/')  # Decorador para definir la ruta raíz
def index():
    # Renderiza el template 'index.html'
    return render_template('index.html')