# TAREA_Clases, objetos, herencia, encapsulamiento y polimorfismo

# PROGRAMA_Sistema de Gestión de Empleados

# empleados.py

"""
Este programa demuestra los conceptos fundamentales de la Programación Orientada a Objetos (POO) en Python:
- Herencia: La clase base 'Empleado' es heredada por 'Gerente' y 'Desarrollador'.
- Encapsulación: El atributo 'salario' está encapsulado como privado.
- Polimorfismo: Cada clase sobrescribe el método 'calcular_bono' para un comportamiento personalizado.

El programa permite crear empleados de diferentes tipos y calcular su bono, así como mostrar su información.
"""

# Clase base que representa a un empleado genérico

class Empleado:
    def __init__(self, nombre, edad, salario):
        # Atributos comunes a todos los empleados
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario  # Atributo privado (encapsulado)

    # Método que puede ser sobrescrito por las clases hijas para calcular un bono

    def calcular_bono(self):
        return self.__salario * 0.05  # Bono base del 5%

    # Getter: permite acceder al salario de forma controlada

    def obtener_salario(self):
        return self.__salario

    # Setter: permite modificar el salario, validando que no sea negativo

    def modificar_salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            print("El salario no puede ser negativo.")

    # Método para mostrar información general del empleado

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.__salario}"

# Clase derivada que representa a un gerente

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad, salario)
        self.departamento = departamento  # Atributo adicional específico del gerente

    # Sobrescribimos el método para calcular un bono mayor para gerentes

    def calcular_bono(self):
        return self.obtener_salario() * 0.20  # Bono del 20%

    # Mostramos información extendida incluyendo el departamento

    def mostrar_info(self):
        return super().mostrar_info() + f", Departamento: {self.departamento}"

# Clase derivada que representa a un desarrollador

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje  # Atributo adicional específico del desarrollador

    # Sobrescribimos el método para calcular un bono distinto para desarrolladores

    def calcular_bono(self):
        return self.obtener_salario() * 0.10  # Bono del 10%

    # Mostramos información extendida incluyendo el lenguaje de programación

    def mostrar_info(self):
        return super().mostrar_info() + f", Lenguaje: {self.lenguaje}"


# Bloque principal del programa donde se crean objetos y se usan los métodos

if __name__ == "__main__":

    # Creamos un objeto de tipo Gerente

    gerente = Gerente("Laura", 40, 5000, "Marketing")

    # Creamos un objeto de tipo Desarrollador

    dev = Desarrollador("Carlos", 28, 3000, "Python")

    # Mostramos la información de cada empleado

    print(gerente.mostrar_info())
    print("Bono del gerente:", gerente.calcular_bono())

    print(dev.mostrar_info())
    print("Bono del desarrollador:", dev.calcular_bono())

    # Demostración de encapsulamiento: accedemos y modificamos el salario mediante métodos

    print("\nSalario original del desarrollador:", dev.obtener_salario())
    dev.modificar_salario(3500)  # Cambiamos el salario
    print("Nuevo salario del desarrollador:", dev.obtener_salario())

