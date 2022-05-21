from tracemalloc import start, stop
import numpy as np

from math import sqrt, pi, exp, gamma


"""import matplotlib.pyplot as plt"""
"""from MTransformadas import Uniforme, Exponencial, Hipergeometricas, Normal"""


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
    a, b = mu-(100*des), mu+(100*des)
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
    numerador = lmbda*((lmbda*x)**(alpha-1))*exp(lmbda*x)
    denominador = gamma(alpha)
    return numerador/denominador


def GammaR(pseudo: list, lmbda: float, alpha: float) -> list:
    M = max([gamma(x) for x in range(start=.01, stop=1.01, step=.005)])


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
#distribucion_generada = NormalR(distribucion_generada, mu, var)
#distribucion_generada = Hipergeometricas(N=170, p=0.45, m=25, n=1000)
#distribucion_generada = Normal(3, 0.8, 95, 10000)
#distribucion_generada = UniformeR(distribucion_generada, 5, 15)
"""plt.hist(distribucion_generada)
#plt.axvline(x=mu, color='b', label='axvline - full height')
plt.title('Histograma de una variable')
plt.xlabel('Valor de la variable')
plt.ylabel('Conteo')
plt.show()"""
