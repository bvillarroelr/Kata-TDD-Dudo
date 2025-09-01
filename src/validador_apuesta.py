

class ValidadorApuesta:

    def __init__(self,pinta,cantidad):
        if pinta == 1:
            raise ValueError("No puedes empezar la apuesta con un as")
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad
