class Bebidas:
    def __init__(self, nombre, fabricantes, size, mercado):
        self.nombre = nombre
        self.fabricantes = fabricantes
        self.size = size
        self.mercado = mercado

    def information(self):
        """muestra la información que le dimos de la bebida"""
        bebidas = ["El aguardiente antioqueño", "Cerveza Aguila"]
        if self.nombre in bebidas:
            print(f"{self.nombre} es una de las bebidas alcoholicas mas conocidas y vendidas de Colombia \nEs fabricada por {self.fabricantes}\nPodemos encontrar esta bebida en cantidades desde {self.size}\nSalió al mercado en {self.mercado}\n")
        else:
            print(f"{self.nombre} es una de las bebidas más reconocidas y a su vez una de las más vendidas del mundo\nEs fabricada por {self.fabricantes}\nPodemos encontrar esta bebida en cantidades desde {self.size}\nSalió al mercado en {self.mercado}\n")

bebidas1 = Bebidas("El aguardiente antioqueño","Fábrica de Licores de Antioquia ","250 ml hasta 2000 ml","1970")
bebidas2 = Bebidas("Coca Cola", "The Coca-Cola Company","235ml hasta 3Lt", "1886" )
bebidas3 = Bebidas("Cerveza Aguila", "Bavaria S.A.", "330 ml hasta 1 L", "1913")


print("AGUARDIENTE ANTIOQUEÑO \n")
bebidas1.information()

print ("COCA COLA\n")
bebidas2.information()

print("CERVEZA AGUILA\n")
bebidas3.information()

#------------ inheritence-------------------------------- 

class Manzana(Bebidas):
    """Creamos un hijo de la clase Bebidas"""
    def __init__(self, nombre, fabricantes, size, mercado, envase):
        super().__init__(nombre, fabricantes, size, mercado)
        self._envase = envase

    def information(self):
        return(f"{self.nombre} es una de las bebidas más conocidas y vendidas de Colombia\nEs fabricada por {self.fabricantes}\nPodemos encontrar esta bebida en cantidades desde {self.size}\nSalió al mercado en {self.mercado}\nSe encuentra en un envase de {self._envase}")
    #--------------------encapsulamiento-------------------
    def get_envase(self):
        """se utiliza get para el encapsulamiento de un dato"""
        return f"Se puede encontrar en envase de {self._envase}"

    def set_envase(self,envase):
        """se utiliza set para cambiar el dato encapsulado"""
        self._envase = envase
    


Manzana1 = Manzana ("La manzana postobon", "Postobón","269 ml a 3.125 lt",1954," vidrio ")
print("MANZANA POSTOBON\n")
print(Manzana1.information())
Manzana1.set_envase("plastico")
print(Manzana1.get_envase())
