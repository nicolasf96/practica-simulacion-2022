import numpy as np



# Generador Congruencial Lineal (GCL)
# Forma --> Xsub(n+1) = (a Xsub(n) + c) mod (m)
# Están determinados por los parámetros: * Módulo:  m > 0
# Multiplicador 0 <= a <= m
# Incremento c <= m
# Semilla 0 <= X sub0 <= m
class glc:

    numbers = []
    
    def __init__(self, seed: float, a: float, c: float, m: int, n: int) -> None :
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.n =n


    def generate(self):
        next = self.seed
        for i in range(self.n):
            next= (self.a*next + self.c)%self.m
            self.numbers.append(next/self.m)
        return self.numbers


# Generador Media de los Cuadrados
# Forma --> 
class media_cuadrados:

    numbers=[]

    def __init__(self, seed, n):
        self.seed = seed
        self.n = n

    def generate(self):
        seeds = []
        seeds.append(self.seed)
        for i in range(self.n):
            num=int(str(seeds[i]**2).zfill(8)[2:6])
            seeds.append(num)
            self.numbers.append(seeds**2)
        return self.numbers


# Generador Números Pseudo Aleatorios de Numpy
# Forma --> 
def generadorNumpy(n):
   numbers = []
   for i in range(n):
       numbers.append(np.random.uniform(0, 1))
   return numbers

