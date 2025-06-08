class Electrodomestico:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"El electrodoméstico {self.marca} está encendido")

# Uso
microondas = Electrodomestico("LG")
microondas.encender()

