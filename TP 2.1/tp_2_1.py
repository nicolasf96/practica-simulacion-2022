from generadores import glc, media_cuadrados, generadorNumpy, generadorNumpy
from tests import ChiCuadradoTest, KolmogorovTest, test_rachas
import matplotlib.pyplot as plt
import scipy
import scipy.stats as ss
from scipy.stats import chisquare


# Definición de variables
# n -> Cantidad de números pseudoaleatorios a generar
n = 10000
seedGLC1 = 2500
seedGLC2 = 2356
seedGLC3 = 6512
seedGLC4 = 6565
seedMedia1 = 2500
seedMedia2 = 3256
seedMedia3 = 5999
seedMedia4 = 7001
numbersGLCC1 = glc(seedGLC1, a=22695477, c=1, m=2**32, n=n).generate()
numbersGLCC2 = glc(seedGLC2, a=22695477, c=1, m=2**32, n=n).generate()
numbersGLCC3 = glc(seedGLC3, a=22695477, c=1, m=2**32, n=n).generate()
numbersGLCC4 = glc(seedGLC4, a=22695477, c=1, m=2**32, n=n).generate()
numbersGLCJava1 = glc(seedGLC1, a=25214903917, c=11, m=2**48-1, n=n).generate()
numbersGLCJava2 = glc(seedGLC2, a=25214903917, c=11, m=2**48-1, n=n).generate()
numbersGLCJava3 = glc(seedGLC3, a=25214903917, c=11, m=2**48-1, n=n).generate()
numbersGLCJava4 = glc(seedGLC4, a=25214903917, c=11, m=2**48-1, n=n).generate()
numbersMedia1 = media_cuadrados(seedMedia1, n=n).generate()
numbersMedia2 = media_cuadrados(seedMedia2, n=n).generate()
numbersMedia3 = media_cuadrados(seedMedia3, n=n).generate()
numbersMedia4 = media_cuadrados(seedMedia4, n=n).generate()
numbersPython1 = generadorNumpy(n)
numbersPython2 = generadorNumpy(n)
numbersPython3 = generadorNumpy(n)
numbersPython4 = generadorNumpy(n)

# Numeros pseudoaleatorios
print('Numeros GLC C')
print(f'Semilla{seedGLC1}')
print(numbersGLCC1)
print(f'Semilla{seedGLC2}')
print(numbersGLCC2)
print(f'Semilla{seedGLC3}')
print(numbersGLCC3)
print(f'Semilla{seedGLC4}')
print(numbersGLCC4)

print('Numeros GLC Java')
print(f'Semilla{seedGLC1}')
print(numbersGLCJava1)
print(f'Semilla{seedGLC2}')
print(numbersGLCJava2)
print(f'Semilla{seedGLC3}')
print(numbersGLCJava3)
print(f'Semilla{seedGLC4}')
print(numbersGLCJava4)

print('Numeros Media')
print(f'Semilla{seedMedia1}')
print(numbersMedia1)
print(f'Semilla{seedMedia2}')
print(numbersMedia2)
print(f'Semilla{seedMedia3}')
print(numbersMedia3)
print(f'Semilla{seedMedia4}')
print(numbersMedia4)

print('Numeros Python')
print(numbersPython1)
print(numbersPython2)
print(numbersPython3)
print(numbersPython4)


# graficos

fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])

# graficos hist GCL con C
axs[0, 0].set_title(f'Histograma GCL con parametros C semilla:{seedGLC1}')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 0].hist(numbersGLCC1,  edgecolor='black')

axs[0, 1].set_title(f'Histograma GCL con parametros C semilla:{seedGLC2}')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 1].hist(numbersGLCC2,  edgecolor='black')

axs[1, 0].set_title(f'Histograma GCL con parametros C semilla:{seedGLC3}')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 0].hist(numbersGLCC3,  edgecolor='black')

axs[1, 1].set_title(f'Histograma GCL con parametros C semilla:{seedGLC4}')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 1].hist(numbersGLCC4,  edgecolor='black')
plt.show()
# graficos dispersion GCL con C
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC1}')
axs[0, 0].scatter(range(n), numbersGLCC1, c="black", s=1)
axs[0, 1].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC2}')
axs[0, 1].scatter(range(n), numbersGLCC2, c="black", s=1)
axs[1, 0].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC3}')
axs[1, 0].scatter(range(n), numbersGLCC3, c="black", s=1)
axs[1, 1].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC4}')
axs[1, 1].scatter(range(n), numbersGLCC4, c="black", s=1)

