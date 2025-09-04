from cacho import Cacho
from dado import Dado
from arbitro_ronda import ArbitroRonda
from validador_apuesta import ValidadorApuesta


class GestorPartida:
    def __init__(self, jugadores):
        if len(jugadores) < 2:
            raise Exception("Se necesitan al menos 2 jugadores para instanciar")
        self.juego_activo = True
        self.nuevo_turno =True
        self.turno_especial = None
        self.obligar = None
        self.jugadores = jugadores
        self.current_player = []
        self.direccion = 0
        self.cachos = {}
        self.arbitro = ArbitroRonda()
        self.jugadores_con_especial = []
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
        if not self.juego_activo:
            raise Exception("Juego terminado")
        if self.nuevo_turno:
            raise Exception("El turno aun no comienza")
        self.next_player()
        self._jugar()

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
        if not self.juego_activo:
            raise Exception("Juego terminado")
        if not self.nuevo_turno:
            raise Exception("El turno ya comenzó")
        for jugador in self.jugadores:
            self.cachos[jugador].lanzarDados()
        if self.direccion == 0:
            d=input(f"{self.jugador_en_turno()} decida la direccion (izquierda o derecha):")
            self.setDireccion(d)

        if self.turno_especial == self.jugador_en_turno():
            self.obligar = input(f"{self.jugador_en_turno()}, puedes usar tu turno especial, ¿deseas usarlo? (cerrado, abierto o no)" )

        self.apostar()
        self.nuevo_turno = False

    def dudar(self):
        res = self.arbitro.resolver_duda((self.validador.cantidad_actual, self.validador.pinta_actual),
                                         self.cachos.values(), True)
        if res == "pierde_quien_dudo":
            self.cachos[self.jugador_en_turno()].retirarDado(self.arbitro)
            self.cachos[self.jugador_anterior()].agregarDado(self.arbitro)
            self.verificarDados(self.jugador_en_turno())

        if res == "pierde_apostador":
            self.cachos[self.jugador_anterior()].retirarDado(self.arbitro)
            self.cachos[self.jugador_en_turno()].agregarDado(self.arbitro)
            self.current_player = (self.current_player - self.direccion) % len(self.jugadores)
            self.verificarDados(self.jugador_en_turno())
        self.nuevo_turno =True

    def jugador_anterior(self):
        return self.jugadores[self.current_player-self.direccion]

    def calzar(self):
        sum = 0
        for jugador in self.jugadores:
            sum += self.cachos[jugador].getCantidadDados()
        if not self.arbitro.verificarCalzar(sum,self.cachos[self.jugador_en_turno()],self.validador.cantidad_actual) :
            self._player_rollback()
            raise Exception("No puedes calzar en estas condiciones.")

        res = self.arbitro.resolver_calzar((self.validador.cantidad_actual, self.validador.pinta_actual),
                                         self.cachos.values(), True)
        if res == "acierto":
            self.cachos[self.jugador_en_turno()].agregarDado(self.arbitro)
            self.turno_especial = None
        elif res == "falla":
            self.cachos[self.jugador_en_turno()].retirarDado(self.arbitro)
            self.verificarDados(self.jugador_en_turno())
        self.nuevo_turno=True


    def apostar(self):
        try:
            print("Haga su apuesta ")
            pinta = input("Pinta: ")
            cantidad = input("Cantidad: ")
            if self.nuevo_turno == True:
                self.validador = ValidadorApuesta(pinta, cantidad,
                especial=self.obligar == "cerrado" or self.obligar == "abierto")
                return
            un_dado =False
            if self.cachos[self.jugador_en_turno()].getCantidadDados() == 1:
                un_dado=True
            self.validador.apostar(pinta,cantidad,un_dado=un_dado)
        except ValueError as e:
            self._player_rollback()
            raise ValueError(f"Apuesta invalida: {str(e)}")

    def next_player(self):
        self.current_player = (self.current_player + self.direccion) % len(self.jugadores)

    def verificarDados(self, jugador):
        self.turno_especial = None
        if self.cachos[jugador].getCantidadDados() == 1:
            if jugador not in self.jugadores_con_especial:
                self.jugadores_con_especial.append(jugador)
                self.turno_especial = jugador
        elif self.cachos[jugador].getCantidadDados() == 0:
            if self.direccion == 1 and self.current_player == len(self.jugadores) - 1:
                self.current_player = 0
            elif self.direccion == -1 :
                if self.current_player == 0:
                    self.current_player = len(self.jugadores) - 2
                else:
                    self.current_player = (self.current_player -1) % (len(self.jugadores)-1)
            self.jugadores.remove(jugador)
            self.verificar_victoria()

    def ver_dados(self):
        if self.obligar == None:
            return self.cachos[self.jugador_en_turno()].getResultados()
        elif self.obligar == "cerrado":
            if self.turno_especial == self.jugador_en_turno():
                return self.cachos[self.jugador_en_turno()].getResultados()
            else:
                return []
        elif self.obligar == "abierto":
            dados = []
            for jugador in self.jugadores:
                if jugador != self.jugador_en_turno():
                    dados.append(self.cachos[jugador].getResultados())
            return dados

    def verificar_victoria(self):
        if len(self.jugadores) == 1:
            print(f"{self.jugadores[0]} ha ganado")
            self.juego_activo = False

    def _player_rollback(self):
        if not self.nuevo_turno:
            self.current_player = (self.current_player - self.direccion) % len(self.jugadores)