class Persona:
    def __init__(self, name, age, profesion):
        self.name = name
        self.age = age
        self.profesion = profesion

    def saludar(self):
        print(f"Hola, mi nombre es {self.name} tengo {self.age} años y soy {self.profesion}.")

    def nombre(self):
        print(f"me llamo {self.name}")

    def edad(self):
        print(f" mi edad es {self.age} años")

    def trabajo(self):
        print(f"Me desempeño como {self.profesion}")
    
    

persona1 = Persona("Juan",  25, "ingeniero")
persona2 = Persona("Maria", 30, "abogada")

persona1.saludar()
print("")
persona2.saludar()

class Estudiante(Persona):
    def __init__(self, name, age, profesion, semestre):
        super().__init__(name, age, profesion)
        self.semestre = semestre
    
    def saludar_estudiante(self):
        print(f"Hola, mi nombre es {self.name} tengo {self.age} años y voy en el {self.semestre} de mi carrera universitaria ya que quiero ser el mejor {self.profesion}")
    
    def semester(self):
        print(f"voy en el {self.semestre} de mi carrera universitaria ya que quiero ser el mejor {self.profesion}")
       
estudiante1 = Estudiante ("Javier", 20, "programador", 6)
estudiante2 = Estudiante ("Hernesto",19,"diseñador grafico",5)
print("")
estudiante1.saludar_estudiante()
print("")
estudiante2.saludar_estudiante()
