# este archivo solo sirvio en el desarrollo de la api
from server import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9090)