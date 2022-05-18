from datetime import time

import numpy as np
import math 



# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m
class glc:

    m = 22**48-1
    a = 25214903917
    c = 11
    x = 2500
    seed = 0

    def lcg(self):
        #semilla x
        self.x = (self.a * self.x + self.c) % self.m
        return (self.x / self.m)




class Funciones():
    gen= glc()
    def uniforme(self, a, b):
        r = self.gen.lcg()
        x = a + (b - a) * r
        return x

    def exponencial(self, a):
        ex = 1/a
        r = self.gen.lcg()
        x = -ex * math.log(r)
        return x

class Distribuciones():
    funciones = Funciones()
    def generador_uniforme(self, a,b,n):
        numbersUniforme = []
        for i in range(n):
            numbersUniforme.append(Funciones().uniforme(a,b))
        return numbersUniforme

    def generador_exponencial(self, l, n):
        #self.funciones.gen.get_seed()

        exponenciales = []
        for i in range(n):
            exponenciales.append(Funciones().exponencial(l))

        return exponenciales