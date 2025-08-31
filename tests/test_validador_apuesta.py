import pytest

def test_empezar_apuesta():
    pinta = 2
    cantidad = 3
    validador = ValidadorApuesta(2,3)
    assert validador is not None