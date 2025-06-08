class Instrumento:
    def sonar(self):
        print("El instrumento está sonando")

class Guitarra(Instrumento):
    def sonar(self):
        print("La guitarra está tocando una melodía")

class Piano(Instrumento):
    def sonar(self):
        print("El piano está tocando una melodía")

def tocar(instrumento):
    instrumento.sonar()

# Uso
guitarra = Guitarra()
piano = Piano()

tocar(guitarra)
tocar(piano)

