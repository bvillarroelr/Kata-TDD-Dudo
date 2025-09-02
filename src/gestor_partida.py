from cacho import Cacho
from dado import Dado

class GestorPartida:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.current_player = []
        self.direccion = 0
        aux = list(range(0,len(jugadores)))
        self.cachos = {}
        for jugador in jugadores:
            self.cachos[jugador] = Cacho()
        dado = Dado()
        max = 0
        while len(self.current_player) != 1:
            for i in range (len(aux)):
                dado.lanzar()
                if (dado.getValor()== max):
                    self.current_player.append(aux[i])
                elif (dado.getValor()> max):
                    self.current_player = []
                    self.current_player.append(aux[i])
                    max = dado.getValor()
            max = 0
            aux = self.current_player
        self.current_player = self.current_player[0]

    def jugar(self):
         pass

    def setDireccion(self, direccion):
        if direccion == "derecha":
            self.direccion = 1
        elif direccion == "izquierda":
            self.direccion = -1

    def pasar_turno(self):
        self.jugar()
        self.current_player = (self.current_player + self.direccion) % len(self.jugadores)

    def jugador_en_turno(self):
        return self.jugadores[self.current_player]