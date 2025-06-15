# programa en Python para determinar el promedio semanal del clima_POO
# Clase que representa una semana con datos climáticos
class SemanaClimatica:
    def __init__(self, temperaturas=None):
        # Inicializa la lista privada de temperaturas; si no se pasa ninguna, queda vacía
        self.__datos = temperaturas if temperaturas is not None else []

    # Método para calcular la media de las temperaturas almacenadas
    def calcular_media(self):
        if not self.__datos:
            return 0  # Retorna 0 si no hay datos para evitar división por cero
        suma_total = 0
        # Suma cada temperatura almacenada
        for valor in self.__datos:
            suma_total += valor
        # Retorna el promedio
        return suma_total / len(self.__datos)

    # Método para mostrar el promedio calculado
    def mostrar_resultado(self):
        media = self.calcular_media()
        print(f"Temperatura media semanal: {media:.2f}°C")

# Clase derivada que añade avisos según el valor promedio
class SemanaClimaticaConAviso(SemanaClimatica):
    # Sobrescribe el método mostrar_resultado para incluir mensajes de alerta
    def mostrar_resultado(self):
        media = self.calcular_media()
        print(f"Temperatura media semanal: {media:.2f}°C")
        # Condiciones para mostrar avisos según el promedio
        if media > 30:
            print("Aviso: Temperatura media alta esta semana.")
        elif media < 10:
            print("Aviso: Temperatura media baja esta semana.")
        else:
            print("Temperatura media dentro del rango esperado.")

# Función principal que ejecuta el programa
def iniciar():
    print("== Promedio semanal del clima (POO reformulado) ==")
    temperaturas = [22.5, 24.0, 23.8, 21.0, 25.2, 26.5, 24.7]  # Lista de temperaturas predefinidas
    print(f"Temperaturas usadas: {temperaturas}")  # Mostrar las temperaturas usadas
    semana = SemanaClimaticaConAviso(temperaturas)  # Crear instancia con los datos
    semana.mostrar_resultado()  # Mostrar el promedio y posibles avisos

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar()
