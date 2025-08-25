import pytest
nums = [1,2,3,4,5,6]

nums_pintas = {
    1:'As',
    2:'Tonto',
    3:'Tren',
    4:'Cuadra',
    5:'Quina',
    6:'Sexto',
}

def test_numero_valido():
    assert Dado.lanzar() in nums

def test_pinta_valida():
    k = list(range(1,7))
    
    if k[0] == 1:
        assert Dado.pinta == 'As'
    if k[1] == 2:
        assert Dado.pinta == 'Tonto'
    if k[2] == 3:
        assert Dado.pinta == 'Tren' 
    if k[3] == 4:
        assert Dado.pinta == 'Cuadra' 
    if k[4] == 5:
        assert Dado.pinta == 'Quina' 
    if k[5] == 6:
        assert Dado.pinta == 'Sexta'   