plt.show()

# graficos hist GCL con Java
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(f'Histograma GCL con parametros Java semilla:{seedGLC1}')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 0].hist(numbersGLCJava1,  edgecolor='black')

axs[0, 1].set_title(f'Histograma GCL con parametros Java semilla:{seedGLC2}')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 1].hist(numbersGLCJava2,  edgecolor='black')

axs[1, 0].set_title(f'Histograma GCL con parametros Java semilla:{seedGLC3}')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 0].hist(numbersGLCJava3,  edgecolor='black')

axs[1, 1].set_title(f'Histograma GCL con parametros Java semilla:{seedGLC4}')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 1].hist(numbersGLCJava4,  edgecolor='black')
plt.show()

# graficos dispersion GCL con Java
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC1}')
axs[0, 0].scatter(range(n), numbersGLCJava1, c="black", s=1)
axs[0, 1].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC2}')
axs[0, 1].scatter(range(n), numbersGLCJava2, c="black", s=1)
axs[1, 0].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC3}')
axs[1, 0].scatter(range(n), numbersGLCJava3, c="black", s=1)
axs[1, 1].set_title(
    f'Diagrama de dispersion numeros GLC C con semilla: {seedGLC4}')
axs[1, 1].scatter(range(n), numbersGLCJava4, c="black", s=1)
plt.show()

# graficos Media
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(f'Histograma Media Cuadrado con semilla:{seedMedia1}')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 0].hist(numbersMedia1, edgecolor='black')

axs[0, 1].set_title(f'Histograma Media Cuadrado con semilla:{seedMedia2}')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 1].hist(numbersMedia2, edgecolor='black')

axs[1, 0].set_title(f'Histograma Media Cuadrado con semilla:{seedMedia3}')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 0].hist(numbersMedia3, edgecolor='black')

axs[1, 1].set_title(f'Histograma Media Cuadrado con semilla:{seedMedia4}')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 1].hist(numbersMedia4, edgecolor='black')
plt.show()

# graficos dispersion Media

fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(
    f'Diagrama de dispersion numeros Media con semilla: {seedMedia1}')
axs[0, 0].scatter(range(n), numbersMedia1, c="black", s=1)
axs[0, 1].set_title(
    f'Diagrama de dispersion numeros Media con semilla: {seedMedia2}')
axs[0, 1].scatter(range(n), numbersMedia2, c="black", s=1)
axs[1, 0].set_title(
    f'Diagrama de dispersion numeros Media con semilla: {seedMedia3}')
axs[1, 0].scatter(range(n), numbersMedia3, c="black", s=1)
axs[1, 1].set_title(
    f'Diagrama de dispersion numeros Media con semilla: {seedMedia4}')
axs[1, 1].scatter(range(n), numbersMedia4, c="black", s=1)
plt.show()

# graficos Python
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title('Histograma Python')
axs[0, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 0].hist(numbersPython1, edgecolor='black')

axs[0, 1].set_title('Histograma Python')
axs[0, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[0, 1].hist(numbersPython2, edgecolor='black')

axs[1, 0].set_title('Histograma Python')
axs[1, 0].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 0].hist(numbersPython3, edgecolor='black')

axs[1, 1].set_title('Histograma Python')
axs[1, 1].set(xlabel='numeros', ylabel='Frecuencia Absoluta')
axs[1, 1].hist(numbersPython4, edgecolor='black')

plt.show()


# graficos dispersion python

fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[11, 8])
axs[0, 0].set_title(f'Diagrama de dispersion Python')
axs[0, 0].scatter(range(n), numbersPython1, c="black", s=1)
axs[0, 1].set_title(f'Diagrama de dispersion Python')
axs[0, 1].scatter(range(n), numbersPython2, c="black", s=1)
axs[1, 0].set_title(f'Diagrama de dispersion Python')
axs[1, 0].scatter(range(n), numbersPython3, c="black", s=1)
axs[1, 1].set_title(f'Diagrama de dispersion Python')
axs[1, 1].scatter(range(n), numbersPython4, c="black", s=1)
plt.show()


# Prueba de test

