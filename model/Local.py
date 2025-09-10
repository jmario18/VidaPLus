

class Estabelecimento:
    def __init__(self, nome, endereco, tipo):
        self.nome = nome
        self.endereco = endereco
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo} - {self.nome}"