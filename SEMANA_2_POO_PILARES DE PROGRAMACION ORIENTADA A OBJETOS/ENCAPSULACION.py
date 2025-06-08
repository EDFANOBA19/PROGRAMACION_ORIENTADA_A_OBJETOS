class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.__autor = autor  # atributo privado

    def mostrar_autor(self):
        print(f"Autor: {self.__autor}")

# Uso
libro = Libro("1984", "George Orwell")
libro.mostrar_autor()
# No se puede acceder directamente a libro.__autor
