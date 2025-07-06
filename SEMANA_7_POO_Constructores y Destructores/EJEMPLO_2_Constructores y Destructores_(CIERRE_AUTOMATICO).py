class Usuario:
    def __init__(self, nombre, edad):
        """
        Constructor de la clase Usuario.
        Este método se ejecuta automáticamente al crear una instancia de la clase.
        Aquí se inicializan los atributos 'nombre' y 'edad', y se simula la apertura de un recurso (archivo).
        """
        self.nombre = nombre
        self.edad = edad

        # Abrimos un archivo en modo de añadir (append) para registrar la creación del usuario
        self.archivo = open("log_usuarios.txt", "a")

        # Escribimos en el archivo que el usuario fue creado
        self.archivo.write(f"[CREADO] Usuario: {self.nombre}, Edad: {self.edad}\n")

        # Imprimimos un mensaje informativo en consola
        print(f"[INFO] Usuario {self.nombre} ha sido creado.")

    def mostrar_info(self):
        """
        Método para mostrar la información del usuario en consola.
        """
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    def __del__(self):
        """
        Destructor de la clase Usuario.
        Este método se ejecuta automáticamente cuando el objeto es destruido (es decir, cuando ya no hay referencias a él).
        Aquí cerramos el archivo y escribimos un mensaje indicando que el usuario fue destruido.
        """
        self.archivo.write(f"[DESTRUIDO] Usuario: {self.nombre}\n")
        self.archivo.close()  # Cerramos el archivo para liberar el recurso
        print(f"[INFO] Usuario {self.nombre} ha sido destruido y el archivo cerrado.")

# Definimos una función para crear un usuario temporal
def crear_usuario_temporal():
    """
    Esta función crea un objeto de tipo Usuario dentro de su propio alcance (scope).
    Cuando la función termina, el objeto ya no es referenciado por ninguna variable y se destruye automáticamente.
    """
    print("[INFO] Entrando en la función crear_usuario_temporal...")

    # Aquí se crea un objeto de la clase Usuario.
    # Esto llama automáticamente al método __init__.
    usuario = Usuario("Laura", 22)

    # Mostramos la información del usuario
    usuario.mostrar_info()

    print("[INFO] Saliendo de la función crear_usuario_temporal...")
    # Al finalizar esta función, la variable 'usuario' se elimina del alcance y se llama automáticamente al método __del__


# Punto de entrada del programa
if __name__ == "__main__":
    # Llamamos a la función que crea un usuario temporal
    crear_usuario_temporal()

    # Este mensaje se imprime después de que el objeto 'usuario' ha sido destruido
    print("[INFO] Fin del programa.")
