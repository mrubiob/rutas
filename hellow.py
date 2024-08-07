from flask import Flask, render_template #importando flask para crear una aplicacion web

#crear una instancia de flask llamada app
app = Flask(__name__)

#crear rutas
@app.route('/') #ruta raiz
def hola_mundo():
    return "Hola Mundo"


@app.route('/hola/<nombre>') #para la ruta /hola/__ cualquier cosa despues, se pasara como variable
def hola(nombre):
    return f"¿Hola {nombre}, cómo estás?"
    #return f"<h1>¿Hola {nombre}, cómo estás?</h1>"

@app.route('/hello/<name>/<int:j>')
def hello(name, j):
    return render_template('hola.html', nombre=name, cantidad=j) #render_template permite mostrar los archivos html

if __name__=="__main__": # asegura que el archivo se está ejecutando y no desde otro modulo
    app.run(debug=True) # ejecuta la aplicacion
