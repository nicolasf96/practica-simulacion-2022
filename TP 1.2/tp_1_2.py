from clases import negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting
from matplotlib import pyplot as plt


def graficoDineroUnicaTirada(resultados, capAcotado):
    plt.title("Metodo Guetting- Flujo de dinero respecto a n tiradas")
    plt.axhline(capAcotado, color='k', ls="solid")
    plt.plot(resultados, linewidth=1.2)
    plt.xlabel("(Número de tiradas)")
    plt.ylabel("Capital en el tiempo")
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    # Linea invisible para agregar legend
    plt.axhline(50, color='w', ls="solid", visible=False)
    dineroIni = 'Capital inicial: ' + str(capAcotado)
    dineroFin = (f'Capital Final{resultados[-1]}')
    plt.legend((dineroIni, dineroFin), loc="best")
    plt.ioff()
    plt.show()


def graficoDineroTiradasMultiples(resultados, capAcotado, corridas):
    for i in range(corridas):
        plt.title(f"Metodo Guetting- Flujo de dinero de {corridas} apostadores respecto a n tiradas")
        plt.axhline(capAcotado, color='k', ls="solid")
        plt.axhline(capAcotado * 1.5, color='c', ls="-", linewidth=0.8)
        plt.axhline(capAcotado * 0.5, color='r', ls="-")
        plt.plot(resultados[i], linewidth=1.3)
        plt.xlabel("(Número de tiradas)")
        plt.ylabel("Capital en el tiempo")
        # Me ajustan los x e y
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        # Linea invisible para agregar legend
        plt.axhline(capAcotado, color='w', ls="solid", visible=False)
        dineroIni = 'Capital inicial: ' + str(capAcotado)
        cincuentamas = ('Ganancia del 50%')
        cincuentamenos = ('Pérdida del 50%:')
        plt.legend((dineroIni, cincuentamas, cincuentamenos), loc="best")
        plt.ioff()
    plt.show()


def graficaFrecFavorable(frecuencias, title1):
    plt.title(title1)
    plt.bar(range(0, len(frecuencias)), frecuencias)
    plt.ylabel('Número de Jugadores')
    plt.ylim(0, 100)
    plt.xlabel('n (número de victorias)')
    plt.show()


def tirada() -> int:
    return randint(0, 36)


valorApuesta = 50  # Valor de la apuesta
valorApuestaIdeal = valorApuesta * 100
capAcotado = 1000  # Capital acotado
capIdeal = 200000  # Capital ideal

t = 100  # número de tiradas
c = 10  # número de corridas



dineroMartinGalaAcotado = [[0 for x in range(t)] for y in range(c)]
frecRelativasMG = []
dineroMartinGalaAcotadM = [[0 for x in range(t)] for y in range(c)]

dineroguetting = [[0 for x in range(t)] for y in range(c)]
dineroFibonacciIdeal = [[0 for x in range(t)] for y in range(c)]
dineroFibonacciX100Ideal = [[0 for x in range(t)] for y in range(c)]


apuesta_minima = 1
j1 = JugadorGuetting(capital=50, apuesta_ini=1)
guetting = []

for i in range(100):
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



vic = [0 for i in range(100)]

for jugador in guetting:
    vic[jugador.victorias-1]+=1

graficaFrecFavorable(vic,"Frecuencia Relativa - Guetting")

graficoDineroUnicaTirada(resultadosj1, capAcotado)

graficoDineroTiradasMultiples(resultados, capAcotado, 100)