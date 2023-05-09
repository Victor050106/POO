class Cuerpos_celestes:
    """Clase que representa un cuerpo celeste del sistema solar."""
    def __init__(self, name, age, position, gravity, volume, life):
        """Inicializa un nuevo cuerpo celeste con los atributos dados."""
        self.name = name
        self.age = age
        self.position = position
        self.life = life
        self.gravity = gravity
        self.volume = volume
    
    def information(self):
        """Muestra información sobre el cuerpo celeste."""
        print(f"{self.name} es un cuerpo celeste que tiene {self.age} de años.\nEs el {self.position} del sistema solar.\nCuenta con una gravedad de {self.gravity}\nTiene un volumen de {self.volume} km3\nEn este planeta {self.life} se encuentra vida.\n")

Cuerpo1=Cuerpos_celestes ("Planeta Tierra","4.54 billones","tercer planeta","9,2 m/s2","1.083.206.916.846","si" )
Cuerpo2=Cuerpos_celestes ("Júpiter", "4,500 millones d","quinto planeta","24,79 m/s2","1.431.281.810.739.360","no")

print("TIERRA\n")
Cuerpo1.information()

print("JÚPITER\n")
Cuerpo2.information()

#-------------------------Herencia--------------------------
class Cometa (Cuerpos_celestes):
    """clase hijo que de la clase Cuerpos celestes"""
    def __init__(self,name, age, position, gravity, volume, life,paso, observacion ):
        super().__init__(name, age, position, gravity, volume, life)
        self.paso=paso
        self._observacion=observacion

    def information(self):
        print(f"{self.name} es uno de los cometas mas conocidos del mundo, pasa cada {self.paso}")
#-------------------------encapsulamiento----------------------
    def get_observacion(self):
        return f"visto por primera vez en el año {self._observacion}"
    def set_observacion(self,observacion):
        self._observacion = observacion
Cometa1 = Cometa ("El cometa halley", None,None,None,None,None,"75 años aproximadamente","239 a.C")

print("COMETA HALLEY\n")

Cometa1.information()
print(Cometa1.get_observacion())

Cometa1.set_observacion("239 a.C,este dato no se puede cambiar")
print(Cometa1.get_observacion())
