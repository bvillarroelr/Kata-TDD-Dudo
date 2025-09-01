import math
class ArbitroRonda:
    def __init__(self):
        pass
        self.pool_dados = 0
    def resolver_duda(self, apuesta, mesa, ases_comodin: bool):
        cantidad, pinta = apuesta
        total = mesa.count(pinta)
        if ases_comodin and pinta != 1:
            total += mesa.count(1)
        return "pierde_quien_dudo" if total >= cantidad else "pierde_apostador"
        
    def resolver_calzar(self, apuesta, mesa, ases_comodin: bool):
        cantidad, pinta = apuesta
        total = mesa.count(pinta)
        if ases_comodin and pinta != 1:
            total += mesa.count(1)
        return "acierto" if total == cantidad else "falla"
    
    def verificarCalzar(self, dados_en_juego, cacho):
        if cacho.getCantidadDados() == 1:
            return True
        
        apuesta = cacho.getApuesta()
        cantidad_apostada = apuesta[0]

        if cantidad_apostada >= math.ceil(dados_en_juego / 2):
            return True
        else:
            return False

    def getPoolDados(self):
        return self.pool_dados
    
    def addPool(self):
        self.pool_dados += 1

    def popPool(self):
        self.pool_dados -= 1