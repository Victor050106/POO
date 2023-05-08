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
    
    def cuerpo_celeste(self):
        """Muestra información sobre el cuerpo celeste."""
        print(f"{self.name} es un cuerpo celeste que tiene {self.age} de años.")
    
    def posicion(self):
        print(f"Es el {self.position} del sistema solar.")
    
    def gravedad(self):
        print(f"Cuenta con una gravedad de {self.gravity}")

    def volumen(self):
        print(f"Tiene un volumen de {self.volume} km3")
    
    def vida(self):
        print(f"En este planeta {self.life} se encuentra vida.")
    

    
Cuerpo1=Cuerpos_celestes ("El planeta Tierra", "4.54 billones", "tercer planeta", "9,2 m/s2"," 1.083.206.916.846", "si" )
Cuerpo2=Cuerpos_celestes ("Júpiter", "4,500 millones","quinto planeta","24,79 m/s2","1.431.281.810.739.360","no")

print("TIERRA")
print()

Cuerpo1.cuerpo_celeste()
print()

Cuerpo1.vida()
print()

Cuerpo1.posicion()
print()

Cuerpo1.gravedad()
print()

Cuerpo1.volumen()
print()

print("JÚPITER")
print()

Cuerpo2.cuerpo_celeste()
print()

Cuerpo2.vida()
print()

Cuerpo2.posicion()
print()

Cuerpo2.gravedad()
print()

Cuerpo2.volumen()
print()

#-------------------------Herencia--------------------------
class Cometa (Cuerpos_celestes):
    def __init__(self,name, age, position, gravity, volume, life,paso, observacion ):
        super().__init__(name, age, position, gravity, volume, life)
        self.paso=paso
        self.__observacion=observacion

    def information(self):
        print(f"{self.name} es uno de los cometas mas conocidos del mundo, pasa cada {self.paso}")
#-------------------------encapsulamiento----------------------
    def get_observacion(self):
        print(f"visto por primera vez en el año {self.__observacion}")

Cometa1 = Cometa ("El cometa halley", None,None,None,None,None,"75 años aproximadamente","239 a.C")

print("COMETA HALLEY")
print()

Cometa1.information()
Cometa1.get_observacion()