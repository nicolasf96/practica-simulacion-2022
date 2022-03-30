import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

#TP 1.2 Simulación de Una Ruleta
#Datos

def frecuenciaR(nro,cont):
    frecuenciaA = 0
    if nro % 2 == 0:
        frecuenciaA+= 1
    freqRel= frecuenciaA/cont
    return freqRel

frecuencia = 1/37

valorApuesta = 50 #Valor de la apuesta
valorApuestaIdeal = valorApuesta * 100
capAcotado = 1000 #Capital acotado
capIdeal = 200000 #Capital ideal

t = 100 #número de tiradas
c = 10 #número de corridas

#Estrategia Martingala
#Tomamos como ganadores a los numeros pares


dineroMartinGalaAcotado= [[0 for x in range(t)] for y in range(c)]
frecRelativasMG = []
dineroMartinGalaAcotadM= [[0 for x in range(t)] for y in range(c)]

dineroFibonacciAcotado= [[0 for x in range(t)] for y in range(c)]
frecRelativasFB = []
dineroFibonacciAcotadoM= [[0 for x in range(t)] for y in range(c)]

dineroFibonacciX100Acotado= [[0 for x in range(t)] for y in range(c)]
frecRelativasFBx100 = []
dineroFibonacciX100AcotadoM= [[0 for x in range(t)] for y in range(c)]



dineroMartinGalaIdeal= [[0 for x in range(t)] for y in range(c)]
dineroFibonacciIdeal= [[0 for x in range(t)] for y in range(c)]
dineroFibonacciX100Ideal= [[0 for x in range(t)] for y in range(c)]



def martinGala(apuestaInicial,capital, tiradas, corridas):
    dineroLista = [[0 for x in range(t)] for y in range(c)]
    apuesta= apuestaInicial
    for i in range(0, corridas):
        numeros= np.random.randint(0, 37, tiradas)
        print(numeros)
        dineroJugador= capital
        h = 1  # contador
        cont = 0
        contFrecuencias = 0
        for n in range(0, tiradas):
            if dineroJugador >= (apuesta*h):
                if numeros[n] % 2 != 0:
                    dineroJugador = dineroJugador - (apuesta * h)
                    h = h * 2
                else:
                    dineroJugador = dineroJugador + (apuesta * h)
                    h = 1
                    contFrecuencias = contFrecuencias + 1
                cont= cont + 1
            if corridas == 1 : frecRelativasMG.append(contFrecuencias/cont)
            if h > 16: h = 1
            dineroLista[i][n] = dineroJugador
            print(dineroLista[i][n])
    return dineroLista, frecRelativasMG


def fib(n):
    fibo = []
    a, b = 0,1
    fibo.extend([a,b])
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        fibo.extend([a,b])
    return fibo

def fibonacci(capital, tiradas, corridas):
    dineroLista = [[0 for x in range(t)] for y in range(c)]
    sucFibo = fib(1000)
    for i in range(0, corridas):
        numeros= np.random.randint(0, 37, tiradas)
        print(numeros)
        dineroJugador= capital
        cont = 0
        cont2 = 0
        contFrecuencias= 0
        apuesta = sucFibo[cont]
        for n in range(0, tiradas):
            if dineroJugador >= apuesta:
                if numeros[n] % 2 != 0 :
                    dineroJugador = dineroJugador - apuesta
                    cont = cont + 1
                else:
                    dineroJugador = dineroJugador + apuesta
                    if cont >= 2:
                        cont = cont - 2
                    else:
                        cont = 1
                    contFrecuencias = contFrecuencias + 1
                cont2 = cont2 + 1
                apuesta = sucFibo[cont]
            if corridas == 1: frecRelativasFB.append(contFrecuencias / cont2)
            dineroLista[i][n] = dineroJugador
            print(dineroLista[i][n])
    return dineroLista, frecRelativasFB

