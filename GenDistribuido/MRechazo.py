from tracemalloc import start, stop
import numpy as np

from math import sqrt, pi, exp, gamma, factorial, trunc


import matplotlib.pyplot as plt
from Otros import Uniforme, Exponencial, Hipergeometricas, Normal
from MTransformada import UniformeT, ExponencialT, NormalT


def densidad_norm(m, v, x):
    numerador = exp(-(((x-m)**2)/2*(v**2)))
    denominador = v*sqrt(2*pi)
    return numerador/denominador


def NormalR(pseudo: list, mu: float, des: float) -> list:
    """Aproximacion a una distribucion N~(mu,des) con metodo
    de aceptacion y rechazo de Von Neumann
    pseudo: Elementos pseudoaleatorios con distribucion uniforme
    mu:media de la funcion objetivo
    des:desvio de la funcion objetivo"""
    a, b = mu-(10*des), mu+(10*des)
    M = 1/(des*sqrt(2*pi))  # maximo valor de densidad de la funcion objetivo
    aceptados = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = a+((b-a)*V)
            if(M*U <= densidad_norm(mu, des, T)):
                # T se acepta
                aceptados.append(T)
                break
    norm = [T for T in aceptados]
    return norm


def densidad_gamma(lmbda: float, alpha: float, x: float) -> float:
    numerador = lmbda*((lmbda*x)**(alpha-1))*exp(-lmbda*x)
    denominador = gamma(alpha)
    return numerador/denominador


def GammaR(pseudo: list, lmbda: float, alpha: float, max_x: float) -> list:
    x_max = (alpha-1)/lmbda  # x en el que se da la maxima densidad
    M = densidad_gamma(lmbda=lmbda, alpha=alpha, x=x_max)
    a, b = 0, max_x
    gmma = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = b*V  # a=0 siempre

            if(M*U <= densidad_gamma(lmbda=lmbda, alpha=alpha, x=T)):
                gmma.append(T)
                break
    return gmma


def ExponenecialR(pseudo: list, lmbda: float, max_x: float) -> list:
    """Una distribucion exponencial es un caso especial de
    distribucion Gamma donde el parametro de forma alfa=1"""
    return GammaR(pseudo=pseudo, lmbda=lmbda, alpha=1, max_x=max_x)


def UniformeR(pseudo: list, a: float, b: float) -> list:
    aceptados = []
    M = 1/(b-a)
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = a+((b-a)*V)
            if(M*U <= 1/(b-a)):
                aceptados.append(T)
                break
    return aceptados


def densidad_Poisson(lmbda: float, x: int) -> float:
    numerador = (lmbda**x)*exp(-lmbda)
    denominador = factorial(x)
    return numerador/denominador


def PoissonR(pseudo: list, lmbda: float, max_x: int) -> list:
    M = densidad_Poisson(lmbda=lmbda, x=trunc(lmbda))
    poisson = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(V*max_x)  # a=0 siempre, b=max_x
            if(M*U <= densidad_Poisson(lmbda, T)):
                poisson.append(T)
                break
    return poisson


"""def densidad_Hipergeometrica(N_p: int, N_q: int, n: int, x: int) -> float:
    N = N_p+N_q
    a = factorial(N_p)/(factorial(x)*factorial(N_p-x))
    b = factorial(N_q)/(factorial(N-x)*factorial(N_q-(N-x)))
    c = factorial(N)/(factorial(n)*factorial(N-n))
    return (a*b)/c


def HipergeometricaR(pseudo: list, N_p: int, n: int) -> list:   #NO FUNCIONA
    N = len(pseudo)
    N_q = N-N_p
    q = trunc((n*N_q)/N)
    M = densidad_Hipergeometrica(N_p, N_q, n, q)
    hiper = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(V*N_p)
            if(M*U <= densidad_Hipergeometrica(N_p, N_q, n, T)):
                hiper.append(T)
                break
    return hiper"""


def densidad_binomial(n: int, p: float, x: int) -> float:
    a = factorial(n)/(factorial(x)*(factorial(n-x)))
    b = p**x
    c = (1-p)**(n-x)
    return a*b*c


def BinomialR(pseudo: list, n: int, p: float) -> list:
    M = densidad_binomial(n, p, trunc(n*p))
    binom = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(n*V)
            if(M*U <= densidad_binomial(n, p, T)):
                binom.append(T)
                break
    return binom


def densidad_Pascal(r: int, p: float, x: int) -> float:
    a = factorial(x+r-1)/(factorial(x)*(factorial(r-1)))
    b = p**r
    c = (1-p)**(x)
    return a*b*c


def PascalR(pseudo: list, r: int, p: float) -> list:
    M = densidad_Pascal(r, p, trunc(r*(1-p)/p))
    pascal = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(2*r*V)
            if(M*U <= densidad_Pascal(r, p, T)):
                pascal.append(T)
                break
    return pascal


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


#mu = 1
#var = 1
distribucion_generada = generador_numpy(10000)
distribucion_generada = NormalR(distribucion_generada, 19, 8)
#distribucion_generada = Hipergeometricas(N=170, p=0.45, m=25, n=1000)
#distribucion_generada = Normal(3, 0.8, 95, 10000)
#distribucion_generada = UniformeR(distribucion_generada, 5, 15)
#distribucion_generada = NormalT(distribucion_generada, 2, .5)
#distribucion_generada = GammaR(distribucion_generada, lmbda=2, alpha=2, max_x=20)
#plt.hist(distribucion_generada, bins=35)
#distribucion_generada = PoissonR(distribucion_generada, 10, 25)
#distribucion_generada = BinomialR(distribucion_generada, 40, .5)
#distribucion_generada = PascalR(distribucion_generada, 80, .5)
#distribucion_generada = HipergeometricaR(distribucion_generada, 900, 160)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
#plt.axvline(x=mu, color='b', label='axvline - full height')
plt.title('Histograma de una variable')
plt.xlabel('Valor de la variable')
plt.ylabel('Conteo')
plt.show()
