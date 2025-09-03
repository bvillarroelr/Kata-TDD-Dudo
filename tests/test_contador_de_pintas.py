import pytest

from contador_de_pintas import ContadorDePintas

def test_contador(mocker):
    cacho1 = mocker.Mock()
    cacho1.getResultados.return_value = [1, 2, 2, 3, 6]

    cacho2 = mocker.Mock()
    cacho2.getResultados.return_value = [1, 2, 3, 4, 5]

    contador = ContadorDePintas([cacho1, cacho2])

    resultado = contador.contar()
    trenes = contador.contar(pinta=3)
    assert resultado == [2, 5, 4, 3, 3, 3]
    assert trenes == 4

    cacho1.getResultados.assert_called_once()
    cacho2.getResultados.assert_called_once()

def test_contador_ronda_de_un_dado(mocker):
    cacho1 = mocker.Mock()
    cacho1.getResultados.return_value = [1, 2, 2, 3, 6]

    cacho2 = mocker.Mock()
    cacho2.getResultados.return_value = [1, 2, 3, 4, 5]

    contador = ContadorDePintas([cacho1, cacho2])

    resultado = contador.contar(un_dado=True)
    trenes = contador.contar(pinta=3, un_dado=True)
    assert resultado == [2, 3, 2, 1, 1, 1]
    assert trenes == 2

    cacho1.getResultados.assert_called_once()
    cacho2.getResultados.assert_called_once()

def test_pinta_invalida(mocker):
    cacho1 = mocker.Mock()
    cacho1.getResultados.return_value = [1, 2, 2, 3, 6]

    cacho2 = mocker.Mock()
    cacho2.getResultados.return_value = [1, 2, 3, 4, 5]

    contador = ContadorDePintas([cacho1, cacho2])

    with pytest.raises(ValueError) as exc_info:
        contador.contar(pinta=7)
    assert "Pinta fuera de rango" in str(exc_info.value)
    cacho1.getResultados.assert_called_once()
    cacho2.getResultados.assert_called_once()