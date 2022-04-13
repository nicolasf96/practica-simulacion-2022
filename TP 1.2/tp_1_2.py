from clases import Jugador, JugadorFibonacci, negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting, JugadorColumnas
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def graficoDineroUnicaTirada(resultados: list, capAcotado: float, metodo: str) -> None:
    plt.title(f"{metodo}- Flujo de dinero respecto a n tiradas")
    plt.axhline(capAcotado, color='k', ls="solid")
    plt.plot(resultados, linewidth=1.2)
    plt.xlabel("Número de tiradas 'n'")
    plt.ylabel("Capital en 'n' tiradas")
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


def graficoDineroTiradasMultiples(resultados: list, capAcotado: float, corridas: int, metodo: str) -> None:
    for i in range(corridas):
        plt.title(
            f"{metodo}- Flujo de dinero de {corridas} apostadores respecto a n tiradas")
        plt.axhline(capAcotado, color='k', ls="solid")
        #plt.axhline(capAcotado * 1.5, color='c', ls="-", linewidth=0.8)
        #plt.axhline(capAcotado * 0.5, color='r', ls="-")
        plt.plot(resultados[i], linewidth=1.3)
        plt.xlabel("Número de tiradas 'n'")
        plt.ylabel("Capital en 'n' tiradas")
        # Me ajustan los x e y
        ax = plt.gca()
        ax.relim()
        ax.autoscale_view()
        # Linea invisible para agregar legend
        plt.axhline(capAcotado, color='w', ls="solid", visible=False)
        dineroIni = 'Capital inicial: ' + str(capAcotado)
        #cincuentamas = ('Ganancia del 50%')
        #cincuentamenos = ('Pérdida del 50%:')
        #plt.legend((dineroIni, cincuentamas, cincuentamenos), loc="best")
        plt.legend((dineroIni,), loc="best")
        plt.ioff()
    plt.show()


def graficaFrecFavorable(frecuencias: list, title1: str) -> None:
    plt.title(f"Frecuencia relativa- {title1}")
    plt.bar(range(0, len(frecuencias)), frecuencias)
    plt.ylabel('Número de Jugadores')
    plt.ylim(0, 100)
    plt.xlabel('n (número de victorias)')
    plt.show()


def tirada() -> int:
    return randint(0, 36)


valorApuesta = 50  # Valor de la apuesta
valorApuestaIdeal = valorApuesta * 100
capAcotado = 50  # Capital acotado
capIdeal = 200000  # Capital ideal

t = 100  # número de tiradas
c = 10  # número de corridas


def ejecutar(clase: Jugador, metodo: str, capital_acotado: bool = False):
    """Genera todas las graficas
    Se puede indicar si el capital es acotado o no, por defecto no es acotado
    lo que significa que el jugador puede asumir perdidas"""
    apuesta_minima = 1

    j1 = clase(capital=50, apuesta_ini=1, cap_acotado=capital_acotado)
    listado_jugadores = []

    for i in range(100):
        listado_jugadores.append(
            clase(capital=50, apuesta_ini=1, cap_acotado=capital_acotado))

    resultadosj1 = [j1.capital, ]

    for i in range(100):
        n = tirada()
        j1.jugar(n)
        resultadosj1.append(j1.capital)

    resultados = []
    for jugador in listado_jugadores:
        lista = []
        for i in range(100):
            n = tirada()
            jugador.jugar(n)
            lista.append(jugador.capital)
        resultados.append(lista)

    vic = [0 for i in range(100)]

    for jugador in listado_jugadores:
        vic[jugador.victorias-1] += 1

    graficaFrecFavorable(vic, metodo)
    graficoDineroUnicaTirada(resultadosj1, capAcotado, metodo)
    graficoDineroTiradasMultiples(resultados, capAcotado, 100, metodo)


#ejecutar(clase=JugadorMG, metodo="Metodo Martin Gala sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorMG, metodo="Metodo Martin Gala c/capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorParoli, metodo="Metodo de Paroli sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorParoli, metodo="Metodo de Paroli c/capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorFibonacci, metodo="Metodo basado en Fibonacci sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorFibonacci, metodo="Metodo basado en Fibonacci c/capital acotado", capital_acotado=True)

#ejecutar(clase=JugadorGuetting, metodo="Metodo de Guetting sin restricciones de capital", capital_acotado=False)
#ejecutar(clase=JugadorGuetting, metodo="Metodo de Guetting c/capital acotado", capital_acotado=True)

ejecutar(clase=JugadorColumnas, metodo="Metodo de columnas sin restricciones de capital", capital_acotado=False)
ejecutar(clase=JugadorColumnas, metodo="Metodo de columnas c/capital acotado", capital_acotado=True)
