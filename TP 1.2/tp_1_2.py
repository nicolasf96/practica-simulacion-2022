from clases import Jugador, JugadorFibonacci, negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting, JugadorColumnas
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def graficoDineroUnicaTirada(resultados: list, capAcotado: float, metodo: str) -> None:
    plt.title(
        f"Flujo de dinero de una corrida en 'n' tiradas-{metodo}", fontsize=25)
    plt.axhline(capAcotado, color='k', ls="solid")
    plt.plot(resultados, linewidth=1.2)
    plt.xlabel("Número de tiradas 'n'", fontsize=25)
    plt.ylabel("Capital en 'n' tiradas", fontsize=25)
    # Me ajustan los x e y
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()
    # Linea invisible para agregar legend
    plt.axhline(50, color='w', ls="solid", visible=False)
    dineroIni = 'Capital inicial: ' + str(capAcotado)
    dineroFin = (f'Capital Final{resultados[-1]}')
    plt.legend((dineroIni, dineroFin), loc="best", prop={'size': 25})
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.ioff()
    plt.show()


def graficoDineroTiradasMultiples(resultados: list, capAcotado: float, corridas: int, metodo: str) -> None:
    for i in range(corridas):
        plt.title(
            f"Flujo de dinero de {corridas} corridas respecto a 'n' tiradas-{metodo}", fontsize=25)
        plt.axhline(capAcotado, color='k', ls="solid")
        plt.axhline(capAcotado * 1.5, color='c', ls="-", linewidth=0.8)
        plt.axhline(capAcotado * 0.5, color='r', ls="-")
        plt.plot(resultados[i], linewidth=1.3)
        plt.xlabel("Número de tiradas 'n'", fontsize=25)
        plt.ylabel("Capital en 'n' tiradas", fontsize=25)
        # Me ajustan los x e y
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        # Linea invisible para agregar legend
        plt.axhline(capAcotado, color='w', ls="solid", visible=False)
        dineroIni = 'Capital inicial: ' + str(capAcotado)
        cincuentamas = ('Ganancia del 50%')
        cincuentamenos = ('Pérdida del 50%:')
        plt.legend((dineroIni, cincuentamas, cincuentamenos),
                   loc="best", prop={'size': 25})
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        #plt.legend((dineroIni,), loc="best")
        plt.ioff()
    plt.show()


def graficaFrecFavorable(frecuencias: list, title1: str) -> None:
    plt.title(f"Frecuencia relativa de obtener una apuesta favorable segun 'n'- {title1}", fontsize=25)
    plt.bar(range(0, len(frecuencias)), frecuencias)
    plt.ylabel('Frecuencia relativa', fontsize=25)
    plt.ylim(0, 1)
    plt.xlabel('Cantidad de tiradas "n"', fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()


def tirada() -> int:
    return randint(0, 36)


valorApuesta = 10  # Valor de la apuesta
valorApuestaIdeal = valorApuesta * 100
capAcotado = 1000  # Capital acotado
capIdeal = 200000  # Capital ideal

t = 100  # número de tiradas
c = 10  # número de corridas


def ejecutar(clase: Jugador, metodo: str, capital_acotado: bool = False):
    """Genera todas las graficas
    Se puede indicar si el capital es acotado o no, por defecto no es acotado
    lo que significa que el jugador puede asumir perdidas"""
    apuesta_minima = 1

    j1 = clase(capital=1000, apuesta_ini=10, cap_acotado=capital_acotado)
    listado_jugadores = []

    for i in range(100):
        listado_jugadores.append(
            clase(capital=1000, apuesta_ini=10, cap_acotado=capital_acotado))
    vic = [0 for i in range(100)]
    resultadosj1 = [j1.capital, ]
    ultima_vic = 0
    for i in range(100):
        n = tirada()
        #victorias_antes = j1.victorias
        j1.jugar(n)
        #vict_n = j1.victorias-victorias_antes
        # if vict_n >= 1:
        #    vic[(i+1)-ultima_vic] += 1
        #    ultima_vic = i+1
        resultadosj1.append(j1.capital)
    # for i in range(len(vic)-1):
    #    vic[i]/=100
    resultados = []

    for jugador in listado_jugadores:
        lista = []
        ultima_victoria = 0
        for i in range(100):
            n = tirada()
            victorias_antes = jugador.victorias
            jugador.jugar(n)
            victoria_n = jugador.victorias-victorias_antes
            if victoria_n >= 1:
                vic[i-ultima_victoria] += 1
                ultima_victoria = i+1
            lista.append(jugador.capital)
        resultados.append(lista)
    for i in range(100):
        vic[i] /= (100**2)
    """vic = [0 for i in range(100)]

    for jugador in listado_jugadores:
        vic[jugador.victorias-1] += 1"""

    graficaFrecFavorable(vic, metodo)
    graficoDineroUnicaTirada(resultadosj1, capAcotado, metodo)
    graficoDineroTiradasMultiples(resultados, capAcotado, 100, metodo)


ejecutar(clase=JugadorMG, metodo="Sin restricciones de capital",capital_acotado=False)
ejecutar(clase=JugadorMG, metodo="Con capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorFibonacci, metodo="Sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorFibonacci, metodo="Con capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorGuetting, metodo="Sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorGuetting, metodo="Con capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorColumnas, metodo="Sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorColumnas, metodo="Con capital acotado", capital_acotado=True)
