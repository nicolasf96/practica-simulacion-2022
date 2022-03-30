from clases import negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting
import matplotlib as plt


def graficoDineroUnicaTirada(dineroTiempo, titulo,dineroInicial):
    plt.title(titulo)
    plt.axhline(dineroInicial, color='k', ls="solid")
    plt.plot(dineroTiempo[0], linewidth=1.2)
    plt.xlabel("(Número de tiradas)")
    plt.ylabel("Capital en el tiempo")
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    plt.axhline(dineroInicial,color='w', ls="solid",visible=False) #Linea invisible para agregar legend
    dineroIni = 'Capital inicial: ' + str(dineroInicial)
    dineroFin=('Capital Final: ' + str(dineroTiempo[0][t-1]))
    plt.legend((dineroIni,dineroFin), loc="best")
    plt.ioff()
    plt.show()


def graficoDineroTiradasMultiples(dineroTiempo, titulo,dineroInicial):
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
        plt.axhline(dineroInicial,color='w', ls="solid",visible=False) #Linea invisible para agregar legend
        dineroIni = 'Capital inicial: ' + str(dineroInicial)
        cincuentamas =('Ganancia del 50%')
        cincuentamenos = ('Pérdida del 50%:')
        plt.legend((dineroIni,cincuentamas,cincuentamenos), loc="best")
        plt.ioff()
    plt.show()

def graficaFrecFavorable(frecuencias, title):
    plt.title(title)
    plt.bar(range(0,len(frecuencias)),frecuencias)
    plt.ylabel('Frec. Relativa de apuesta favorable')
    plt.ylim(0, 1)
    plt.xlabel('n (número de tiradas)')
    plt.show()


def tirada() -> int:
    return randint(0, 36)




# dineroMartinGalaAcotado= [[0 for x in range(t)] for y in range(c)]
# frecRelativasMG = []
# dineroMartinGalaAcotadM= [[0 for x in range(t)] for y in range(c)]


# graficoDineroUnicaTirada(dineroMartinGalaIdeal[0],'Estrategia Martingala',capIdeal)
# graficoDineroTiradasMultiples(dineroMartinGalaIdeal[0],'MartinGala - Capital Ideal',capIdeal)