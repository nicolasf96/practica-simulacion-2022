from math import sqrt, log
from scipy.special import erfinv


def ExponencialT(pseudo: list, lmbda: float) -> list:
    expo = []
    for r in pseudo:
        x = log(1-r)/(-lmbda)
        expo.append(x)
    return expo


def UniformeT(pseudo: list, a: float, b: float) -> list:
    """pseudo: Lista de numeros pseudoaleatorios
    a:valor minimo
    b:valor maximo
    returns: Lista distribuida uniformemente en [a,b]"""
    # la func de densidad es 1/b-a
    # la func de acumulacion es x-a/b-a
    uni = []
    for r in pseudo:
        x = a+(b-a)*r
        uni.append(x)
    return uni


def NormalT(pseudo: list, mu: float, sigma: float) -> list:
    norm = []
    for r in pseudo:
        x = mu+(sqrt(2)*sigma*erfinv((2*r)-1))
        norm.append(x)
    return norm
