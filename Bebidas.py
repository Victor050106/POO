class Bebidas:
    def __init__(self, nombre, fabricantes, tamaño, mercado):
        self.nombre = nombre
        self.fabricantes = fabricantes
        self.tamaño = tamaño
        self.mercado = mercado

    def information(self):
        bebidas = ["El aguardiente antioqueño", "Cerveza Aguila"]
        if self.nombre in bebidas:
            print(f"{self.nombre} es una de las bebidas alcoholicas mas conocidas y vendidas de Colombia, Es fabricada por {self.fabricantes},Podemos encontrar esta bebida en cantidades desde {self.tamaño},Salió al mercado en {self.mercado}")
        else:
            print(f"{self.nombre} es una de las bebidas más reconocidas y a su vez una de las más vendidas del mundo, Es fabricada por {self.fabricantes},Podemos encontrar esta bebida en cantidades desde {self.tamaño},Salió al mercado en {self.mercado}")

    def creator(self):
        print(f"Es fabricada por {self.fabricantes}")

    def cantidad(self):
        print(f"Podemos encontrar esta bebida en cantidades desde {self.tamaño}")

    def salida(self):
        print(f"Salió al mercado en {self.mercado}")

bebidas1=Bebidas("El aguardiente antioqueño","Fábrica de Licores de Antioquia ", "250 ml hasta 2000 ml", "1970")
bebidas2 = Bebidas("Coca Cola", "The Coca-Cola Company","235ml hasta 3Lt", "1886" )
bebidas3 =Bebidas("Cerveza Aguila", "Bavaria S.A.", "330 ml hasta 1 L", "1913")


print("AGUARDIENTE ANTIOQUEÑO")
print("")
bebidas1.information()

print("")

print ("COCA COLA")
print("")
bebidas2.information()

print("")

print("CERVEZA AGUILA")
print("")
bebidas3.information()

#------------ inheritence-------------------------------- 

class Manzana(Bebidas):
    def __init__(self, nombre, fabricantes, tamaño, mercado, envase):
        super().__init__(nombre, fabricantes, tamaño, mercado)
        self.envase = envase

    def information(self):
         print(f"{self.nombre} es una de las bebidas más conocidas y vendidas de Colombia, Es fabricada por {self.fabricantes},Podemos encontrar esta bebida en cantidades desde {self.tamaño},Salió al mercado en {self.mercado}, y se encuentra en un envase de {self.envase}")
         
   

Manzana1 = Manzana ("La manzana postobon", "Postobón","269 ml a 3.125 lt",1954," vidrio y plastico ")
Manzana1.information()
