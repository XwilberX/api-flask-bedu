# Este archivo sirve para el deploy(publicacion) de la api en G Cloud
from server import app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)