# Tests Chi cuadrado
print('test chi cuadrado')
print('Resultados NumerosGLC')
print(ChiCuadradoTest(numbersGLCC1, 0.95, 9))
print(ChiCuadradoTest(numbersGLCC2, 0.95, 9))
print(ChiCuadradoTest(numbersGLCC3, 0.95, 9))
print(ChiCuadradoTest(numbersGLCC4, 0.95, 9))

print('Resultados NumerosMedia')
print(ChiCuadradoTest(numbersMedia1, 0.95, 9))
print(ChiCuadradoTest(numbersMedia2, 0.95, 9))
print(ChiCuadradoTest(numbersMedia3, 0.95, 9))
print(ChiCuadradoTest(numbersMedia4, 0.95, 9))

print('Resultados Numeros Python')
print(ChiCuadradoTest(numbersPython1, 0.95, 9))
print(ChiCuadradoTest(numbersPython2, 0.95, 9))
print(ChiCuadradoTest(numbersPython3, 0.95, 9))
print(ChiCuadradoTest(numbersPython4, 0.95, 9))


# Test de racha
print('test de racha')
print('Resultados NumerosGLCC')
print(f'semilla: {seedGLC1}')
test_rachas(numbersGLCC1)
print(f'semilla: {seedGLC2}')
test_rachas(numbersGLCC2)
print(f'semilla: {seedGLC3}')
test_rachas(numbersGLCC3)
print(f'semilla: {seedGLC3}')
test_rachas(numbersGLCC4)

print('Resultados NumerosJava')
print(f'semilla: {seedGLC1}')
test_rachas(numbersGLCJava1)
print(f'semilla: {seedGLC2}')
test_rachas(numbersGLCJava2)
print(f'semilla: {seedGLC3}')
test_rachas(numbersGLCJava3)
print(f'semilla: {seedGLC3}')
test_rachas(numbersGLCJava4)

print('Resultados NumerosMedia')
print(f'semilla: {seedMedia1}')
test_rachas(numbersMedia1)
print(f'semilla: {seedMedia2}')
test_rachas(numbersMedia2)
print(f'semilla: {seedMedia3}')
test_rachas(numbersMedia3)
print(f'semilla: {seedMedia4}')
test_rachas(numbersMedia4)

print('Resultados Numeros Python')
print(f'test de racha Python 1')
test_rachas(numbersPython1)
print(f'test de racha Python 2')
test_rachas(numbersPython2)
print(f'test de racha Python 3')
test_rachas(numbersPython3)
print(f'test de racha Python 4')
test_rachas(numbersPython4)

# Test KS
print('Test KS GLC')
print(f' semilla:{seedGLC1}'+KolmogorovTest(numbersGLCC1, 0.05))
print(f' semilla:{seedGLC2}'+KolmogorovTest(numbersGLCC2, 0.05))
print(f' semilla:{seedGLC3}'+KolmogorovTest(numbersGLCC3, 0.05))
print(f' semilla:{seedGLC4}'+KolmogorovTest(numbersGLCC4, 0.05))
print('Test KS java')
print(f' semilla:{seedGLC1}'+KolmogorovTest(numbersGLCJava1, 0.05))
print(f' semilla:{seedGLC2}'+KolmogorovTest(numbersGLCJava2, 0.05))
print(f' semilla:{seedGLC3}'+KolmogorovTest(numbersGLCJava3, 0.05))
print(f' semilla:{seedGLC4}'+KolmogorovTest(numbersGLCJava4, 0.05))
print('Test KS media')
print(f' semilla:{seedMedia1}'+KolmogorovTest(numbersMedia1, 0.05))
print(f' semilla:{seedMedia2}'+KolmogorovTest(numbersMedia2, 0.05))
print(f' semilla:{seedMedia3}'+KolmogorovTest(numbersMedia3, 0.05))
print(f' semilla:{seedMedia4}'+KolmogorovTest(numbersMedia4, 0.05))
print('Test KS media')
print(f'numbersPython1'+KolmogorovTest(numbersPython1, 0.05))
print(f'numbersPython2'+KolmogorovTest(numbersPython2, 0.05))
print(f'numbersPython3'+KolmogorovTest(numbersPython3, 0.05))
print(f'numbersPython4'+KolmogorovTest(numbersPython4, 0.05))
