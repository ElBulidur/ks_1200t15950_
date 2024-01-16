# HERANÇA

class Curso:

    # Propriedade Descrição
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    # Propriedade Carga Horaria
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    
    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    # metodos
    def imprimir_curso(self):
        print(f"Curso: {self.descricao} com carga horário: {self.carga_horaria} horas")

    def mensagem_boas_vindas(self):
        print("Olá, seja bem vindo ao cuso.")


########### HERANÇA #######

# Classe de aulas EAD
class AulasEAD(Curso):
    @property
    def plataforma(self):
        return self.__plataforma
    
    @plataforma.setter
    def plataforma(self, plataforma):
        self.__plataforma = plataforma
    
    # Polimorfismo
    def mensagem_boas_vindas(self):
        print("Bem vindo ao curso de Python")
    

# Classe de aulas presencial
class AulasPresencial(Curso):
    @property
    def sala(self):
        return self.__sala
    
    @sala.setter
    def plataforma(self, sala):
        self.__sala = sala





python_ead = AulasEAD()

python_ead.plataforma = "ZOOM"
python_ead.descricao = "Python EAD"
python_ead.carga_horaria = 32

print(python_ead.plataforma)
python_ead.imprimir_curso()