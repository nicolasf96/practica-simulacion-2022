from clases import negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting
from matplotlib import pyplot as plt


def graficoDineroUnicaTirada(dineroTiempo, titulo, dineroInicial):
    plt.title(titulo)
    plt.axhline(dineroInicial, color='k', ls="solid")
    plt.plot(dineroTiempo[0], linewidth=1.2)
    plt.xlabel("(Número de tiradas)")
    plt.ylabel("Capital en el tiempo")
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    # Linea invisible para agregar legend
    plt.axhline(dineroInicial, color='w', ls="solid", visible=False)
    dineroIni = 'Capital inicial: ' + str(dineroInicial)
    dineroFin = (f'Capital Final{dineroTiempo[0]}')
    plt.legend((dineroIni, dineroFin), loc="best")
    plt.ioff()
    plt.show()


def graficoDineroTiradasMultiples(dineroTiempo, titulo, dineroInicial):
    for i in range(c):
        plt.title(titulo)
        plt.axhline(dineroInicial, color='k', ls="solid")
        plt.axhline(dineroInicial * 1.5, color='c', ls="-", linewidth=0.8)
        plt.axhline(dineroInicial * 0.5, color='r', ls="-")
        plt.plot(dineroTiempo[i], linewidth=1.3)
        plt.xlabel("(Número de tiradas)")
        plt.ylabel("Capital en el tiempo")
        # Me ajustan los x e y
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        # Linea invisible para agregar legend
        plt.axhline(dineroInicial, color='w', ls="solid", visible=False)
        dineroIni = 'Capital inicial: ' + str(dineroInicial)
        cincuentamas = ('Ganancia del 50%')
        cincuentamenos = ('Pérdida del 50%:')
        plt.legend((dineroIni, cincuentamas, cincuentamenos), loc="best")
        plt.ioff()
    plt.show()


def graficaFrecFavorable(frecuencias, title1):
    plt.title(title1)
    plt.bar(range(0, len(frecuencias)), frecuencias)
    plt.ylabel('Frec. Relativa de apuesta favorable')
    plt.ylim(0, 1)
    plt.xlabel('n (número de tiradas)')
    plt.show()


def tirada() -> int:
    return randint(0, 36)


# dineroMartinGalaAcotado= [[0 for x in range(t)] for y in range(c)]
# frecRelativasMG = []
# dineroMartinGalaAcotadM= [[0 for x in range(t)] for y in range(c)]


valorApuesta = 50  # Valor de la apuesta
valorApuestaIdeal = valorApuesta * 100
capAcotado = 1000  # Capital acotado
capIdeal = 200000  # Capital ideal

t = 100  # número de tiradas
c = 10  # número de corridas

# Estrategia Martingala
# Tomamos como ganadores a los numeros pares


dineroMartinGalaAcotado = [[0 for x in range(t)] for y in range(c)]
frecRelativasMG = []
dineroMartinGalaAcotadM = [[0 for x in range(t)] for y in range(c)]

dineroguetting = [[0 for x in range(t)] for y in range(c)]
dineroFibonacciIdeal = [[0 for x in range(t)] for y in range(c)]
dineroFibonacciX100Ideal = [[0 for x in range(t)] for y in range(c)]

# graficaFrecFavorable(
#   dineroMartinGalaAcotado[1], "Frecuencia Relativa - Martingala")
#dineroMartinGalaIdeal = martinGala(valorApuestaIdeal, capIdeal, t, c)
# graficoDineroUnicaTirada(dineroMartinGalaIdeal[0],'Estrategia Martingala',capIdeal)
# graficoDineroTiradasMultiples(dineroMartinGalaIdeal[0],'MartinGala - Capital Ideal',capIdeal)

apuesta_minima = 1
j1 = JugadorGuetting(capital=50, apuesta_ini=1)
guetting = []

for i in range(10):
    guetting.append(JugadorGuetting(capital=50, apuesta_ini=1))

resultadosj1 = [j1.capital, ]

for i in range(100):
    n = tirada()
    j1.jugar(n)
    resultadosj1.append(j1.capital)

resultados = []
for jugador in guetting:
    lista = []
    for i in range(100):
        n = tirada()
        jugador.jugar(n)
        lista.append(jugador.capital)
    resultados.append(lista)

# graficoDineroUnicaTirada(dineroTiempo=resultadosj1,
#                        dineroInicial=10E5, titulo="abc")

plt.title("Metodo Guetting- Flujo de dinero respecto a n tiradas")
plt.axhline(50, color='k', ls="solid")
plt.plot(resultadosj1, linewidth=1.2)
plt.xlabel("(Número de tiradas)")
plt.ylabel("Capital en el tiempo")
# Me ajustan los x e y
ax = plt.gca()
ax.relim()
ax.autoscale_view()
# Linea invisible para agregar legend
plt.axhline(50, color='w', ls="solid", visible=False)
dineroIni = 'Capital inicial: ' + str(50)
dineroFin = (f'Capital Final{resultadosj1[-1]}')
plt.legend((dineroIni, dineroFin), loc="best")
plt.ioff()
plt.show()

for i in range(10):
    plt.title(
        "Metodo Guetting- Flujo de dinero de 10 apostadores respecto a n tiradas")
    plt.axhline(50, color='k', ls="solid")
    plt.axhline(50 * 1.5, color='c', ls="-", linewidth=0.8)
    plt.axhline(50 * 0.5, color='r', ls="-")
    plt.plot(resultados[i], linewidth=1.3)
    plt.xlabel("(Número de tiradas)")
    plt.ylabel("Capital en el tiempo")
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    # Linea invisible para agregar legend
    plt.axhline(50, color='w', ls="solid", visible=False)
    dineroIni = 'Capital inicial: ' + str(50)
    cincuentamas = ('Ganancia del 50%')
    cincuentamenos = ('Pérdida del 50%:')
    plt.legend((dineroIni, cincuentamas, cincuentamenos), loc="best")
    plt.ioff()
plt.show()
