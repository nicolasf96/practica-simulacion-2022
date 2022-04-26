from generadores import glc, media_cuadrados, generadorNumpy
import tests


# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m

generatorGLC = glc(64, 15, 12, 87, 100)
numbersGLC = generatorGLC.generate()

generatorMC = media_cuadrados(1931,100)
numbersMediaCuadrados = generatorMC.generate()

numbersNumpy = generadorNumpy(100)

print(numbersMediaCuadrados)
