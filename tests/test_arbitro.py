import pytest
from arbitro_ronda import ArbitroRonda
from cacho import Cacho

import pytest
from arbitro_ronda import ArbitroRonda
from cacho import Cacho

def test_duda_pierde_quien_dudo():
    arb = ArbitroRonda()
    apuesta = (2, 6)   # 2 sextos

    c1 = Cacho()
    c1.setResultados([6, 6, 3, 4, 1])      # 2 seis + 1 as
    c2 = Cacho()
    c2.setResultados([2, 3, 4, 5, 1])      # no cambia el mínimo requerido

    mesa = [c1, c2]
    resultado = arb.resolver_duda(apuesta, mesa, ases_comodin=True)
    assert resultado == "pierde_quien_dudo"

def test_duda_pierde_apostador():
    arb = ArbitroRonda()
    apuesta = (4, 5)   # 4 quinas

    c1 = Cacho()
    c1.setResultados([5, 2, 3, 1, 4])      # 1 cinco + 1 as = 2
    c2 = Cacho()
    c2.setResultados([2, 3, 4, 6, 2])      # 0 cinco, 0 as

    mesa = [c1, c2]
    resultado = arb.resolver_duda(apuesta, mesa, ases_comodin=True)
    assert resultado == "pierde_apostador"  # total = 2 < 4

def test_calzar_acierta():
    arb = ArbitroRonda()
    apuesta = (3, 2)  # 3 "tontos"

    c1 = Cacho()
    c1.setResultados([2, 2, 1, 4, 5])      # 2 doses + 1 as = 3
    c2 = Cacho()
    c2.setResultados([3, 4, 5, 6, 3])      # 0 doses, 0 ases

    mesa = [c1, c2]
    res = arb.resolver_calzar(apuesta, mesa, ases_comodin=True)
    assert res == "acierto"                # total exacto = 3

def test_calzar_falla():
    arb = ArbitroRonda()
    apuesta = (4, 6)  # 4 "sextos"

    c1 = Cacho()
    c1.setResultados([6, 6, 1, 2, 3])      # 2 seises + 1 as = 3
    c2 = Cacho()
    c2.setResultados([2, 3, 4, 5, 2])      # 0 seises, 0 ases

    mesa = [c1, c2]
    res = arb.resolver_calzar(apuesta, mesa, ases_comodin=True)
    assert res == "falla"                  # total = 3 ≠ 4


def test_condicion_calzar_mitad_dados():
    # solo si tiene 1 dado o mas de la mitad está en juego
    c1 = Cacho()
    c2 = Cacho()
    dados_en_juego = c1.getCantidadDados() + c2.getCantidadDados() # 2 cachos en juego, 5 dados por cacho = 10
    
    arb = ArbitroRonda()
    # suponemos que el jugador con el cacho 1 es quien quiere calzar
    assert arb.verificarCalzar(dados_en_juego, c1,5) is True

def test_condicion_calzar_1dado():
    c1 = Cacho()
    c2 = Cacho()
    arb = ArbitroRonda()
    for i in range(4):
        c1.retirarDado(arb)    # solo queda 1 dado

    dados_en_juego = c1.getCantidadDados() + c2.getCantidadDados()
    assert dados_en_juego == 6 
    assert arb.verificarCalzar(dados_en_juego, c1,2) is True # como c1 tiene un dado, si se puede calzar

def test_quitar_y_dar_dados():
    c1 = Cacho()
    c2 = Cacho()
    arb = ArbitroRonda()

    c1.retirarDado(arb)
    c2.retirarDado(arb)

    assert arb.getPoolDados() == 2

    c2.agregarDado(arb) # se debe quitar del pool

    assert arb.getPoolDados() == 1