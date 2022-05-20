import numpy as np
from numpy import std
from scipy.stats import norm
from math import sqrt, pi, exp


def max_densidad_norm(mu_: float, var_: float) -> tuple:
    """Devuelve el maximo y minimo valor que puede tener f de densidad en [0,1]"""
    f_0 = (1/var_*sqrt(2*pi))*exp(-((mu_**2)/2*(var_**2)))
    f_1 = (1/var_*sqrt(2*pi))*exp(-(((1-mu_)**2)/2*(var_**2)))
    return max(f_0, f_1), min(f_0, f_1)


def Normal( mu: float, var: float, K: int) -> list:
    pass
