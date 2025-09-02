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



