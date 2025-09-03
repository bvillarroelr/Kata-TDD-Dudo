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

def test_cambiar_apuesta_a_as():
    pinta = 2
    cantidad = 2
    validador = ValidadorApuesta(pinta,cantidad)
    cantidad = int(cantidad/2) + 1
    validador.apostar(1,cantidad)
    assert validador.pinta_actual == 1
    assert validador.cantidad_actual == cantidad

def test_cambiar_apuesta_a_as_invalido():
    validador = ValidadorApuesta(2,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(1,4)
    assert validador.pinta_actual == 2
    assert validador.cantidad_actual == 2
    assert "Cantidad invalida para cambio a as" in str(exc_info.value)

def test_cambiar_apuesta_de_as():
    cantidad = 2
    validador = ValidadorApuesta(2,cantidad)
    cantidad = int(cantidad/2) + 1
    validador.apostar(1,cantidad)
    cantidad = cantidad*2 +1
    validador.apostar(3,cantidad)
    assert validador.pinta_actual == 3
    assert validador.cantidad_actual == cantidad

def test_cambiar_apuesta_de_as_invalida():
    cantidad = 2
    validador = ValidadorApuesta(2, cantidad)
    cantidad = int(cantidad / 2) + 1
    validador.apostar(1, cantidad)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(3, 3)
    assert validador.pinta_actual == 1
    assert validador.cantidad_actual == cantidad
    assert "Cantidad invalida para cambio de as" in str(exc_info.value)

def test_empezar_apuesta_de_pinta_fuera_de_rango():
    pinta = 0
    cantidad = 2
    with pytest.raises(ValueError) as exc_info:
        validador = ValidadorApuesta(pinta,cantidad)
    assert "Pinta fuera de rango" in str(exc_info.value)

def test_empezar_apuesta_de_pinta_fuera_de_rango2():
    pinta = 7
    cantidad = 2
    with pytest.raises(ValueError) as exc_info:
        validador = ValidadorApuesta(pinta,cantidad)
    assert "Pinta fuera de rango" in str(exc_info.value)

def test_empezar_apuesta_con_cantidad_negativa():
    pinta = 2
    cantidad = -1
    with pytest.raises(ValueError) as exc_info:
        validador = ValidadorApuesta(pinta,cantidad)
    assert "Cantidad fuera de rango" in str(exc_info.value)

def test_apostar_con_pinta_fuera_de_rango():
    pinta = 0
    cantidad = 3
    validador = ValidadorApuesta(2,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(pinta,cantidad)
    assert validador.cantidad_actual == 2
    assert validador.pinta_actual == 2

def test_apostar_con_pinta_fuera_de_rango2():
    pinta = 7
    cantidad = 3
    validador = ValidadorApuesta(2,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(pinta,cantidad)
    assert "Pinta fuera de rango" in str(exc_info.value)
    assert validador.cantidad_actual == 2
    assert validador.pinta_actual == 2

def test_apostar_con_cantidad_fuera_de_rango():
    validador = ValidadorApuesta(2,2)
    with pytest.raises(ValueError) as exc_info:
        validador.apostar(2,-1)
    assert validador.cantidad_actual == 2
    assert validador.pinta_actual == 2

def test_apostar_especial_con_as():
    validador = ValidadorApuesta(1,2, especial = True)
    assert validador.pinta_actual == 1
    assert validador.cantidad_actual == 2