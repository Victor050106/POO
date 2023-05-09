class Libros:
    """clase que representa un libro del mundo"""
    def __init__(self, titulo, autor, editorial, year):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.year = year
        
    def informacion(self):
        """muestra toda la informacion que pedimos """
        return (f"Libro:{self.titulo}\nEscrito por:{self.autor}\nPublicado por:{self.editorial}\nAño de publicación:{self.year}\n")

libro1 = Libros("Cien años de soledad", "Gabriel García Márquez", "Sudamericana", 1967)
libro2 = Libros("El amor en los tiempos del cólera", "Gabriel García Márquez", "Sudamericana", 1985)


print(" CIEN AÑOS DE SOLEDAD\n")
print(libro1.informacion())

print("EL AMOR EN LOS TIEMPOS DEL COLERA\n")
print(libro2.informacion())
#--------------------Herencia-----------------
class Libro(Libros):
    """clase que representa un libro famoso del mundo"""   
    def __init__(self, titulo, autor, editorial, year, paginas):
        super().__init__(titulo, autor, editorial,year )
        self.paginas = paginas
        self._autor = autor

    def  informacion(self):
        print(f"El libro {self.titulo} cuenta con {self.paginas} paginas\nFue publicado por {self.editorial} en el año {self.year}")
#----------------encapsulamiento-------------------
    def get_autor(self):
        return (f"\n El autor del libro es:{self._autor}")
    def set_autor(self,autor):
        self._autor = autor
book1 = Libro ("Crónica de una muerte anunciada", "Gabriel García Márquez", "La Oveja Negra", 1981,156)


print("CRONICAS DE UNA MUERTE ANUNCIADA")
print(book1.informacion())
print(book1.get_autor())
book1.set_autor(" Pues Gabriel García Márquez, quien más")
print(book1.get_autor())