def fibonacciX100(capital, tiradas, corridas):
    dineroLista = [[0 for x in range(t)] for y in range(c)]
    sucFibo = fib(1000)
    for i in range(0, corridas):
        numeros= np.random.randint(0, 37, t)
        print(numeros)
        dineroJugador= capital
        cont = 0
        cont2=0
        contFrecuencias = 0
        apuesta = sucFibo[cont] * 100
        for n in range(0, tiradas):
            if dineroJugador >= apuesta:
                if numeros[n] % 2 != 0:
                    dineroJugador = dineroJugador - apuesta
                    cont = cont + 1
                else:
                    dineroJugador = dineroJugador + apuesta
                    if cont >= 2:
                        cont = cont - 2
                    else:
                        cont = 1
                    contFrecuencias = contFrecuencias + 1
                cont2 = cont2 + 1
                apuesta = sucFibo[cont]  * 100
            if corridas == 1: frecRelativasFBx100.append(contFrecuencias / cont2)
            dineroLista[i][n] = dineroJugador
            print(dineroLista[i][n])
    return dineroLista, frecRelativasFBx100

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


# MARTINGALA  -  1 CORRIDA
dineroMartinGalaAcotado = martinGala(valorApuesta,capAcotado,t,1)
graficaFrecFavorable(dineroMartinGalaAcotado[1],"Frecuencia Relativa - Martingala")


# FIBONACCI - 1 Corrida
dineroFibonacciAcotado = fibonacci(capAcotado,t,1)
graficaFrecFavorable(dineroFibonacciAcotado[1],"Frecuencia Relativa - Fibonacci")


# FIBONACCI x 100 - 1 Corrida
dineroFibonacciX100Acotado = fibonacciX100(capAcotado,t,1)
graficaFrecFavorable(dineroFibonacciX100Acotado[1],"Frecuencia Relativa - Fibonacci x 100")


graficoDineroUnicaTirada(dineroMartinGalaAcotado[0],'Estrategia Martingala - Cap. Acotado',capAcotado)

graficoDineroUnicaTirada(dineroFibonacciAcotado[0],'Estrategia Fibonacci - Cap. Acotado',capAcotado)

graficoDineroUnicaTirada(dineroFibonacciX100Acotado[0],'Estrategia Fibonacci x 100 - Cap. Acotado',capAcotado)


# MARTINGALA  -  Múltiples Corridas
dineroMartinGalaAcotadoM = martinGala(valorApuesta,capAcotado,t,c)


# FIBONACCI - Múltiples Corridas
dineroFibonacciAcotadoM = fibonacci(capAcotado,t,c)


# FIBONACCI x 100 - Múltiples Corridas
dineroFibonacciX100AcotadoM = fibonacciX100(capAcotado,t,c)


graficoDineroTiradasMultiples(dineroMartinGalaAcotadoM[0],'MartinGala - Capital Acotado',capAcotado)

graficoDineroTiradasMultiples(dineroFibonacciAcotadoM[0],'Fibonacci - Capital Acotado',capAcotado)

graficoDineroTiradasMultiples(dineroFibonacciX100AcotadoM[0],'Fibonacci x 100 - Capital Acotado',capAcotado)


print('----------------------MARTINGALA---------------------')
dineroMartinGalaIdeal =  martinGala(valorApuestaIdeal,capIdeal,t,c)

print('----------------------FIBONACCI---------------------')
dineroFibonacciIdeal = fibonacci(capIdeal,t,c)

print('----------------------FIBONACCI X 100---------------------')
dineroFibonacciX100Ideal = fibonacciX100(capIdeal,t,c)


graficoDineroUnicaTirada(dineroMartinGalaIdeal[0],'Estrategia Martingala',capIdeal)

graficoDineroUnicaTirada(dineroFibonacciIdeal[0],'Estrategia Fibonacci',capIdeal)

graficoDineroUnicaTirada(dineroFibonacciX100Ideal[0],'Estrategia Fibonacci x 100',capIdeal)

graficoDineroTiradasMultiples(dineroMartinGalaIdeal[0],'MartinGala - Capital Ideal',capIdeal)

graficoDineroTiradasMultiples(dineroFibonacciIdeal[0],'Fibonacci - Capital Ideal',capIdeal)

graficoDineroTiradasMultiples(dineroFibonacciX100Ideal[0],'Fibonacci x 100 - Capital Ideal',capIdeal)