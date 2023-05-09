class Materia:
    def __init__(self, nombre, profesor, horario, salon):
        self.nombre = nombre
        self.profesor = profesor
        self.horario = horario
        self.salon = salon

    def informacion(self):
        print(f"Materia:{self.nombre}\nImpartida por el profesor:{self.profesor}\nHorario:{self.horario}\nsalón:{self.salon}\n")

materia1 = Materia("Matemáticas", "Juan Pérez", "Lunes y Miércoles de 8:00 a 10:00", "A-101")
materia2 = Materia("Historia", "María González", "Martes y Jueves de 10:00 a 12:00", "B-202")

materia1.informacion()
materia2.informacion()

class Calculo(Materia):
    def __init__(self, nombre, profesor, horario, salon,calificacion):
        super().__init__(nombre, profesor, horario, salon)
        self._calificacion =calificacion
        
    
    def informacion(self):
        print(f"Materia:{self.nombre}\nImpartida por el profesor:{self.profesor}\nHorario:{self.horario}\nSalón:{self.salon}\n")

    def get_calificacion(self):
        return f"Calificación promedio:{self._calificacion}"
    
    def set_calificacion(self,calificacion):
        self._calificacion = calificacion

calculo1 = Calculo (" calculo"," diego parra", "viernes de 8:00 a 12:00","C -101","4.5 ")

calculo1.informacion()
print(calculo1.get_calificacion())
calculo1.set_calificacion("5")
print(calculo1.get_calificacion())
