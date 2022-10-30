
from asyncio.windows_events import NULL
import json
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

from controladores.ControladorCandidato import ControladorCandidato

#Configuración del proyecto
app=Flask(__name__)
cors = CORS(app)

ControladorCandidato = None

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

# #Exponer un end-point de prueba
@app.route("/",methods=['GET'])
def test():
    json= {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/Candidato",methods=['GET'])
def index():
    pass
@app.route("/Candidato",methods=['GET'])
def retrieve():
    pass
@app.route("/Candidato",methods=['POST'])
def create():
    pass
@app.route("/Candidato/<string:id>",methods=['PUT'])
def update():
    pass
@app.route("/Candidato/<string:id>",methods=['DELETE'])
def delete():
    pass

#Enlace al archivo config.json en donde está la dirección del puerto del servidor
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

    if dataConfig("test") == "true" :
        print("Test ing D8 connection...")
        from repositorios.InterfaceRepo import InterfaceRepo
        repo = InterfaceRepo()

    else:
        ControladorCandidato = ControladorCandidato()
        serve(app,host=dataConfig["url-backend"],port=dataConfig ["port "]) #Production-grade WSGI serv
        #https://docs.pylonsproject.org/projects/waitress/en/stable/api.html
        #https://docs.pylonsproject.org/projects/waitress/en/stable/arguments.html#arguments