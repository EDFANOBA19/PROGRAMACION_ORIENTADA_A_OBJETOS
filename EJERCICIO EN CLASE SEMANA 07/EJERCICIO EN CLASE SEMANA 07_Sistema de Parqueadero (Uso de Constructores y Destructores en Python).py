class Vehiculo:
    def __init__(self, placa, tipo):
        # Constructor: se ejecuta automáticamente al crear un objeto Vehiculo
        # Inicializa los atributos placa y tipo con los valores recibidos
        self.placa = placa
        self.tipo = tipo

        # Muestra mensaje indicando que el vehículo ha ingresado al parqueadero
        print(f"Vehículo {self.tipo} con placa {self.placa} ha ingresado al parqueadero.")

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es destruido
        # Aquí simulamos la salida del vehículo del parqueadero
        print(f"Vehículo {self.tipo} con placa {self.placa} ha salido del parqueadero.")

def simular_parqueadero():
    # Creamos dos vehículos dentro de esta función para simular su ingreso
    v1 = Vehiculo("ABC123", "Carro")  # Vehículo 1 ingresa
    v2 = Vehiculo("XYZ789", "Moto")  # Vehículo 2 ingresa

    # Al terminar esta función, las variables v1 y v2 salen de alcance
    # y el recolector de basura de Python eliminará los objetos automáticamente,
    # lo que disparará el método __del__ para cada vehículo

if __name__ == "__main__":
    # Llamamos a la función que simula el parqueadero
    simular_parqueadero()

    # Al finalizar simular_parqueadero(), los objetos v1 y v2 se destruyen automáticamente
    # sin necesidad de llamar explícitamente a del, mostrando los mensajes de salida

