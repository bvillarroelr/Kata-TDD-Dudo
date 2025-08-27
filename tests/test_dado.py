import pytest
from dado import Dado
nums = [1,2,3,4,5,6]

def test_numero_valido():
    d = Dado()
    assert d.lanzar() in nums

def test_pinta_valida():
    d = Dado()
    d.lanzar()
    
    if d.valor == 1:
        assert d.pinta == 'As'
    if d.valor == 2:
        assert d.pinta == 'Tonto'
    if d.valor == 3:
        assert d.pinta == 'Tren' 
    if d.valor == 4:
        assert d.pinta == 'Cuadra' 
    if d.valor == 5:
        assert d.pinta == 'Quina' 
    if d.valor == 6:
        assert d.pinta == 'Sexta'   

