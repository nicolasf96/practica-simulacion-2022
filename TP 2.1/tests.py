import numpy as np
from scipy.stats import ksone, norm, chisquare, kstest, chi2
from math import sqrt, trunc
import matplotlib.pyplot as plt


# Parámetros:
# numerosPseudoaleatorios -> lista con números aleatorios
# q -> intervalo de confianza (100 - %confianza)
# df -> grados de libertad
def ChiCuadradoTest(numerosPseudoaleatorios, q, df):

    numbers = numerosPseudoaleatorios
    # Frecuencia observada en intervalos definidos (bins)
    # plt.hist() -> Devuelve la frecuencia absoluta de los 10 intervalo
    f_obs, x, c = plt.hist(numerosPseudoaleatorios, edgecolor='black')
    k = len(f_obs)
   # Frecuencia esperada en (bins) intervalos
    f_esp = len(numbers)/k

    # Realizo el cálculo y la sumatoria de la fórmula de chi2
    chi2_list = []
    for i in range(10):
        num = ((f_obs[i] - f_esp)**2)/f_esp
        chi2_list.append(num)
    # Al final obtengo un número de chi**2
    chi2_num = sum(chi2_list)
    #print('Valor chi cuadrado de la muestra GLC:', chi2_num)

    # Este número lo debo comparar en la tabla de contingencia de chi2
    # Si es mayor al valor establecido en la tabla, dado un intervalo de confianza (q) y grados de libertad (df) -> entonces no cumple

    # Creo la tabla de chi2 dados tales parámetros q y df
    chi2_table = chi2.ppf(q=q, df=df)

    if chi2_num < chi2_table:
        resultado = 'PASA LA PRUEBA'
        #print(f'Valor chi2_num:{chi2_num} < Valor chi2 tabla:{chi2_table}')
    else:
        resultado = 'No PASA LA PRUEBA'
        #print(f'Valor chi2_num:{chi2_num} < Valor chi2 tabla:{chi2_table}')

    return f'{resultado}, Valor datos:{chi2_num}, Valor tabla:{chi2_table}'


def KolmogorovTest(lista, alfa):
    '''Test de Kolmogorov-Smirnov, compara el cdf(valor crítico) de una distribucion uniforme con el cdf(d) de la muestra(lista) de tamaño n, para el nivel de significancia alfa. Devuelde verdadero si la distribución es uniforme, falso si no lo es.'''

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
    k_tabla = ksone.ppf(1 - alfa / 2, len(lista))

    if dmaximo < k_tabla:  # Comparo el valor d de la muestra con el valor crítico de la tabla
        # Hipotesis aceptada, distribucion es uniforme
        return f'dmax:{dmaximo} k_tabla:{k_tabla} pasa prueba '
    # Hipótesis rechazada, distribucion no es uniforme
    return f'dmax:{dmaximo} k_tabla:{k_tabla} NO pasa prueba '


def test_autocorrelacion(lista, alfa, m, i):
    N = len(lista)  # tamaño de la muestra
    # i-->rimer elemento donde se busca correlacion
    # m-->se busca correlacion entre r_i y r_i+k*m
    # M--> el mayor entero tal que i+(M+1)*m es menor que N
    M = trunc((N-(i+1))/m)-1
    if M <= 0:
        return
    densidad = 0
    densidad = sum([lista[(i+k*m)]*lista[i+(k+1)*m]
                   for k in range(0, M+1)])/(M+1)
    desviacion = sqrt((13*M)+7)/(12*(M+1))
    z = (densidad-0.25)/desviacion
    if (abs(z) > norm.ppf(1-(alfa/2))):
        #print(f'Son aleatorios')
        return f'Pasa la prueba, estadistico:{z} {densidad=}, {desviacion=}'
    #print(f'No son aleatorios')
    return f'No pasa la frueba, estadistico:{z} {densidad=}, {desviacion=}'


def test_rachas(pseudo: list, alpha: float = .05) -> str:
    media_est = np.mean(pseudo)
    sec = [1 if r > media_est else 0 for r in pseudo]
    c = 0
    for i in range(1, len(sec)-1):
        if sec[i-1] != sec[i]:
            c += 1
    n_0 = sec.count(0)
    n_1 = sec.count(1)
    nn2 = 2*n_0*n_1
    n = len(sec)
    mean_c = .5+(nn2/n)
    if n_1 == 0 or n_0 == 0:
        return 'No pasa la prueba, todos son mayores o menores que la mededia'
    var_c = (nn2*(nn2-n))/((n**2)*(n-1))
    z = (c-mean_c)/sqrt(var_c)
    if(abs(z) < norm.ppf(1-alpha/2)):
        return f'Pasa la prueba, {mean_c=}, {var_c=}, estadistico{z}'
    return f'No Pasa la prueba, {mean_c=}, {var_c=}, estadistico{z}'
