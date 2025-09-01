from sys import exception


class ValidadorApuesta:

    def __init__(self,pinta,cantidad):
        if pinta == 1:
            raise ValueError("No puedes empezar la apuesta con un as")
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad

    def apostar(self,pinta,cantidad):
        if pinta == 1:
            if cantidad == int(self.cantidad_actual/2) + 1:
                self.pinta_actual = pinta
                self.cantidad_actual = cantidad
                return True
            else:
                raise ValueError("Cantidad invalida para cambio a as")
        if self.pinta_actual > pinta:
            raise ValueError("No se puede bajar la pinta apostada")
        if self.cantidad_actual > cantidad:
            raise ValueError("No se puede bajar la cantidad apostada")
        if self.pinta_actual == pinta and self.cantidad_actual == cantidad:
            raise ValueError("La apuesta debe subir en algun aspecto")
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad
        return True
