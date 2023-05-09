class Animal:
    def __init__(self, nombre, especie , genero, edad, favorite_food):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.favorite_food = favorite_food
        
    def information(self):
        """muestra información de el animal 1 y 2 """
        print(f"\n Nombre:{self.nombre} \n Comida favorita:{self.favorite_food} \n Especie:{self.especie} \n Genero:{self.genero} \n Edad:{self.edad}\n")


Animal1 = Animal("copito", "gato", "macho", " 7 años", "Pescado" )
Animal2 = Animal("princesa", "perro", "hembra"," 5 años","Carne" )

Animal1.information()
Animal2.information()
#------------ inheritence-------------------------------- 
class Panda(Animal):
    def __init__(self, nombre,nombre_cientifico, especie, genero, edad,favorite_food, life, origen, colores):
        super().__init__(nombre, especie, genero, edad, favorite_food )
        self.nombre_cientifico = nombre_cientifico
        self.life = life
        self.origen = origen
        self._colores = colores
        
    def information(self):
        """muestra información basica de el animal"""
        return f"\n Nombre cientifico:{self.nombre_cientifico} \n Nombre:{self.nombre}\n Especie:{self.especie}\n Lugar de origen:{self.origen}\n Comida favorita:{self.favorite_food} \n Viven aproximadamente:{self.life} \n Genero:{self.genero} "
 #------------------encapsulamiento------------------
    def get_colores(self):
        """Returns the color of the animal's fur"""
        return f"\n Color de piel:{self._colores}"
    def set_colores(self, colores):
        """cambia le color de el animal"""
        self._colores = colores
    
Panda1 = Panda ("Oso panda", "Ailuropoda melanoleuca"," mamifero", "macho y hembra", None,"Bambú","20 años"," La península iberica","blanco con lineas negras")

print("EL OSO PANDA")
print(Panda1.information())
print(Panda1.get_colores())
Panda1.set_colores("café")
print(Panda1.get_colores())