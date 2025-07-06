class SesionUsuario:
    def __init__(self, usuario):
        # Constructor: inicia la sesión del usuario
        self.usuario = usuario
        self.activa = True
        print(f"Sesión iniciada para el usuario '{self.usuario}'.")

    def cerrar_sesion(self):
        # Método para cerrar la sesión manualmente
        if self.activa:
            self.activa = False
            print(f"Sesión cerrada para el usuario '{self.usuario}'.")
        else:
            print("La sesión ya está cerrada.")

    def __del__(self):
        # Destructor: asegura que la sesión se cierre si no se hizo manualmente
        if self.activa:
            print(f"Cerrando sesión automáticamente para '{self.usuario}' (desde destructor).")
            self.activa = False

sesion = SesionUsuario("juan123")
# No cerramos la sesión manualmente para que el destructor la cierre automáticamente
del sesion
