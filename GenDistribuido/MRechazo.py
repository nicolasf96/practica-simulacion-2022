import numpy as np

from math import sqrt, pi, exp

import matplotlib.pyplot as plt
import numpy as np
from MTransformadas import Uniforme, Exponencial, Hipergeometricas, Normal


def densidad_norm(m, v, x):
    return (1/v*sqrt(2*pi))*exp(-(((x-m)**2)/2*(v**2)))


def max_densidad_norm(mu_: float, var_: float) -> float:
    """Devuelve el maximo valor que puede tener f de densidad en [0,1]"""
    f_0 = densidad_norm(mu_, var_, 0)
    f_1 = densidad_norm(mu_, var_, 1)
    return max(f_0, f_1)


def normal(pseudo: list, mu: float, var: float) -> list:
    a, b = mu-(2*var), mu+(2*var)
    M = 1/(var*sqrt(2*pi))  # maximo valor de densidad de la funcion objetivo
    aceptados = []
    for U in pseudo:
        while True:
            V = np.random.uniform(0, 1)
            T = a+((b-a)*V)
            if(M*U <= densidad_norm(mu, var, T)):
                # T se acepta
                aceptados.append(T)
                break
    norm = [a+((b-a)*T) for T in aceptados]
    return norm


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


"""mu = -1
var = 1.2
distribucion_generada = generador_numpy(10000)
distribucion_generada = normal(
    distribucion_generada, mu, var)"""
distribucion_generada = Hipergeometricas(N=170, p=0.45, m=25, n=1000)
#distribucion_generada = Normal(3, 0.8, 95, 10000)
plt.hist(distribucion_generada, bins=45)
#plt.axvline(x=mu, color='b', label='axvline - full height')
plt.title('Histograma de una variable')
plt.xlabel('Valor de la variable')
plt.ylabel('Conteo')
plt.show()
