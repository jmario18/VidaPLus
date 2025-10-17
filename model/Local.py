

class Unidade:
    def __init__(self, nome, tipo, endereco, id=None):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.endereco = endereco


    def __str__(self):
        return f"{self.tipo} - {self.nome}"