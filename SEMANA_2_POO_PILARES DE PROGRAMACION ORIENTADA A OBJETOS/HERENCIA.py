class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_salario(self):
        print(f"Salario de {self.nombre}: {self.salario}")

class Gerente(Empleado):
    def mostrar_salario(self):
        print(f"Salario del gerente {self.nombre}: {self.salario * 1.2}")

# Uso
gerente = Gerente("Carlos", 3000)
gerente.mostrar_salario()
