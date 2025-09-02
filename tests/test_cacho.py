import pytest
from cacho import Cacho
from dado import Dado
from arbitro_ronda import ArbitroRonda

def test_cantidad_dados_inicial():
    cacho = Cacho()
    cant_inicial = cacho.getCantidadDados()
    assert cant_inicial == 5

def test_lanzar_dados():
    cacho = Cacho()
    cacho.lanzarDados()
    assert cacho.getResultados() is not None

def test_retirar_dados():
    cacho = Cacho()
    arb = ArbitroRonda()
    cacho.retirarDado(arb)
    assert cacho.getCantidadDados() == 4

def test_agregar_dados():
    cacho = Cacho()
    arb = ArbitroRonda()
    cacho.retirarDado(arb) # 4
    cacho.agregarDado(arb) # 5
    assert cacho.getCantidadDados() == 5

def test_retirar_dados_limite():
    cacho = Cacho()
    arb = ArbitroRonda()
    cacho.setCantidadDados(0)
    cacho.retirarDado(arb)
    # Cantidad no negativa
    assert cacho.getCantidadDados() == 0

def test_mostrar_ocultar():
    cacho = Cacho()
    assert cacho.visible is False
    cacho.toggleMostrar()
    assert cacho.visible is True

def test_buffer_dados():
    cacho = Cacho()
    arb = ArbitroRonda()
    # parte con 5 dados
    cacho.agregarDado(arb)
    assert cacho.getCantidadDados() == 5
    # si se le agrega un dado, sigue teniendo 5, pero la proxima vez que le quiten un dado no lo pierde
    cacho.agregarDado(arb)
    # deberia tener 2 dados en la ¨reserva¨ si le quitan
    assert cacho.getCantidadDados() == 5
    cacho.retirarDado(arb)
    assert cacho.getCantidadDados() == 5
    cacho.retirarDado(arb)
    assert cacho.getCantidadDados() == 5
    cacho.retirarDado(arb)
    assert cacho.getCantidadDados() == 4
