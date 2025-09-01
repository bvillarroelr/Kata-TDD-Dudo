from dado import Dado
from arbitro_ronda import ArbitroRonda
class Cacho:
    def __init__(self):
        self.visible = False
        self.apuesta = None # tupla
        self.lista_dados = []
        for i in range (1,6):
            d = Dado()
            self.lista_dados.append(d)

        self.cantidad_dados = len(self.lista_dados)
    def lanzarDados(self):
        for i in range(len(self.lista_dados)):
            self.lista_dados[i].lanzar()
        return self.lista_dados
    
    def agregarDado(self, arbitro):
        if self.cantidad_dados < 5:
            d = Dado()
            self.lista_dados.append(d)        
            self.cantidad_dados +=1
            arbitro.popPool()
        
    def retirarDado(self, arbitro):
        if self.cantidad_dados > 0:
            self.lista_dados.pop()
            self.cantidad_dados -=1
            arbitro.addPool()
        else:
            return

    def getResultados(self):
        l = []
        for i in range(len(self.lista_dados)):
            l.append(self.lista_dados[i].getValor())
        return l    
    
    def toggleMostrar(self):
        if self.visible is False:
            self.visible = True
        else:
            self.visible = False
        return self.visible

    def getCantidadDados(self):
        return self.cantidad_dados
    
    def setCantidadDados(self, num):
        self.cantidad_dados = num

    def getApuesta(self):
        return self.apuesta
    
    def setApuesta(self, apuesta: tuple):
        self.apuesta = apuesta