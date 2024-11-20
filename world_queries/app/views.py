#VIEWS
#Este archivo meneja las rutas de Flask, llamando a funciones de consulta y pasando los resultados a templates.
from flask import render_template
from flask import Blueprint,request
from .queries import cons1,cons2,cons3,cons4,cons5


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


# Define a helper to get the nested key value
def get_nested_value(item, key):
    keys = key.split('.')  # Handle dot notation for nested keys
    for k in keys:
        item = item.get(k)  # Navigate to the next level
        if item is None:
            return None  # Return None if any key is missing
    return item


# Define la ruta de consulta1
@views.route('/1',methods=['GET'])  
# Decorador para definir la ruta consulta1
def c1():
    #Importa datos y los ordena
    data = cons1()
    sort_by = request.args.get('sort_by','population')
    sort_order = request.args.get('sort_order', 'desc')
    reverse = True if sort_order == 'desc' else False

    #Intenta ordenar los datos
    try:
        sorted_data = sorted(data, key=lambda x: get_nested_value(x,sort_by), reverse=reverse)
    except Exception as e:
        print(f"Error during sorting: {e}")
        sorted_data = data 

    #print(sorted_data)
    # Renderiza el template con datos ordenados
    return render_template('consulta_1.html', results=sorted_data)


# Define la ruta de consulta2
@views.route('/2',methods=['GET'])  
# Decorador para definir la ruta consulta2
def c2():
    #Importa datos y los ordena
    data = cons2()
    sort_by = request.args.get('sort_by','Percentage')
    sort_order = request.args.get('sort_order', 'desc')
    reverse = True if sort_order == 'desc' else False

    #Intenta ordenar los datos
    try:
        sorted_data = sorted(data, key=lambda x: get_nested_value(x,sort_by), reverse=reverse)
    except Exception as e:
        print(f"Error during sorting: {e}")
        sorted_data = data 

    print(sorted_data)
    # Renderiza el template con datos ordenados
    return render_template('consulta_2.html', results=sorted_data)

# Define la ruta de consulta3
@views.route('/3')  
# Decorador para definir la ruta consulta3
def c3():
    # Renderiza
    data = cons3() 
    print (data)
    return render_template('consulta_3.html',results = data)

# Define la ruta de consulta4
@views.route('/4')  
# Decorador para definir la ruta consulta4
def c4():
    # Renderiza
    data = cons4() 
    print (data)
    return render_template('consulta_4.html',results = data)

# Define la ruta de consulta5
@views.route('/5')  
# Decorador para definir la ruta consulta5
def c5():
    # Renderiza
    data = cons5() 
    print (data)
    return render_template('consulta_5.html',results = data)