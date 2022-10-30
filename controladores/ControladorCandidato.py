from modelos.Candidatos import Candidatos
from repositorios.CandidatoRepo import CandidatoRepo

class ControladorCandidato():
    """Clase que implementa el controlador para los endpoints relacionados con el candidato"""

    def __init__(self):
        print(" >Creando ControladorCandidato ")
        self.repositorio = CandidatoRepo()

    def index (self):
        print(" >Listar todos los candidatos")
        x = self.repositorio.findAll()
        return x
        
    def create (self,data):
         print(" >Crear un candidato")
         elCandidato = self.repositorio.save(Candidatos(data))
         return elCandidato

    def retrieve (self):
         print(" >Mostrando un Candidato con id", id)
         elCandidato = self.repositorio.findById(id)
         return elCandidato

    def update (self, id , data):
         print(" >Actualizando Candidato con id", id)
         candidatoActual = Candidatos(self.repositorioCandidato.findById(id))
         candidatoActual.resolucion   = data["N° REsolucion"]
         candidatoActual.cedula       = data["cedula"]
         candidatoActual.nombre       = data["nombre"]
         candidatoActual.apellido     = data["apellido"]
         return self.repositosioCandidato.save(candidatoActual)
         
    def delete (self):
        print(" >Eliminando Candidato con id", id)
        cuenta = self.repositorio.delete(id)
        return cuenta