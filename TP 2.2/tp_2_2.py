import math

import numpy as np
from generadores import Distribuciones
from tests import ChiCuadradoTest, KolmogorovTest, test_autocorrelacion, test_rachas
import matplotlib.pyplot as plt



n = 10000
#numeros generados
numbersUniforme=Distribuciones().generador_uniforme(a=0,b=1,n=n)
numbersExponencial=Distribuciones().generador_exponencial(l=3,n=n)
numbersNormal=Distribuciones().generador_normal(media=8, desv=0.25, K=95, n=n)
numbersGamma=Distribuciones().generador_gamma(k=3,alpha=0.4,n=n)

print(numbersUniforme)
print(numbersExponencial)
print(numbersNormal)
print(numbersGamma)
#graficos
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])

# graficos hist GCL con C
axs[0, 0].set_title(f'Histograma de numeros uniforme')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 0].hist(numbersUniforme, bins=round(math.sqrt(len(numbersUniforme))),   edgecolor='black')

axs[0, 1].set_title(f'Histograma de numeros exponenciales')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 1].hist(numbersExponencial, bins=round(math.sqrt(len(numbersExponencial))),  edgecolor='black')

axs[1, 0].set_title(f'Histograma de numeros normal')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 0].hist(numbersNormal, bins=round(math.sqrt(len(numbersNormal))),  edgecolor='black')

axs[1, 1].set_title(f'Histograma de numeros gamma')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 1].hist(numbersGamma, bins=round(math.sqrt(len(numbersGamma))),  edgecolor='black')


plt.show()



#Test
print('Test chi cuadrado')
print('Resultado numbersUniforme')
print(ChiCuadradoTest(numbersUniforme, 0.95, 9))
print('Resultado numbersExponencial')
print(ChiCuadradoTest(numbersExponencial, 0.95, 9))
print('Resultado numbersNormal')
print(ChiCuadradoTest(numbersNormal, 0.95, 9))
print('Resultado numbersGamma')
print(ChiCuadradoTest(numbersGamma, 0.95, 9))
