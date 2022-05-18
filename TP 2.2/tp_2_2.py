import math

import numpy as np
from generadores import Distribuciones
from tests import ChiCuadradoTest, KolmogorovTest, test_autocorrelacion, test_rachas
import matplotlib.pyplot as plt



n = 10000
#numeros generados
numbersUniforme=Distribuciones().generador_uniforme(a=0,b=1,n=n)
numbersExponencial=Distribuciones().generador_exponencial(l=1.5,n=n)

print(numbersUniforme)
print(numbersExponencial)
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



plt.show()



#Test
print('Test chi cuadrado')
print('Resultado numbersUniforme')
print(ChiCuadradoTest(numbersUniforme, 0.95, 9))
print('Resultado numbersExponencial')
print(ChiCuadradoTest(numbersExponencial, 0.95, 9))
