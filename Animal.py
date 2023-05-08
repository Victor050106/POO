class Animal:
    def __init__(self, nombre, especie , genero, edad):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad

    def information(self):
        if self.nombre =="copito":
            print(f"\n Nombre:{self.nombre} \n Comida favorita: Pescado \n Especie:{self.especie} \n Genero:{self.genero} \n Edad:{self.edad}")
        else:
            print(f"\n Nombre:{self.nombre} \n Comida favorita: Carne \n Especie:{self.especie} \n Genero:{self.genero} \n Edad:{self.edad}") 

Animal1 = Animal("copito", "gato", "macho", " 7 años" )
Animal2 = Animal("princesa", "perro", "hembra"," 5 años" )

Animal1.information()
Animal2.information()


#------------ inheritence-------------------------------- 
class Panda(Animal):
    def __init__(self, nombre, especie, genero, edad, life , origen,colores):
        super().__init__(nombre, especie, genero, edad)
        self.life = life
        self.origen = origen
        self.__colores = colores

    def information(self):
        return f"\n Nombre:{self.nombre}. \n Especie:{self.especie}. \n Tiempo de vida:{self.life}. \n Origen:{self.origen}."
 #--------------------encapsulamiento----------------------
    def get_colores(self):
        """encapsulamiento de el color de piel de el oso"""
        return f"\n Color de piel:{self.__colores}"

Panda1 = Panda ("Oso panda", " mamifero", "macho y hembra", 5,"20 años", " La península iberica","blanco con lineas negras")

print("EL OSO PANDA")
print("")
Panda1.information()
print(Panda1.get_colores())