from http import HTTPStatus # para generar codigos de estado de respuestas
from flask_classful import FlaskView # libreria que extiende a flask 
from flask import jsonify, request, Response # metodos utilez para obtener datos de lo que nos envian(request) 
                                             # y/o responder (Response)
from bson import json_util # Metodo util para pasar la query de mongo a json


from server import mongo

# Heredar FlaskView a una clase, significa que podemos hacer uso de sus metodos y propiedades
class DatosPM10View(FlaskView):
    route_base = '/dpmdiez'

    # Se utiliza para poder ponerles nombres perzonalizadas a las funciones y cada nombre
    # de funcion se convertira en una ruta que tendra los metodos declarados aqui
    default_methods = ['GET']

    def primer_año_all(self):
        estaciones = mongo.db.datospmdiez_uno.find()
        response = json_util.dumps(estaciones)
        return Response(response, mimetype="application/json"), HTTPStatus.OK

    def primer_año_byes(self):
        body = request.get_json()
        estacion = body['estacion']

        estaciones = mongo.db.datospmdiez_uno.find({}, {'_id' : 0, estacion : 1, 
                                                        'FECHA' : 1, 'HORA' : 1})
        response = json_util.dumps(estaciones)

        return Response(response, mimetype="application/json"), HTTPStatus.OK

    def segundo_año_all(self):
        estaciones = mongo.db.datospmdiez_dos.find()
        response = json_util.dumps(estaciones)
        return Response(response, mimetype="application/json"), HTTPStatus.OK

    
    def segundo_año_byes(self):
        body = request.get_json()
        estacion = body['estacion']

        estaciones = mongo.db.datospmdiez_dos.find({}, {'_id' : 0, estacion : 1, 
                                                        'FECHA' : 1, 'HORA' : 1})
        response = json_util.dumps(estaciones)

        return Response(response, mimetype="application/json"), HTTPStatus.OK