from dado import Dado

class Cacho:
    def __init__(self):
        self.visible = False
        self.lista_dados = []
        for i in range (1,6):
            d = Dado()
            self.lista_dados.append(d)

        self.cantidad_dados = len(self.lista_dados)
    def lanzarDados(self):
        for i in range(len(self.lista_dados)):
            self.lista_dados[i].lanzar()
        return self.lista_dados
    
    def agregarDado(self):
        d = Dado()
        self.lista_dados.append(d)
        self.cantidad_dados +=1
        
    def retirarDado(self):
        if self.cantidad_dados > 0:
            self.lista_dados.pop()
            self.cantidad_dados -=1
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