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

    def binomial(self, N, p):
        x = 0
        for i in range(N):
            r = self.gen.lcg()
            if ((r - p) <= 0):
                x = x + 1
        return x

    def pascal(self, k, q):
        tr = 1.0
        qr = math.log(q)
        for i in range(k):
            r = self.gen.lcg()
            tr = tr * r
        x = math.log(tr) / qr
        return x

    def hipergeometrica(self, N, p, m):
        x = 0.0

        for i in range(m):
            r = self.gen.lcg()
            if (r - p) <= 0:
                s = 1.0
                x += 1.0
            else:
                s = 0.0
            p = (N * p - s) / (N - 1.0)
            N -= 1.0

        return x

    def poisson(self, l):
        x = 0.0
        b = math.exp(-l)
        t = 1.0
        while True:
            r = self.gen.lcg()
            t = t * r
            if (t - b) <= 0:
                break
            else:
                x += 1.0
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

    def generador_binomial(self, N, p, n):
        numbers = []
        for i in range(n):
            numbers.append(self.funciones.binomial(N, p))
        return numbers

    def generador_hipergeometricas(self, N, p, m, n):
        numbers = []
        for i in range(n):
            x = self.funciones.hipergeometrica(N, p, m)
            numbers.append(x)
        return numbers

    def generador_poisson(self, lamb, n):
        numbers = []
        for i in range(n):
            numbers.append(self.funciones.poisson(lamb))
        return numbers


    def generador_pascal(self, k, p, n):
        q = 1 - p
        numbers = []
        for i in range(n):
            numbers.append(self.funciones.pascal(k, q))
        return numbers