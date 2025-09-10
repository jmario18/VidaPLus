class Consulta:
    def __init__(self, id_consulta, paciente, medico, data_hora, motivo):
        self.id_consulta = id_consulta
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.motivo = motivo

    def __repr__(self):
        return (f"Consulta(id_consulta={self.id_consulta}, paciente={self.paciente}, "
                f"medico={self.medico}, data_hora={self.data_hora}, motivo={self.motivo})")