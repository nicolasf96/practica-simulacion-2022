import math
from typing import Any
from math import log
import numpy as np
from numpy import std
from math import sqrt, pi, exp




def Uniforme( a: float, b: float, n:int) -> list:
    numbers = []
    for i in range(n):
        r = np.random.uniform(0, 1)
        x = a + (b - a) * r
        numbers.append(x)
    return numbers

def Exponencial(l: float, n:int) -> Any:
    numbers = []
    for i in range(n):
        ex = 1 / l
        r = np.random.uniform(0, 1)
        x = -ex * math.log(r)
        numbers.append(x)
    return numbers

def Normal( mu: float, var: float, K: int, n:int) -> list:
    numbers = []
    for i in range(n):
        suma = 0
        for i in range(K):
            r =np.random.uniform(0, 1)
            suma = suma + r
        x = var * (suma - K / 2) / sqrt(K / 12) + mu
        numbers.append(x)
    return numbers

def Gamma(k: int, alpha: float, n) -> list:
    numbers = []
    for i in range(n):
        tr = 1.0
        for i in range(k):
            r = np.random.uniform(0, 1)
            tr = tr * r
        x = -math.log(tr) / alpha
        numbers.append(x)
    return numbers

def Binomial( N: int, p: float, n: int) -> list:
    numbers = []
    for i in range(n):
        x = 0
        for i in range(N):
            r = np.random.uniform(0, 1)
            if ((r - p) <= 0):
                x = x + 1
        numbers.append(x)
    return numbers

def Hipergeometricas( N:int, p: float, m: int, n: int) -> list:
    numbers = []
    for i in range(n):
        x = 0.0
        for i in range(m):
            r = np.random.uniform(0, 1)
            if (r - p) <= 0:
                s = 1.0
                x += 1.0
            else:
                s = 0.0
            p = (N * p - s) / (N - 1.0)
            N -= 1.0
        numbers.append(x)
    return numbers

def Poisson( l: int, n: int) ->list:
    numbers = []
    for i in range(n):
        x = 0.0
        b = math.exp(-l)
        t = 1.0
        while True:
            r = np.random.uniform(0, 1)
            t = t * r
            if (t - b) <= 0:
                break
            else:
                x += 1.0
        numbers.append(x)
    return numbers
def Pascal(k: int, p: float, n: int)-> list:
    q = 1 - p
    numbers = []
    for i in range(n):
        tr = 1.0
        qr = math.log(q)
        for i in range(k):
            r = np.random.uniform(0, 1)
            tr = tr * r
        x = math.log(tr) / qr
        numbers.append(x)
    return numbers

print(Uniforme(a=0, b=1, n=1000))
print(Exponencial(l=3, n=1000))
print(Normal(mu=8, var=0.25, K=95, n=1000))
print(Gamma(k=8, alpha=0.95, n=1000))
print(Binomial(N=35, p=0.50, n=1000))
#print(Hipergeometricas(N=170, p=0.45, m=25, n=1000))
print(Poisson(l=6, n=1000))
print(Pascal(k=4,p=0.45, n=1000))