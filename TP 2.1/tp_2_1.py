from generadores import glc, media_cuadrados, generadorNumpy, generadorNumpy
import matplotlib.pyplot as plt
import scipy
import scipy.stats as ss
from scipy.stats import chisquare
"""
Tests para evaluar uniformidad e independencia de los generadores de números aleatorios
 
Pueden ser:
• Teóricos: los que trabajan con la expresión del generado, para evaluar a los generados si los
números que generaría son uniformes e independientes
• Empíricos: aquellos que trabajan con los números obtenidos del generador para verificar
esas propiedades.
"""
n=10000
numbers = glc(7, 5**15, 3, 2**35, n).generate()
numbersMedia= media_cuadrados(9751, n).generate()
numbersNumpy= generadorNumpy(n)
numbersPython= generadorNumpy(n)
print(numbers)
print(numbersMedia)
print(numbersNumpy)
print(numbersPython)
 
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