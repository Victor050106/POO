class Animal:
    def __init__(self, nombre, especie , genero, edad):
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad

    def eat(self):
        if self.nombre =="copito":
            print(f"{self.nombre} se toma su leche favorita")
        else:
            print(f"{self.nombre} se come sus huesos favoritos que le trajo su dueño")

    def sleep(self):
        if self.nombre =="copito":
            print(f"{self.nombre} duerme mucho porque ya tiene {self.edad} años")
        else:
            print(f"{self.nombre} es mas activa y juguetona ya que tiene {self.edad} años")

    def play(self):
        if self.nombre == "princesa":
            print(f"{self.nombre} juega mucho con su mejor amigo copito ")
        else:
            print(f"{self.nombre} le gusta jugar mucho con su mejor amiga princesa")

    def especies(self):
        if self.especie == "perro":
            print(f"{self.nombre} es más brusca ya que es un {self.especie}")
        else:
            print(f"{self.nombre} es más cariñoso ya que es un {self.especie}")
    
    

Animal1 = Animal("copito", "gato", "macho",  7 )
Animal2 = Animal("princesa", "perro", "hembra", 5 )


Animal1.eat()
print("")
Animal1.sleep()
print("")
Animal1.play()
print("")
Animal1.especies()
print("")
Animal2.eat()
print("")
Animal2.sleep()
print("")
Animal2.play()
print("")
Animal2.especies()
print("")

#------------ inheritence-------------------------------- 
class Panda(Animal):
    def __init__(self, nombre, especie, genero, edad, años_vida, origen):
        super().__init__(nombre, especie, genero, edad)
        self.años_vida = años_vida
        self.origen = origen

    def information(self):
        print(f"{self.nombre} es un {self.especie} el cual su tiempo de vida es de aproximadamente {self.años_vida}, según varias investigaciones se cree que su origen viene de {self.origen}")


Panda1 = Panda ("El Oso panda", " mamifero", "macho y hembra", 5,20, " La península iberica")

print("EL OSO PANDA")
print("")
Panda1.information()
