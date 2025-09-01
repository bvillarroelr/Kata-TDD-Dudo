from sys import exception


class ValidadorApuesta:

    def __init__(self,pinta,cantidad):
        if pinta == 1:
            raise ValueError("No puedes empezar la apuesta con un as")
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad

    def apostar(self,pinta,cantidad):
        if self.pinta_actual > pinta:
            raise ValueError("No se puede bajar la pinta apostada")
        if self.cantidad_actual > cantidad:
            raise ValueError("No se puede bajar la cantidad apostada")
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad