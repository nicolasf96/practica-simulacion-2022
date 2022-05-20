from typing import Any
from math import log


def Exponencial(pseudo: list, lambda_e: float) -> Any:
    expo = []
    for r in pseudo:
        x = log(1-r)/lambda_e
        expo.append(x)
    return expo


def Uniforme(pseudo: list, a: float, b: float) -> list:
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
