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
            self.numbers.append(next)
        return self.numbers





