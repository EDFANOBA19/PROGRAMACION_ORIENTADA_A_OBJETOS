# Programa en Python para determinar el promedio semanal del clima
# Función que devuelve una lista fija con las temperaturas diarias
def obtener_temperaturas():
    # Lista con temperaturas simuladas para cada día de la semana (7 días)
    datos_temperatura = [22.5, 24.0, 23.8, 21.0, 25.2, 26.5, 24.7]
    return datos_temperatura

# Función que calcula el promedio de una lista de temperaturas semanal
def promedio_temperaturas(lista_temperaturas):
    total = 0
    # Se suma cada temperatura de la lista
    for temp in lista_temperaturas:
        total += temp
    # Se divide la suma total entre la cantidad de temperaturas para obtener el promedio
    return total / len(lista_temperaturas)

# Función principal que coordina la ejecución del programa
def ejecutar():
    print("== Cálculo del promedio semanal de temperaturas (Estilo Tradicional) ==")
    temperaturas = obtener_temperaturas()  # Obtenemos las temperaturas predefinidas
    print(f"Temperaturas registradas: {temperaturas}")  # Mostramos las temperaturas usadas
    promedio = promedio_temperaturas(temperaturas)  # Calculamos el promedio semanal
    print(f"Temperatura promedio semanal: {promedio:.2f} grados Celsius")  # Mostramos el resultado con dos decimales

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar()
