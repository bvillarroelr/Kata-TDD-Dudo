import pytest
from validador_apuesta import *

from src.validador_apuesta import ValidadorApuesta


def test_empezar_apuesta():
    pinta = 2
    cantidad = 3
    validador = ValidadorApuesta(pinta,cantidad)
    assert validador is not None

def test_empezar_apuesta_con_as():
    pinta = 1
    cantidad = 2
    with pytest.raises(ValueError) as exc_info:
        validador = ValidadorApuesta(pinta,cantidad)
    assert "No puedes empezar la apuesta con un as" in str(exc_info.value)

def test_cambio_de_pinta_valido():
    validador = ValidadorApuesta(2,2)
    validador.apostar(3,2)
    assert validador.pinta_actual == 3
    assert validador.cantidad_actual == 2
