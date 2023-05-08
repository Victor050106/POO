class Materia:
    def __init__(self, nombre, profesor, horario, salon):
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
        self.salon = salon

    def informacion(self):
        print(f"La materia {self.nombre} es impartida por el profesor {self.profesor} en el horario {self.horario} en el salón {self.salon}")

    def profesores(self):
        print(f"El profesor de la materia es {self.profesor}")

    def horarios(self):
        print(f"La materia se imparte en el horario {self.horario}")

materia1 = Materia("Matemáticas", "Juan Pérez", "Lunes y Miércoles de 8:00 a 10:00", "A-101")
materia2 = Materia("Historia", "María González", "Martes y Jueves de 10:00 a 12:00", "B-202")

materia1.informacion()
print()
materia2.informacion()

class Calculo(Materia):
    def __init__(self, nombre, profesor, horario, salon,calificacion):
        super().__init__(nombre, profesor, horario, salon)
        self. __calificacion =calificacion
        
    
    def informacion(self):
        print(f"La materia {self.nombre} es impartida por el profesor {self.profesor} en el horario {self.horario} en el salón {self.salon}, con calificaciones promedio de {self.__calificacion}")

    def get_calificacion(self):
        return self.__calificacion

calculo1 = Calculo (" calculo"," diego parra", "viernes de 8:00 a 12:00","C -101","4.5 ")


print()
print(calculo1.get_calificacion())