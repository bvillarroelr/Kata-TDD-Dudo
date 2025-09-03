from cacho import Cacho
from dado import Dado
from arbitro_ronda import ArbitroRonda
from validador_apuesta import ValidadorApuesta


class GestorPartida:
    def __init__(self, jugadores):
        self.nuevo_turno =True
        self.jugadores = jugadores
        self.current_player = []
        self.direccion = 0
        self.cachos = {}
        self.arbitro = ArbitroRonda()
        for jugador in jugadores:
            self.cachos[jugador] = Cacho()
        self._escoger_jugador_inicial()

    def _jugar(self):
        opcion = input(f"{self.jugador_en_turno()} escriba su opción : (apostar, dudar o calzar")
        if opcion == "dudar":
            self.dudar()
        elif opcion == "calzar":
            self.calzar()
        elif opcion == "apostar":
            self.apostar()

    def setDireccion(self, direccion):
        if direccion == "derecha":
            self.direccion = 1
        elif direccion == "izquierda":
            self.direccion = -1

    def jugar(self):
        self._jugar()
        if not self.nuevo_turno:
            self.next_player()

    def jugador_en_turno(self):
        return self.jugadores[self.current_player]

    def _escoger_jugador_inicial(self):
        aux = list(range(0, len(self.jugadores)))
        dado = Dado()
        max = 0
        while len(self.current_player) != 1:
            for i in range(len(aux)):
                dado.lanzar()
                if (dado.getValor() == max):
                    self.current_player.append(aux[i])
                elif (dado.getValor() > max):
                    self.current_player = []
                    self.current_player.append(aux[i])
                    max = dado.getValor()
            max = 0
            aux = self.current_player
        self.current_player = self.current_player[0]

    def empezar_turno(self):
        self.nuevo_turno = False
        for cacho in self.cachos.values():
            cacho.lanzarDados()
        if self.direccion == 0:
            d=input(f"{self.jugador_en_turno()} decida la direccion (izquierda o derecha):")
            self.setDireccion(d)

        while True:
            try:
                print("Haga su apuesta inicial")
                pinta = input("Pinta: ")
                cantidad = input("Cantidad: ")
                self.validador = ValidadorApuesta(pinta,cantidad)
                break
            except ValueError as e:
                print(str(e))
        self.current_player = (self.direccion + self.current_player) % len(self.jugadores)

    def dudar(self):
        res = self.arbitro.resolver_duda((self.validador.cantidad_actual, self.validador.pinta_actual),
                                         self.cachos.values(), True)
        if res == "pierde_quien_dudo":
            self.cachos[self.jugador_en_turno()].retirarDado(self.arbitro)
            self.cachos[self.jugador_anterior()].agregarDado(self.arbitro)

        if res == "pierde_apostador":
            self.cachos[self.jugador_anterior()].retirarDado(self.arbitro)
            self.cachos[self.jugador_en_turno()].agregarDado(self.arbitro)
            self.current_player = (self.current_player - self.direccion) % len(self.jugadores)
        self.nuevo_turno =True

    def jugador_anterior(self):
        return self.jugadores[self.current_player-self.direccion]

    def calzar(self):

        res = self.arbitro.resolver_calzar((self.validador.cantidad_actual, self.validador.pinta_actual),
                                         self.cachos.values(), True)
        if res == "acierto":
            self.cachos[self.jugador_en_turno()].agregarDado(self.arbitro)
        elif res == "falla":
            self.cachos[self.jugador_en_turno()].retirarDado(self.arbitro)
        self.nuevo_turno=True

    def apostar(self):
            print("Haga su apuesta inicial")
            pinta = input("Pinta: ")
            cantidad = input("Cantidad: ")
            self.validador = ValidadorApuesta(pinta,cantidad)

    def next_player(self):
        self.current_player = (self.current_player + self.direccion) % len(self.jugadores)
