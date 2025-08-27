import pytest

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
    cacho.retirarDado()
    assert cacho.getCantidadDado() == 4

def test_agregar_dados():
    cacho = Cacho()
    cacho.agregarDado()
    assert cacho.getCantidadDados() == 6

def test_retirar_dados_limite():
    cacho = Cacho()
    cacho.setCantidadDados(0)
    cacho.retirarDado()
    # Cantidad no negativa
    assert cacho.getCantidadDados() == 0