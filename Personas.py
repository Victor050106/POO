class Persona:
    def __init__(self, name, age, profesion):
        self.name = name
        self.age = age
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, mi nombre es {self.name}\ntengo {self.age} años\nsoy {self.profesion}.\n")

persona1 = Persona("Juan",  25, "ingeniero")
persona2 = Persona("Maria", 30, "abogada")

persona1.saludar()

persona2.saludar()
#---------------------herencia-------------
class Estudiante(Persona):
    def __init__(self, name, age, profesion, semestre):
        super().__init__(name, age, profesion)
        self._semestre = semestre
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.name}\ntengo {self.age} años y voy en el universidad\nquiero ser el mejor {self.profesion}\n")
#----------------------encapsulamiento---------------------
    def get_semestre(self):
        print(f"voy en el {self._semestre} de mi carrera universitaria\n")
    
    def set_semestre(self,semestre):
        self._semestre = semestre
       
estudiante1 = Estudiante ("Javier", 20, "programador", 6)
estudiante2 = Estudiante ("Hernesto",19,"diseñador grafico",5)

estudiante1.saludar()
estudiante1.set_semestre(8)
estudiante1.get_semestre()

estudiante2.saludar()
estudiante2.set_semestre(7)
estudiante2.get_semestre()
