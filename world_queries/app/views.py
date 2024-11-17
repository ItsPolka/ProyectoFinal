#VIEWS
#Este archivo meneja las rutas de Flask, llamando a funciones de consulta y pasando los resultados a templates.
from flask import render_template
from flask import Blueprint
from .queries import cons1

views = Blueprint('views', __name__)

# Define la ruta de inicio
@views.route('/')  
# Decorador para definir la ruta raíz
def index():
    # Renderiza el template 'index.html'
    return render_template('index.html')

# Define la ruta de about
@views.route('/about')  
# Decorador para definir la ruta about
def about():
    # Renderiza el template 'index.html'
    return render_template('about.html')

# Define la ruta de consulta1
@views.route('/1')  
# Decorador para definir la ruta consulta1
def c1():

    processed_text = cons1()

    # Renderiza el template 'index.html'
    return render_template('consulta_1.html')

# Define la ruta de consulta2
@views.route('/2')  
# Decorador para definir la ruta consulta2
def c2():
    # Renderiza el template 'index.html'
    return render_template('consulta_2.html')

# Define la ruta de consulta3
@views.route('/3')  
# Decorador para definir la ruta consulta3
def c3():
    # Renderiza el template 'index.html'
    return render_template('consulta_3.html')

# Define la ruta de consulta4
@views.route('/4')  
# Decorador para definir la ruta consulta4
def c4():
    # Renderiza el template 'index.html'
    return render_template('consulta_4.html')

# Define la ruta de consulta5
@views.route('/5')  
# Decorador para definir la ruta consulta5
def c5():
    # Renderiza el template 'index.html'
    return render_template('consulta_5.html')