import random

CARAS = {
        1: "As",
        2: "Tonto",
        3: "Tren",
        4: "Cuadra",
        5: "Quina",
        6: "Sexta",
}

class Dado:
    def __init__(self):
        self.valor = None
        self.pinta = None

    def lanzar(self):
        self.valor = random.randint(1,6)
        self.pinta = CARAS.get(self.valor)
        print(f'{self.valor}: {self.pinta}')

        # para facilitar las operaciones a futuro solo retornamos el valor
        return self.valor

    def getValor(self):
        return self.valor
