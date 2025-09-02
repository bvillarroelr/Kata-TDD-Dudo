

class ValidadorApuesta:

    def __init__(self,pinta,cantidad):
        if pinta == 1:
            raise ValueError("No puedes empezar la apuesta con un as")
        self._actualizar_apuesta(pinta,cantidad)

    def apostar(self, pinta, cantidad):
        if self._es_cambio_a_as(pinta, cantidad):
            return self._actualizar_apuesta(pinta, cantidad)

        self._validar_cambio_apuesta(pinta, cantidad)
        self._validar_cambio_desde_as(pinta, cantidad)

        return self._actualizar_apuesta(pinta, cantidad)

    def _es_cambio_a_as(self, pinta, cantidad):
        if pinta == 1:
            if cantidad == int(self.cantidad_actual / 2) + 1:
                return True
            else:
                raise ValueError("Cantidad invalida para cambio a as")

    def _validar_cambio_apuesta(self, pinta, cantidad):
        if self.pinta_actual == pinta and self.cantidad_actual == cantidad:
            raise ValueError("La apuesta debe subir en algun aspecto")
        elif self.pinta_actual > pinta:
            raise ValueError("No se puede bajar la pinta apostada")
        elif self.cantidad_actual > cantidad:
            raise ValueError("No se puede bajar la cantidad apostada")

    def _validar_cambio_desde_as(self, pinta, cantidad):
        if self.pinta_actual == 1 and self.cantidad_actual * 2 + 1 != cantidad:
            raise ValueError("Cantidad invalida para cambio de as")

    def _validar_rango_pinta(self,pinta):
        if pinta < 1  or pinta > 6:
            raise ValueError("Pinta fuera de rango")

    def _validar_rango_cantidad(self,cantidad):
        if cantidad < 1:
            raise ValueError("Cantidad fuera de rango")

    def _actualizar_apuesta(self, pinta, cantidad):
        self._validar_rango_pinta(pinta)
        self._validar_rango_cantidad(cantidad)
        self.pinta_actual = pinta
        self.cantidad_actual = cantidad
        return True


