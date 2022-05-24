from MTransformada import UniformeT, ExponencialT, NormalT
from MRechazo import UniformeR, GammaR, EmpiricaR, ExponenecialR, NormalR, BinomialR, PascalR, PoissonR, HipergeometricaR
from scipy.stats import uniform, norm, gamma, expon, binom, poisson, nbinom, geom
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


def KolmogorovTest(lista, alfa, dist_type):
    '''Test de Kolmogorov-Smirnov, compara el cdf(valor crítico) de una distribucion 
    con el cdf(d) de la muestra(lista) de tamaño n, para el nivel de significancia alfa. 
    Devuelde verdadero si la distribución es uniforme, falso si no lo es.'''

    lista.sort()  # Ordeno la lista de menor a mayor
    d_positivo = []  # array de los valores calculados para d positivo con la fórmula de KS
    d_negativo = []  # array de los valores calculados para d negativo con la fórmula de KS

    for i in range(len(lista)):
        # Fórmula de KS para d positivo
        d_positivo.append(i / len(lista) - lista[i])
        # Fórmula de KS para d negativo
        d_negativo.append(lista[i] - (i - 1) / len(lista))

    # Calculo el máximo entre los d
    dmaximo = max(max(d_positivo), max(d_negativo))
    # Tomo el valor crítico d de la tabla de KS
    if type(dist_type) is type(binom):
        k_tabla = binom.ppf(1 - alfa / 2, len(lista), p=p)
    elif type(dist_type) is type(nbinom):
        k_tabla = nbinom.ppf(1 - alfa / 2, len(lista), p=p)
    else:
        k_tabla = dist_type.ppf(1 - alfa / 2, len(lista))

    if dmaximo < k_tabla:  # Comparo el valor d de la muestra con el valor crítico de la tabla
        # Hipotesis aceptada, distribucion es uniforme
        return f'Pasa prueba '
    # Hipótesis rechazada, distribucion no es uniforme
    return f'No pasa prueba '


cola = .05  # 1-cola/2 es el intervalo de confianza para el test Kolmogorov-Smirnov
a, b = 2, 15
dist = generador_numpy(10000)
dist = UniformeT(dist, a, b)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA uniforme-Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion UniformeT entre {a=} y {b=}-> {KolmogorovTest(dist,cola,uniform)}")

mu, des = 2, .5
dist = generador_numpy(10000)
dist = NormalT(dist, mu, des)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Normal- Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion NormalT {mu=} y {des=}-> {KolmogorovTest(dist,cola,norm)}")

lmbda_e = 2
dist = generador_numpy(10000)
dist = ExponencialT(dist, lmbda_e)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Exponencial- Transformacion inversa')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion ExponencialT con {lmbda_e=}-> {KolmogorovTest(dist,cola,expon)}")


dist = generador_numpy(10000)
dist = UniformeR(dist, a, b)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Uniforme-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion UniformeR entre {a=} y {b=}-> {KolmogorovTest(dist,cola,uniform)}")

dist = generador_numpy(10000)
dist = NormalR(dist, mu, des)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Normal-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion NormalR {mu=} y {des=}-> {KolmogorovTest(dist,cola,norm)}")

lmbda_p, X_p = 10, 25
dist = generador_numpy(10000)
dist = PoissonR(dist, lmbda_p, X_p)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion de Poisson-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion PoissonR {lmbda_p=} y {X_p=}-> {KolmogorovTest(dist,cola,poisson)}")


n, p = 40, .5
dist = generador_numpy(10000)
dist = BinomialR(dist, n, p)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Binomial-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion BinomialR {n=} y {p=}-> {KolmogorovTest(dist,cola,binom)}")

r = 80
dist = generador_numpy(10000)
dist = PascalR(dist, r, p)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion de Pascal-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion PascalR {r=} y {p=}-> {KolmogorovTest(dist,cola,nbinom)}")

lmbda_g, alpha_g, X_g = 2, 2, 20
dist = generador_numpy(10000)
dist = GammaR(dist, lmbda_g, alpha_g, X_g)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Gamma-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion GammaR {lmbda_g=}, {alpha_g=} y {X_g=}-> {KolmogorovTest(dist,cola,gamma)}")

dist = generador_numpy(10000)
dist = ExponenecialR(dist, lmbda=lmbda_e, max_x=20)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Exponencial-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion ExponencialR con {lmbda_e=}-> {KolmogorovTest(dist,cola,expon)}")

dist = generador_numpy(10000)
fr_empirica = [.01, .09, .03, .06, .04, .07, .1, .3, .3]
dist = EmpiricaR(dist, -9, fr_empirica)
plt.hist(dist, bins=round(
    sqrt(len(dist))),  edgecolor='black')
plt.title('Histograma de una VA con distribucion Empicrica-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()

N_g, K_g, n_g = 200, 60, 10
dist = generador_numpy(10000)
dist = HipergeometricaR(dist, N_g, K_g, n_g)
plt.hist(dist, bins=round(sqrt(len(dist))),  edgecolor='black')
plt.title(
    'Histograma de una VA con distribucion Hipergeometrica-Aceptacion y rechazo')
plt.xlabel('Valor de la variable')
plt.ylabel('Ocurrencias')
plt.show()
print(
    f"Test Kolmogorov-Smirnov: Distribucion HiperGeometrica con {N_g=}, {K_g=} y {n_g=}-> {KolmogorovTest(dist,cola,geom)}")
