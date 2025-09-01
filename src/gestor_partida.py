from cacho import Cacho


class GestorPartida:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.cachos = {}
        for jugador in jugadores:
            self.cachos[jugador] = Cacho()