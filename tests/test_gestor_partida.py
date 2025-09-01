import pytest


def test_base_partida():
    jugadores = ["Andrés", "Benjamín","Alex"]
    gestor = GestorPartida(jugadores)
    for jugador in jugadores:
        assert gestor.cachos[jugador].getCantidadDados() == 5