
from connection.connection import *

class Paciente:


    def __init__(self, nome, idade, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f"Paciente: {self.nome}"
    
    
