"""Modulo """
class Libros:
    """clase que representa un libro del mundo"""
    def __init__(self, titulo, autor, editorial, year):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.year = year
        
    def informacion(self):
        """muestra toda la informacion que pedimos """
        print(f"El libro {self.titulo} fue escrito por {self.autor} y publicado por {self.editorial} en el año {self.year}")
    
    def creator(self):
        """muestra a el autor"""
        print(f"El autor del libro es {self.autor}")

    def editoria(self):
        """muestra a la editorial"""
        print(f"La editorial del libro es {self.editorial}")

    def tiempo(self):
        """muestra el año en que se publico"""
        print(f"El libro fue publicado en el año {self.year}")

libro1 = Libros("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 1967)
libro2 = Libros("El amor en los tiempos del cólera", "Gabriel García Márquez", "Sudamericana", 1985)


print(" CIEN AÑOS DE SOLEDAD")
print("")
libro1.informacion()
print("")


print("EL AMOR EN LOS TIEMPOS DEL COLERA")
print("")
libro2.informacion()
print("")
class Libro(Libros):
    """clase que representa un libro famoso del mundo"""   
    def __init__(self, titulo, autor, editorial, year, paginas):
        super().__init__(titulo, autor, editorial,year )
        self.paginas = paginas

    def  informacion(self):
        print(f"El libro {self.titulo} fue escrito por {self.autor}, cuenta con {self.paginas} paginas, fue publicado por {self.editorial} en el año {self.year}")
book1 = Libro ("Crónica de una muerte anunciada", "Gabriel García Márquez", "La Oveja Negra", 1981,156)


print("CRONICAS DE UNA MUERTE ANUNCIADA")
print("")
book1.informacion()