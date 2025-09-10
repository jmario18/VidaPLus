


class Profissional:


    def __init__(self, nome, cargo, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cargo = cargo

    def __str__(self):
        return f"{self.cargo}: {self.nome}"