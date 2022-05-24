from MTransformada import UniformeT, ExponencialT, NormalT
from MRechazo import UniformeR, GammaR, EmpiricaR, ExponenecialR, NormalR, BinomialR, PascalR, PoissonR
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


distribucion_generada = generador_numpy(10000)
distribucion_generada = UniformeT(distribucion_generada, 2, 15)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA uniforme-Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = NormalT(distribucion_generada, 2, .5)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Normal- Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = ExponencialT(distribucion_generada, 2)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Exponencial- Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = UniformeR(distribucion_generada, 5, 15)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Uniforme-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = NormalR(distribucion_generada, 19, 8)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Normal-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = PoissonR(distribucion_generada, 10, 25)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion de Poisson-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = BinomialR(distribucion_generada, 40, .5)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Binomial-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = PascalR(distribucion_generada, 80, .5)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion de Pascal-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = GammaR(
    distribucion_generada, lmbda=2, alpha=2, max_x=20)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Gamma-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
distribucion_generada = ExponenecialR(distribucion_generada, lmbda=2, max_x=20)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Exponencial-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

distribucion_generada = generador_numpy(10000)
fr_empirica = [.01, .09, .03, .06, .04, .07, .1, .3, .3]
distribucion_generada = EmpiricaR(distribucion_generada, -9, fr_empirica)
plt.hist(distribucion_generada, bins=round(
    sqrt(len(distribucion_generada))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Empicrica-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

#plt.axvline(x=mu, color='b', label='axvline - full height')
