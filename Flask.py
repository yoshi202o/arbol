#Importar el módulo Flask en el proyecto.
from flask import Flask 

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")

#‘/’ URL está vinculado con la función first_flask.
def first_flask():

    return "Este es mi primer programa en Flask"
####################################

#La función route() de la clase Flask.
@app.route("/cuboRubik")

#‘/’ URL está vinculado con la función first_flask.
def second_flask():

    return "Tengo 8 cobos Rubik"


#Ejecutamos la app en el servidor local.
app.run(debug=True)

# Crear entorno virtual 
#python -m venv
#Activar entorno virtual
#ever\Scripts\activate
# Instalar el módulo flask
# pip install flask