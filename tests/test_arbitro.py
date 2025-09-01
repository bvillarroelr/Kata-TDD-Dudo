import pytest
from arbitro_ronda import ArbitroRonda

def test_duda_pierde_quien_dudo():
    arb = ArbitroRonda()
    apuesta = (2, 6)   # 2 sextos
    mesa = [6, 6, 3, 4, 1]  # hay dos sextos + un As (comodín)
    resultado = arb.resolver_duda(apuesta, mesa, ases_comodin=True)
    assert resultado == "pierde_quien_dudo"

def test_duda_pierde_apostador():
    arb = ArbitroRonda()
    apuesta = (4, 5)   # 4 quinas
    mesa = [5, 2, 3, 1, 4]  # hay 1 quina + un As = 2 (< 4)
    resultado = arb.resolver_duda(apuesta, mesa, ases_comodin=True)
    assert resultado == "pierde_apostador"

def test_calzar_acierta():
    arb = ArbitroRonda()
    apuesta = (3, 2)  # 3 "tontos"
    mesa = [2, 2, 1, 4, 5]  # 2 tontos + 1 as (comodín) = 3
    res = arb.resolver_calzar(apuesta, mesa, ases_comodin=True)
    assert res == "acierto"

def test_calzar_falla():
    arb = ArbitroRonda()
    apuesta = (4, 6)  # 4 "sextos"
    mesa = [6, 6, 1, 2, 3]  # 2 sextos + 1 as = 3 (< 4)
    res = arb.resolver_calzar(apuesta, mesa, ases_comodin=True)
    assert res == "falla"