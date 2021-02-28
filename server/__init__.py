from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS


app = Flask(__name__, template_folder='../template')

# Cadena de conexion para mongodb atlas
app.config["MONGO_URI"] = 'mongodb+srv://infrabyte:%40Mendez99@cluster0.sl6e0.mongodb.net/calidad_aire?retryWrites=true&w=majority'

# Para que no ordene las respuestas json
app.config["JSON_SORT_KEYS"] = False

# Registrando la ruta /
@app.route("/")
def index():
    # Renderizando un templete html
    return render_template("index.html")

# Sirve para decirle que pueden consumir esta app desde otra app
CORS(app)

# instancia de mongo, para su uso posterior
mongo = PyMongo(app)

# Registrando rutas desde otros directorios de la ayuda del paquete flask_classful
# La importacion tiene que ser aqui por que si no, se vuelve una importacion circular
from server.controllers.DPM10 import DatosPM10View
DatosPM10View.register(app, route_prefix='/api')

from server.controllers.DPM25 import DatosPM25View
DatosPM25View.register(app, route_prefix='/api')
