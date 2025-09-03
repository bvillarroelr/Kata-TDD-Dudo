import math
from contador_de_pintas import ContadorDePintas

class ArbitroRonda:
    def __init__(self):
        self.pool_dados = 0

    def resolver_duda(self, apuesta, mesa, ases_comodin: bool):
        cantidad, pinta = apuesta
        contador = ContadorDePintas(mesa)
        total = contador.contar(pinta=pinta, un_dado=not ases_comodin)
        return "pierde_quien_dudo" if total >= cantidad else "pierde_apostador"
        
    def resolver_calzar(self, apuesta, mesa, ases_comodin: bool):
        cantidad, pinta = apuesta
        contador = ContadorDePintas(mesa)
        total = contador.contar(pinta=pinta, un_dado=not ases_comodin)
        return "acierto" if total == cantidad else "falla"
    
    def verificarCalzar(self, dados_en_juego, cacho):
        if cacho.getCantidadDados() == 1:
            return True
        
        apuesta = cacho.getApuesta()
        cantidad_apostada = apuesta[0]
        return cantidad_apostada >= math.ceil(dados_en_juego / 2)

    def getPoolDados(self):
        return self.pool_dados
    
    def addPool(self):
        self.pool_dados += 1

    def popPool(self):
        self.pool_dados -= 1