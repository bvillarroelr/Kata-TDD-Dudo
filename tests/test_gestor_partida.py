import pytest
from gestor_partida import *

from dado import Dado

@pytest.fixture
def partida_base(mocker):
    def _crear(jugadores, valores_dados, inputs):
        mocker.patch("random.randint", side_effect=valores_dados)
        mocker.patch("builtins.input", side_effect=inputs)
        gestor = GestorPartida(jugadores)
        return gestor
    return _crear

def preparar_dados(gestor, dados_por_jugador):
    for nombre, cantidad in dados_por_jugador.items():
        gestor.cachos[nombre].lista_dados = [Dado() for _ in range(cantidad)]
        gestor.cachos[nombre].setCantidadDados(cantidad)

def avanzar_turnos(gestor, cantidad):
    for _ in range(cantidad):
        gestor.empezar_turno()
        gestor.jugar()

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
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Benjamín"
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Alex"
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Andrés"
    gestor.setDireccion("izquierda")
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Alex"

def test_jugador_duda_mal(partida_base):
    dados = [6, 2, 4] + [5] * 15
    inputs = ["derecha", 5, 3, "dudar"]
    gestor = partida_base(["Andrés", "Benjamín", "Alex"], dados, inputs)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 4
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].buffer == 1
    assert gestor.jugador_en_turno() == "Benjamín"

def test_jugador_duda_bien(partida_base):
    dados = [6, 2, 4] + [5] * 15
    inputs = ["derecha", 3, 3, "dudar"]
    gestor = partida_base(["Andrés", "Benjamín", "Alex"], dados, inputs)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].getCantidadDados() == 4
    assert gestor.cachos["Benjamín"].buffer == 1
    assert gestor.jugador_en_turno() == "Andrés"

def test_jugador_calza_bien(partida_base):
    dados = [6, 2, 4] + [5] * 15
    inputs = ["derecha", 5, 15, "calzar"]
    gestor = partida_base(["Andrés", "Benjamín", "Alex"], dados, inputs)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Benjamín"].buffer == 1
    assert gestor.jugador_en_turno() == "Benjamín"


def test_jugador_calza_mal(partida_base):
    dados = [6, 2, 4] + [5] * 15
    inputs = ["derecha", 3, 25, "calzar"]
    gestor = partida_base(["Andrés", "Benjamín", "Alex"], dados, inputs)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 4
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].buffer == 0
    assert gestor.jugador_en_turno() == "Benjamín"

def test_jugador_apuesta(partida_base):
    dados = [6, 2, 4] + [5] * 15
    inputs = ["derecha", 3, 15, "apostar", 4, 15]
    gestor = partida_base(["Andrés", "Benjamín", "Alex"], dados, inputs)
    gestor.empezar_turno()
    gestor.jugar()
    assert gestor.cachos["Benjamín"].getCantidadDados() == 5
    assert gestor.cachos["Andrés"].getCantidadDados() == 5
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Alex"
    assert gestor.ver_dados() == [5,5,5,5,5]

def test_ronda_obligada_abierta(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*80
    inputs = ["derecha"] + [ 3, 15, "dudar"] * 4 + ["abierto", 1, 15]
    gestor = partida_base(jugadores, dados, inputs)
    avanzar_turnos(gestor, 4)
    gestor.empezar_turno()
    assert gestor.cachos["Andrés"].getCantidadDados() == 1
    assert gestor.ver_dados() == [[5,5,5,5,5],[5,5,5,5,5]]
    gestor.next_player()
    assert gestor.ver_dados() == [[5],[5,5,5,5,5]]

def test_ronda_obligada_cerrada(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*80
    inputs = ["derecha"]+ [3, 15, "dudar"] * 4 + ["cerrado", 1, 5]
    gestor = partida_base(jugadores, dados, inputs)
    avanzar_turnos(gestor, 4)
    gestor.empezar_turno()
    assert gestor.cachos["Andrés"].getCantidadDados() == 1
    assert gestor.ver_dados() == [5]
    gestor.next_player()
    assert gestor.ver_dados() == []

def test_jugador_pierde(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*45
    inputs = ["derecha", 3, 15, "dudar", 3, 15, "dudar", 3, 15]
    gestor = partida_base(jugadores, dados, inputs)

    gestor.empezar_turno()
    gestor.jugar()
    gestor.cachos["Andrés"].setCantidadDados(1)
    assert gestor.cachos[gestor.jugador_en_turno()].getCantidadDados() == 1

    gestor.empezar_turno()
    gestor.jugar()
    gestor.empezar_turno()
    assert gestor.jugador_en_turno() == "Benjamín"
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Alex"
    gestor.next_player()
    assert gestor.jugador_en_turno() == "Benjamín"

def test_jugador_gana(partida_base, capsys):
    jugadores = ["Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*35
    inputs = ["derecha", 3, 15, "dudar", 3, 15, "dudar", 3, 15]
    gestor = partida_base(jugadores, dados, inputs)

    gestor.empezar_turno()
    gestor.jugar()
    gestor.cachos["Benjamín"].setCantidadDados(1)
    assert gestor.cachos[gestor.jugador_en_turno()].getCantidadDados() == 1

    gestor.empezar_turno()
    gestor.jugar()
    salida = capsys.readouterr()
    assert "Alex ha ganado" in salida.out

    with pytest.raises(Exception, match="Juego terminado"):
        gestor.jugar()

def test_jugador_apuesta_mal(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*35
    inputs = ["derecha", 1, 15, 2, 15, "apostar", 3, 14]
    gestor = partida_base(jugadores, dados, inputs)

    with pytest.raises(ValueError, match="Apuesta invalida"):
        gestor.empezar_turno()

    gestor.empezar_turno()
    assert gestor.jugador_en_turno() == "Andrés"

    with pytest.raises(ValueError, match="Apuesta invalida"):
        gestor.jugar()

    assert gestor.jugador_en_turno() == "Andrés"

def test_jugador_calza_invalido(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*35
    inputs = ["derecha", 2, 5, "calzar"]
    gestor = partida_base(jugadores, dados, inputs)

    gestor.empezar_turno()
    with pytest.raises(Exception, match="No puedes calzar en estas condiciones."):
        gestor.jugar()

    assert gestor.jugador_en_turno() == "Andrés"

def test_mala_apuesta_ronda_especial(partida_base):
    jugadores = ["Andrés", "Benjamín", "Alex"]
    dados = [6, 2, 4] + [5]*15
    inputs = ["derecha", 3, 15, "dudar", "cerrado", 1, 5,
              "apostar", 2, 5, "apostar", 1, 6, "apostar", 1, 5, "apostar", 6, 6]
    gestor = partida_base(jugadores, dados, inputs)

    preparar_dados(gestor, {"Andrés": 2, "Alex": 1})

    gestor.empezar_turno()
    gestor.jugar()
    gestor.empezar_turno()

    with pytest.raises(ValueError, match="Apuesta invalida"):
        gestor.jugar()

    gestor.jugar()

    with pytest.raises(ValueError, match="Apuesta invalida"):
        gestor.jugar()

    gestor.jugar()
    assert gestor.jugador_en_turno() == "Alex"
