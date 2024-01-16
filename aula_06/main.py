# HERANÇA

class Curso:
    def __init__(self, descricao, carga_horaria):
        self.descricao = descricao
        self.carga_horaria = carga_horaria

    def imprimir_curso(self):
        print(f"Curso: {self.descricao} com carga horário: {self.carga_horaria} horas")

    def mensagem_boas_vindas(self):
        print("Olá, seja bem vindo ao cuso.")


# programando_com_python = Curso("1200 - Programando com python", 32)

########### HERANÇA #######

# Classe de aulas EAD
class AulasEAD(Curso):
    def __init__(self, descricao, carga_horaria, plataforma):
        super().__init__(descricao, carga_horaria)
        self.plataforma = plataforma
    
    def mensagem_boas_vindas(self):
        print("Bem vindo ao curso de Python")
    


# Classe de aulas presencial
class AulasPresencial(Curso):
    def __init__(self, descricao, carga_horaria, sala):
        super().__init__(descricao, carga_horaria)
        self.sala = sala


python_ead = AulasEAD("Python EAD", 32, "ZOOM")
# python_presencial = AulasPresencial("Turma A")

# print(python_ead.plataforma)
# print(python_presencial.sala)

python_ead.descricao = "python"
python_ead.carga_horaria

python_ead.imprimir_curso()

# python_presencial.mensagem_boas_vindas()
# python_ead.mensagem_boas_vindas()