class ArbitroRonda:
    def __init__(self):
        pass

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
