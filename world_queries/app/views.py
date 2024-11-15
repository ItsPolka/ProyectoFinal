#CONTROLADORES
#Este archivo meneja las rutas de Flask, llamando a funciones de consulta y pasando los resultados a templates.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta1')
def consulta_1():
    #resultados= nameOfFunction()
    #return render_template('consulta_1.html',resultados=resultados)
    return render_template('consulta_1.html')

@app.route('/consulta2')
def consulta_2():
    #resultados= nameOfFunction()
    #return render_template('consulta_2.html',resultados=resultados)
    return render_template('consulta_2.html')

@app.route('/consulta3')
def consulta_3():
    #resultados= nameOfFunction()
    #return render_template('consulta_3.html',resultados=resultados)
    return render_template('consulta_3.html')

@app.route('/consulta4')
def consulta_4():
    #resultados= nameOfFunction()
    #return render_template('consulta_4.html',resultados=resultados)
    return render_template('consulta_4.html')

@app.route('/consulta5')
def consulta_5():
    #resultados= nameOfFunction()
    #return render_template('consulta_5.html',resultados=resultados)
    return render_template('consulta_5.html')

if __name__ == "__main__":
    app.run(debug=True)
