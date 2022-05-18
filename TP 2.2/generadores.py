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
    def normal(self, mu, std, K):
        suma = 0
        for i in range(K):
            r = self.gen.lcg()
            suma = suma + r
        x = std * (suma - K/2) / math.sqrt(K / 12) + mu
        return x
    def gamma(self, k, a):
        tr = 1.0
        for i in range(k):
            r = self.gen.lcg()
            tr = tr * r
        x = -math.log(tr) / a
        return x

class Distribuciones():
    funciones = Funciones()
    def generador_uniforme(self, a,b,n):
        numbers = []
        for i in range(n):
            numbers.append(Funciones().uniforme(a,b))
        return numbers

    def generador_exponencial(self, l, n):
        numbers = []
        for i in range(n):
            numbers.append(Funciones().exponencial(l))
        return numbers


    def generador_normal(self, media, desv, K, n):
        numbers = []
        for i in range(n):
            numbers.append(self.funciones.normal(media, desv, K))
        return numbers

    def generador_gamma(self, k, alpha, n):
        numbers = []
        for i in range(n):
            numbers.append(self.funciones.gamma(k, alpha))
        return numbers