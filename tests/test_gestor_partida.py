import pytest
from gestor_partida import *


def test_base_partida():
    jugadores = ["Andrés", "Benjamín","Alex"]
    gestor = GestorPartida(jugadores)
    for jugador in jugadores:
        assert gestor.cachos[jugador].getCantidadDados() == 5

def test_jugador_empieza(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    mocker.patch("random.randint", side_effect=[2, 5, 6])
    gestor = GestorPartida(jugadores)
    assert gestor.jugador_en_turno() == "Alex"

def test_jugador_empieza2(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    mocker.patch("random.randint", side_effect=[2, 5, 5, 4, 5])#Empate en los primeros tiros
    gestor = GestorPartida(jugadores)
    assert gestor.jugador_en_turno() == "Alex"

def test_rotacion_correcta(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    gestor = GestorPartida(jugadores)
    gestor.current_player = 0 #Se coloca al primer jugador para empezar para probar el test
    gestor.setDireccion("derecha")
    mocker.patch.object(gestor, "_jugar") #Pasar turno usa jugar pero no nos interesa en este test
    gestor.jugar()
    assert gestor.jugador_en_turno() == "Benjamín"
    gestor.jugar()
    assert gestor.jugador_en_turno() == "Alex"
    gestor.jugar()
    assert gestor.jugador_en_turno() == "Andrés"
    gestor.setDireccion("izquierda")
    gestor.jugar()
    assert gestor.jugador_en_turno() == "Alex"

def test_jugador_duda_mal(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    valores_dados = [
        6, 2, 4,  # Para que Andrés empiece
        5, 5, 5, 5, 5,  # Andrés
        5, 5, 5, 5, 5,  # Benjamín
        5, 5, 5, 5, 5  # Alex
    ]
    mocker.patch("random.randint", side_effect=valores_dados)
    mocker.patch('builtins.input', side_effect=["derecha", 5, 3, "dudar"])
    gestor = GestorPartida(jugadores)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 4
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].buffer == 1

def test_jugador_duda_bien(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    valores_dados = [
        6, 2, 4,  # Para que Andrés empiece
        5, 5, 5, 5, 5,  # Andrés
        5, 5, 5, 5, 5,  # Benjamín
        5, 5, 5, 5, 5  # Alex
    ]
    mocker.patch("random.randint", side_effect=valores_dados)
    mocker.patch('builtins.input', side_effect=["derecha", 3, 3, "dudar"])
    gestor = GestorPartida(jugadores)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].getCantidadDados() == 4
    assert gestor.cachos["Benjamín"].buffer == 1

def test_jugador_calza_bien(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    valores_dados = [
        6, 2, 4,  # Para que Andrés empiece
        5, 5, 5, 5, 5,  # Andrés
        5, 5, 5, 5, 5,  # Benjamín
        5, 5, 5, 5, 5  # Alex
    ]
    mocker.patch("random.randint", side_effect=valores_dados)
    mocker.patch('builtins.input', side_effect=["derecha", 5, 15, "calzar"])
    gestor = GestorPartida(jugadores)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Benjamín"].buffer == 1

def test_jugador_calza_mal(mocker):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    valores_dados = [
        6, 2, 4,  # Para que Andrés empiece
        5, 5, 5, 5, 5,  # Andrés
        5, 5, 5, 5, 5,  # Benjamín
        5, 5, 5, 5, 5  # Alex
    ]
    mocker.patch("random.randint", side_effect=valores_dados)
    mocker.patch('builtins.input', side_effect=["derecha", 3, 25, "calzar"])
    gestor = GestorPartida(jugadores)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 4
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].buffer == 0