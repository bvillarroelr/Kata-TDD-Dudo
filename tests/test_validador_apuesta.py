import pytest
from validador_apuesta import *


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

def test_cambio_de_cantidad_valido():
    validador = ValidadorApuesta(2,2)
    validador.apostar(2,3)
    assert validador.cantidad_actual == 3
    assert validador.pinta_actual == 2

def test_cambio_de_pinta_invalido():
    validador = ValidadorApuesta(3,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(2,2)
    assert "No se puede bajar la pinta apostada" in str(exc_info.value)
    assert validador.pinta_actual == 3
    assert validador.cantidad_actual == 2

def test_cambio_de_cantidad_invalido():
    validador = ValidadorApuesta(2,3)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(2,2)
    assert "No se puede bajar la cantidad apostada" in str(exc_info.value)
    assert validador.cantidad_actual == 3
    assert validador.pinta_actual == 2

def test_cambio_de_apuesta_igual():
    validador = ValidadorApuesta(2,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(2,2)
    assert "La apuesta debe subir en algun aspecto" in str(exc_info.value)