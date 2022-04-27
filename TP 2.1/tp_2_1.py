from generadores import glc, media_cuadrados, generadorNumpy
import tests
import matplotlib.pyplot as plt


# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m

generatorGLC = glc(64, 15, 12, 87, 1000)
numbersGLC = generatorGLC.generate()

generatorMC = media_cuadrados(9713,1000)
numbersMediaCuadrados = generatorMC.generate()

numbersNumpy = generadorNumpy(1000)

print(numbersGLC)

plt.scatter(numbersNumpy,numbersGLC)
plt.show()

'''
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(numbersNumpy, numbersMediaCuadrados, color='b')
ax.set_xlabel('0 a n')
ax.set_ylabel('0 <= x <= 1')
ax.set_title('Plot')
plt.show()

'''