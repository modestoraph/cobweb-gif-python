import numpy as np
class Funcao(object):

    #Construtor
    def __init__(self, r, s=0.0):
        self.r = r
        self.s = s

    # 1 - Função Logística
    def logistica(self, x):
        return self.r * x * (1 - x)

    # 2 - Função da Reta
    def reta(self, x):
        return self.r * x + self.s

    # 3 - Função Raiz Quadrada
    def raiz(self, x):
        return self.r * np.sqrt(x)

    # 4 - Função Cosseno
    def cosseno(self, x):
        return self.r * np.cos(x)

    # 5 - Função Expansora
    def expansora(self, x):
        return self.r * x % 1


