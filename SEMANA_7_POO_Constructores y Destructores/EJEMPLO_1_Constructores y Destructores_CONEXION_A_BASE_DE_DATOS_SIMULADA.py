class ConexionBD:
    def __init__(self, nombre_bd):
        # Constructor: se conecta a la base de datos (simulado)
        self.nombre_bd = nombre_bd
        self.conectado = True
        print(f"Conectado a la base de datos '{self.nombre_bd}'.")

    def ejecutar_consulta(self, consulta):
        # Método para simular la ejecución de una consulta
        if self.conectado:
            print(f"Ejecutando consulta: {consulta}")
        else:
            print("No hay conexión activa.")

    def __del__(self):
        # Destructor: se desconecta de la base de datos
        if self.conectado:
            self.conectado = False
            print(f"Desconectado de la base de datos '{self.nombre_bd}' (desde destructor).")

db = ConexionBD("MiBaseDeDatos")
db.ejecutar_consulta("SELECT * FROM usuarios")
del db  # Forzamos la llamada al destructor
