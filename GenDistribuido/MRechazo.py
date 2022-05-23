from tracemalloc import start, stop
import numpy as np

from math import sqrt, pi, exp, gamma


import matplotlib.pyplot as plt
from Otros import Uniforme, Exponencial, Hipergeometricas, Normal
from MTransformada import UniformeT, ExponencialT, NormalT


def densidad_norm(m, v, x):
    return (1/v*sqrt(2*pi))*exp(-(((x-m)**2)/2*(v**2)))


def max_densidad_norm(mu_: float, var_: float) -> float:
    """Devuelve el maximo valor que puede tener f de densidad en [0,1]"""
    f_0 = densidad_norm(mu_, var_, 0)
    f_1 = densidad_norm(mu_, var_, 1)
    return max(f_0, f_1)


def NormalR(pseudo: list, mu: float, des: float) -> list:
    """Aproximacion a una distribucion N~(mu,des) con metodo
    de aceptacion y rechazo de Von Neumann
    pseudo: Elementos pseudoaleatorios con distribucion uniforme
    mu:media de la funcion objetivo
    des:desvio de la funcion objetivo"""
    a, b = mu-(5*des), mu+(5*des)
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
            T = b*V

            if(M*U <= densidad_gamma(lmbda=lmbda, alpha=alpha, x=T)):
                gmma.append(T)
                break
    return gmma


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


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


#mu = 1
#var = 1
distribucion_generada = generador_numpy(10000)
#distribucion_generada = NormalR(distribucion_generada, 19, 8)
#distribucion_generada = Hipergeometricas(N=170, p=0.45, m=25, n=1000)
#distribucion_generada = Normal(3, 0.8, 95, 10000)
#distribucion_generada = UniformeR(distribucion_generada, 5, 15)
#distribucion_generada = NormalT(distribucion_generada, 2, .5)
#distribucion_generada = GammaR(distribucion_generada, lmbda=2, alpha=2, max_x=20)
plt.hist(distribucion_generada, bins=35)
#plt.axvline(x=mu, color='b', label='axvline - full height')
plt.title('Histograma de una variable')
plt.xlabel('Valor de la variable')
plt.ylabel('Conteo')
plt.show()
