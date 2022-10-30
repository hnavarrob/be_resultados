
import json
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve

#Configuración del proyecto
app=Flask(__name__)
cors = CORS(app)

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

#Enlace al archivo config.json en donde está la dirección del puerto del servidor
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])