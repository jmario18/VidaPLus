

class Receita:
    def __init__(self, idConsulta, descricao, data_emissao, idPaciente):
        self.idConsulta = idConsulta
        self.descricao = descricao
        self.data_emissao = data_emissao
        self.idPaciente = idPaciente

    def __str__(self):
        return f"Receita(id_consulta={self.idConsulta}, descricao={self.descricao}, data_emissao={self.data_emissao})"