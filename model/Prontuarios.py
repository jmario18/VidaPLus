


class Prontuario:
    def __init__(self, paciente):
        self.paciente = paciente
        self.consultas = []

    def adicionar_consulta(self, consulta):
        self.consultas.append(consulta)

    def listar_consultas(self):
        return self.consultas