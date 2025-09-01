

class ContadorDePintas:
    def __init__(self, lista_cachos):
        self.lista_cachos = lista_cachos
        self.resultados_reales = [0,0,0,0,0,0]
        self.resultados = [0,0,0,0,0,0]
        for cacho in lista_cachos:
            dados = cacho.getResultados()
            for resultado in dados:
                self.resultados_reales[resultado-1] += 1
        self.resultados[0] = self.resultados_reales[0]
        for i in range(1,len(self.resultados_reales)):
            self.resultados[i] = self.resultados_reales[i] + self.resultados[0]

    def contar(self,pinta=0, un_dado=False):
        self._verificar_rango(pinta)
        if un_dado:
            return self._ronda_especial(pinta)
        return self._ronda_normal(pinta)

    def _ronda_especial(self,pinta):
        if pinta == 0:
            return self.resultados_reales
        else:
            return self.resultados_reales[pinta-1]

    def _ronda_normal(self,pinta):
        if pinta == 0:
            return self.resultados
        else:
            return self.resultados[pinta-1]

    def _verificar_rango(self,pinta):
        if pinta < 0 or pinta > 6:
            raise ValueError("Pinta fuera de rango")