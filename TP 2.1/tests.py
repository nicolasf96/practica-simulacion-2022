from scipy.stats import kstest
import scipy.stats as stats
import numpy as np
from scipy.stats import ksone, norm
from math import sqrt
import matplotlib.pyplot as plt



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
        resultado = True        #Hipotesis se afirma, distribución es uniforme
    else:
        resultado = False       #Hipotesis no se afirma, distribución no es uniforme

    return  resultado, chi2_list, chi2_num

def KolmogorovTest(lista, alfa):
    '''Test de Kolmogorov-Smirnov, compara el cdf(valor crítico) de una distribucion uniforme con el cdf(d) de la muestra(lista) de tamaño n, para el nivel de significancia alfa. Devuelde verdadero si la distribución es uniforme, falso si no lo es.'''
    
    lista.sort()            #Ordeno la lista de menor a mayor
    d_positivo = []         #array de los valores calculados para d positivo con la fórmula de KS
    d_negativo = []         #array de los valores calculados para d negativo con la fórmula de KS
    
    for i in range(len(lista)):
        d_positivo.append(i/len(lista) - lista[i])      #Fórmula de KS para d positivo
        d_negativo.append( lista[i]-(i-1)/len(lista))   #Fórmula de KS para d negativo
        
    dmaximo = max(max(d_positivo), max(d_negativo))     #Calculo el máximo entre los d
    k_tabla=ksone.ppf(1-alfa/2, len(lista))             #Tomo el valor crítico d de la tabla de KS
    
    if dmaximo < k_tabla:                   #Comparo el valor d de la muestra con el valor crítico de la tabla
      return True                           #Hipotesis aceptada, distribucion es uniforme
    return False                            #Hipótesis rechazada, distribucion no es uniforme
    
    
def AutocorrelationTest(lista, m, i, alfa):
    '''Test de Autocorrelacion, no anda.'''
    
    maxEntero = int(((len(lista) - i) / m))-1
    muestra = []
    
    for j in  range(i , i+(maxEntero+1)*m):
        muestra.append(lista[j])
    # muestra = [(lista[j]) for j in range(i , maxEntero)]
    
    for k in range(maxEntero-m):
        suma = (muestra[i+k*m]*muestra[i+(k+1)*m])
    
    rho = ((1/(maxEntero+1)) * suma)-0.25
    sigma = (sqrt(13 * (maxEntero+7))/(12*(maxEntero+1)))
    
    zcompara = rho/sigma
    ztabla= norm.ppf(1-alfa/2)
    
    if -ztabla <= zcompara <= ztabla : 
            return True     
    return False
    

def AutocorrelationTest2(x, n):
    '''Test de Autocorrelacion. Devuelve un gráfico.'''
    
    media_lista = np.mean(x)
    c = lambda k: np.mean([(x[i] - media_lista)*(x[i+k] - media_lista) for i in range(n-k)]) #autocovariance
    r = lambda k: c(k)/c(0)  #Autocorrelation

    correlacion = [r(k) for k in range(100)] 

    plt.plot(correlacion)
    plt.show()
        
    