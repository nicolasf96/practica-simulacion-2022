import numpy as np
from math import sqrt, pi, exp, gamma, factorial, trunc


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


def densidad_Hipergeometrica(N: int, K: int, n: int, x: int) -> float:
    a = factorial(K)/(factorial(x)*factorial(K-x))
    b = factorial(N-K)/(factorial(n-x)*factorial(N-K-(n-x)))
    c = factorial(N)/(factorial(n)*factorial(N-n))
    return (a*b)/c


def HipergeometricaR(pseudo: list, N: int, K: int, n: int) -> list:
    media = n*K/N
    M = densidad_Hipergeometrica(N, K, n, media)
    hiper = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(n*V)
            if(M*U <= densidad_Hipergeometrica(N, K, n, T)):
                hiper.append(T)
                break
    return hiper


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


def EmpiricaR(pseudo: list, min_x: int, lista_fr: list) -> list:
    """pseudo: n pseudoaleatorio en [0,1]
    min_x:valor minimo que asumira la VA que sigue la distribucion empirica
    lista_fr:frecuencia relativa de cada numero consecutivo a partir de min_x
    :!!! sum(lista_fr)==1 !!!"""
    n = len(lista_fr)
    a, b = min_x, min_x+n
    frec_rel = dict()
    M = max(lista_fr)
    empiric = []
    for i in range(a, b):
        frec_rel.setdefault(i, lista_fr.pop(0))
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = trunc(a+(b-a)*V)
            if T not in frec_rel.keys():
                break
            if(M*U <= frec_rel[T]):
                empiric.append(T)
                break
    return empiric
