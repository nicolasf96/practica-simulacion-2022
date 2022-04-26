from generadores import glc, media_cuadrados, generadorNumpy


# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m
generator = glc(35, 12, 15, 87, 20)

numbers = generator.generate()

print(numbers)
