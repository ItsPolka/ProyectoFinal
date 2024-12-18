# Archivo principal para ejecutar la aplicación Flask.
from app import create_app
from config import db

# Crea una instancia de la aplicación llamando a `create_app()`
# Esto permite que la configuración y las rutas se carguen correctamente
app = create_app()

with app.app_context():
    db.create_all()

# Verifica si este archivo se está ejecutando directamente
if __name__ == "__main__":
    app.run(debug=True)