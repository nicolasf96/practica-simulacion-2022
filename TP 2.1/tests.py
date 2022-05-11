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
    print('Valor chi cuadrado de la muestra GLC:', chi2_num)

    # Este número lo debo comparar en la tabla de contingencia de chi2
    # Si es mayor al valor establecido en la tabla, dado un intervalo de confianza (q) y grados de libertad (df) -> entonces no cumple

    # Creo la tabla de chi2 dados tales parámetros q y df
    chi2_table = chi2.ppf(q=q, df=df)

    if chi2_num < chi2_table:
        resultado = True
        print('PASA LA PRUEBA:')
        print(f'Valor chi2_num:{chi2_num} < Valor chi2 tabla:{chi2_table}')
    else:
        resultado = False
        print('No PASA LA PRUEBA:')
        print(f'Valor chi2_num:{chi2_num} < Valor chi2 tabla:{chi2_table}')

    return resultado, chi2_num, chi2_table

# Test KS


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
    # i=0 #primer elemento donde se busca correlacion
    # m=0 #se busca correlacion entre r_i y r_i+k*m
    # M=0 #M debe ser el mayor entero tal que i+(M+1)*m es menor que N
    M = trunc((N-(i+1))/m)-1
    if M <= 0:
        return
    densidad = 0
    densidad = sum([lista[(i+k*m)]*lista[i+(k+1)*m]
                   for k in range(0, M+1)])/(M+1)
    desviacion = sqrt((13*M)+7)/(12*(M+1))
    significancia = (densidad-0.25)/desviacion
    if (abs(significancia) > norm.ppf(1-(alfa/2))):
        #print(f'Son aleatorios')
        return True
    #print(f'No son aleatorios')
    return False


def AutocorrelationTest2(x, n):
    '''Test de Autocorrelacion. Devuelve un gráfico.'''

    media_lista = np.mean(x)
    def c(k): return np.mean([(x[i] - media_lista) * (x[i + k] - media_lista)
                              for i in range(n - k)])  # autocovariance

    def r(k): return c(k) / c(0)  # Autocorrelation

    correlacion = [r(k) for k in range(100)]

    plt.plot(correlacion)
    plt.show()


# NO FUNCIONA
"""
def calcular_subsecuencias(lista):
    subsecuencias_menor_5 = 0
    subsecuencias_mayor_6 = 0
    n = len(lista)
    for i in range(n - 1):
        cant = 0
        if lista[i] < lista[i + 1]:
            j = i
            while lista[j] < lista[j + 1] and j < n - 2:
                cant += 1
                j += 1
            if cant <= 5:
                subsecuencias_menor_5 += 1
            else:
                subsecuencias_mayor_6 += 1
            i = j
    print('Cantidas de subsecuencias crecientes de longitud <= 5:', subsecuencias_menor_5)
    print('Cantidas de subsecuencias crecientes de longitud >= 6:', subsecuencias_mayor_6)
    total_corridas = subsecuencias_menor_5 + subsecuencias_mayor_6
    print('Total de subsecuencias corridas:', total_corridas)

    H0 = "los números generados son independientes"
    H1 = "los números generados no son independientes"
    print('\nHipótesis 0:', H0)
    print('\nHipótesis 1:', H1)

<<<<<<< Updated upstream
def KolmogorovTest(lista, alfa):
    '''Test de Kolmogorov-Smirnov, compara el cdf de una distribucion uniforme con el cdf de la muestra de tamaño n, para el nivel de significancia alfa'''
    
    lista.sort() #Ordeno la lista de menor a mayor
    d_positivo = [] #array de los valores calculados para d positivo con la fórmula de KS
    d_negativo = [] #array de los valores calculados para d negativo con la fórmula de KS
    
    for i in range(len(lista)):
        d_positivo.append(i/len(lista) - lista[i]) #Fórmula de KS para d positivo
        d_negativo.append( lista[i]-(i-1)/len(lista)) #Fórmula de KS para d negativo
        
    dmaximo = max(max(d_positivo), max(d_negativo)) #Calculo el máximo
    k_tabla=ksone.ppf(1-alfa/2, len(lista))
    
    if dmaximo < k_tabla:
      return True
    return False
    
=======
    # Calculamos media y varianza del total de corridas

    rv1 = ss.norm()  # Normal estándar
    # tomamos alfa
    alfa = 0.05
    alfa_2 = alfa / 2
    print('\nAlfa:', alfa)
    print('Alfa sobre 2:', alfa_2)
    Za2 = rv1.cdf(alfa_2)  # 1.96 #Z alfa/2
    print('Z alfa sobre 2:', Za2)

    mu = ((2 * n) - 1) / 3
    print('Esperanza:', mu)
    sigma2 = ((16 * n) - 29) / 90
    print('Varianza:', sigma2)
    sigma = math.sqrt(sigma2)
    print('Desvío:', sigma, '\n')

    # Si n > 0, por el TCL, la distribución se aproxima a una normal N(0,1)
    Z0 = rv1.cdf(abs((total_corridas - mu) / sigma))
    print('Z0:', Z0)

    if Z0 < Za2:
        generador_independiente = True
        print('\nNo se puede rechazar la hipótesis de que los datos son independientes')
    else:
        generador_independiente = False
        print('\nSe tiene evidencia de que los datos son dependientes, se rechaza el generador')
    # return generador_independiente
"""


def testRacha(lista):
    subsecuencias_menor_4 = 0
    subsecuencias_mayor_4 = 0
    n = len(lista)
    n1 = 0
    n2 = 0
    for i in range(n - 1):
        cant = 0
        if lista[i] < lista[i + 1]:
            j = i
            while lista[j] < lista[j + 1] and j < n - 2:
                cant += 1
                j += 1
            if cant <= 4:
                subsecuencias_menor_4 += 1
                n1 += cant
            else:
                subsecuencias_mayor_4 += 1
                n2 += cant
            i = j
    print('n1=Cantidad de subsecuencias crecientes de longitud <= 2:', n1)
    print('n2=Cantidad de subsecuencias crecientes de longitud > 2:', n2)
    total_corridas = subsecuencias_menor_4 + \
        subsecuencias_mayor_4  # R= total_corridas
    print('Total de subsecuencias corridas:', total_corridas)

    H0 = "los números generados son aleatoria"
    H1 = "los números generados no son aleatoria"
    print('\nHipótesis 0:', H0)
    print('\nHipótesis 1:', H1)
    if (subsecuencias_menor_4 != 0 and subsecuencias_mayor_4 != 0):
        mu = ((2 * n1 * n2) / (n1 + n2)) + 1
        print('Esperanza:', mu)
        sigma2 = ((2 * n1 * n2) * ((2 * n1 * n2) - n1 - n2)) / \
            (((n1 - n2) ** 2) * (n1 + n2 - 1))
        print('Varianza:', sigma2)
        sigma = math.sqrt(sigma2)
        print('Desvío:', sigma, '\n')

        Z0 = (total_corridas - mu) / sigma
        print('Z0:', Z0)
        Z = -1.9599  # estadistico con un error de 0.05
        # El estadístico de prueba se acerca a una distribución normal si Z0>Z
        if Z0 < Z:
            print(
                '\nNEl estadistico de prueba cae en zona de rechazo, no existe evidencia estadistica para apoyar la aleatoriedad de la muestra')
        else:
            print('\nEl estadistico de prueba cae en zona de aceptacion')
    else:
        print('Se rechaza propuesta numeros generados no aleatorios')
