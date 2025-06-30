# Programa python: calculadora de Areas y gestion de usuarios

# decripcion del programa
"""
Programa que calcula áreas de figuras geométricas y gestiona información de usuarios.
Incluye: rectángulo, triángulo, círculo y almacenamiento de datos de usuario.
Tipos de datos utilizados: integer, float, string, boolean.
Convención snake_case para identificadores.
"""

# Función para calcular área de rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    Args:
        base (float): Medida de la base
        altura (float): Medida de la altura
    Returns:
        float: Área calculada
    """
    return base * altura


# Función para calcular área de triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    return (base * altura) / 2


# Función para calcular área de círculo (usa tipo float y constante)
def calcular_area_circulo(radio: float) -> float:
    PI = 3.1416  # Constante en mayúsculas (convención)
    return PI * (radio ** 2)


# Función para validar usuario (usa boolean y string)
def validar_usuario(usuario: str, edad: int) -> bool:
    """
    Valida si un usuario es mayor de edad.
    Args:
        usuario (str): Nombre del usuario
        edad (int): Edad del usuario
    Returns:
        bool: True si es mayor de edad
    """
    return edad >= 18


# ---------- Ejecución principal ----------
if __name__ == "__main__":
    # Datos de usuario (string, integer, boolean)
    nombre_usuario = "maría_garcía"
    edad_usuario = 25
    es_mayor = validar_usuario(nombre_usuario, edad_usuario)

    # Cálculo de áreas (float)
    area_rect = calcular_area_rectangulo(5.5, 3.2)
    area_tri = calcular_area_triangulo(4.0, 7.5)
    area_circ = calcular_area_circulo(3.0)

    # Resultados
    print(f"Usuario válido: {es_mayor}")
    print(f"Área rectángulo: {area_rect:.2f}")
    print(f"Área triángulo: {area_tri:.2f}")
    print(f"Área círculo: {area_circ:.2f}")

