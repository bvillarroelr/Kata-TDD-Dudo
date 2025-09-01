import pytest
from arbitro_ronda import ArbitroRonda
from cacho import Cacho

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

def test_condicion_calzar_mitad_dados():
    # solo si tiene 1 dado o mas de la mitad está en juego
    c1 = Cacho()
    c2 = Cacho()
    dados_en_juego = c1.getCantidadDados() + c2.getCantidadDados() # 2 cachos en juego, 5 dados por cacho = 10
    
    arb = ArbitroRonda()
    c1.setApuesta((5,3))
    # suponemos que el jugador con el cacho 1 es quien quiere calzar
    assert arb.verificarCalzar(dados_en_juego, c1) is True

def test_condicion_calzar_1dado():
    c1 = Cacho()
    c2 = Cacho()
    arb = ArbitroRonda()
    for i in range(4):
        c1.retirarDado(arb)    # solo queda 1 dado

    c1.setApuesta((5,3))
    dados_en_juego = c1.getCantidadDados() + c2.getCantidadDados()
    assert dados_en_juego == 6 
    assert arb.verificarCalzar(dados_en_juego, c1) is True # como c1 tiene un dado, si se puede calzar

def test_quitar_y_dar_dados():
    c1 = Cacho()
    c2 = Cacho()
    arb = ArbitroRonda()

    c1.retirarDado(arb)
    c2.retirarDado(arb)

    assert arb.getPoolDados() == 2

    c2.agregarDado(arb) # se debe quitar del pool

    assert arb.getPoolDados() == 1