from generadores import glc, media_cuadrados, generadorNumpy, generadorNumpy
from tests import ChiCuadradoTest
import matplotlib.pyplot as plt
import scipy
import scipy.stats as ss
from scipy.stats import chisquare



#Definición de variables
# n -> Cantidad de números pseudoaleatorios a generar
n=10000
numbersGLC = glc(1234, 134775813, 1, 2**32, n).generate()
numbersMedia= media_cuadrados(9751, n).generate()
numbersPython= generadorNumpy(n)
print(numbersGLC)
print(numbersMedia)
print(numbersPython)

#Tests
result_chi2_glc = ChiCuadradoTest(numbersGLC, 0.95, 9)
print(result_chi2_glc)



'''
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])
 
 
axs[0, 0].set_title('Histograma GCL')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
frec_absoluta,x,c= axs[0, 0].hist(numbers,  edgecolor='black')
print('Frecuencia absoluta intervalos:',frec_absoluta)
k= len(frec_absoluta)
print('Cantidad intervalos: ', k)
frec_esp = []
for i in range(k):
    frec_esp.append(n/k)
print('Valor chi cuadrado de la muestra GCL:',chisquare(frec_absoluta, f_exp = frec_esp))
#Si existe concordancia perfecta entre las frecuencias observadas y las esperadas el
#estadístico tomará un valor igual a 0; por el contrario, si existe una gran discrepancias
#entre estas frecuencias el estadístico tomará un valor grande y, en consecuencia,
#se rechazará la hipótesis nula
 
axs[0, 1].set_title('Histograma Media Cuadrado')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
frec_absoluta,x,c=axs[0, 1].hist(numbersMedia, edgecolor='black')
print('Frecuencia absoluta intervalos:',frec_absoluta)
k= len(frec_absoluta)
print('Cantidad intervalos: ', k)
frec_esp = []
for i in range(k):
    frec_esp.append(n/k)
print('Valor chi cuadrado de la muestra Media Cuadrado:',chisquare(frec_absoluta, f_exp = frec_esp))
 
axs[1, 0].set_title('Histograma Numpy')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
frec_absoluta,x,c=axs[1, 0].hist(numbersNumpy, edgecolor='black')
print('Frecuencia absoluta intervalos:',frec_absoluta)
k= len(frec_absoluta)
print('Cantidad intervalos: ', k)
frec_esp = []
for i in range(k):
    frec_esp.append(n/k)
print('Valor chi cuadrado de la muestra Numpy:',chisquare(frec_absoluta, f_exp = frec_esp))
 
axs[1, 1].set_title('Histograma Python')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
frec_absoluta,x,c=axs[1, 1].hist(numbersPython, edgecolor='black')
print('Frecuencia absoluta intervalos:',frec_absoluta)
k= len(frec_absoluta)
print('Cantidad intervalos: ', k)
frec_esp = []
for i in range(k):
    frec_esp.append(n/k)
print('Valor chi cuadrado de la muestra Python:',chisquare(frec_absoluta, f_exp = frec_esp))
 
plt.show()
'''
 