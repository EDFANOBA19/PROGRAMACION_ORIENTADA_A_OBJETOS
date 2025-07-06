import time

class Temporizador:
    def __init__(self):
        # Constructor: inicia el temporizador
        self.inicio = time.time()
        print("Temporizador iniciado.")

    def tiempo_transcurrido(self):
        # Devuelve el tiempo transcurrido desde la creación del objeto
        return time.time() - self.inicio

    def __del__(self):
        # Destructor: muestra el tiempo total cuando el objeto es destruido
        tiempo = time.time() - self.inicio
        print(f"Temporizador detenido. Tiempo total: {tiempo:.2f} segundos.")

t = Temporizador()
time.sleep(2)  # Simula espera de 2 segundos
del t  # Destructor muestra el tiempo total
