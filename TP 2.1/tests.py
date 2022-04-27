from scipy.stats import kstest
import scipy.stats as stats
import numpy as np
from scipy.stats import ksone
from scipy.stats import norm
from math import sqrt



#Parámetros:
#numerosPseudoaleatorios -> lista con números aleatorios
#q -> intervalo de confianza (100 - %confianza)
#df -> grados de libertad
def ChiCuadradoTest(numerosPseudoaleatorios,q,df):
    '''
    '''
    numbers = numerosPseudoaleatorios
    #Frecuencia observada en intervalos definidos (bins)
    #np.histogram() -> Devuelve dos matrices: hist y bin_edges. 
    f_obs = np.histogram(numbers, bins=(0,1,2,3,4,5,6,7,8,9,10))

   #Frecuencia esperada en (bins) intervalos
    f_esp = len(numbers)/10

    #Realizo el cálculo y la sumatoria de la fórmula de chi2
    chi2_list = []
    for i in range(10):
        num = ((f_obs[0][i-1]- f_esp)**2)/f_esp
        chi2_list.append(num)
    # Al final obtengo un número de chi**2
    chi2_num = sum(chi2_list)


    # Este número lo debo comparar en la tabla de contingencia de chi2
    # Si es mayor al valor establecido en la tabla, dado un intervalo de confianza (q) y grados de libertad (df) -> entonces no cumple

    #Creo la tabla de chi2 dados tales parámetros q y df
    chi2_table = stats.chi2.ppf(q=q, df=df)

    if chi2_num < chi2_table:
        resultado = True
    else:
        resultado = False

    return  resultado, chi2_list, chi2_num

