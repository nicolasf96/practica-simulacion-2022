import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)



r=[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
n=[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 33, 31, 35]

inicio=40
cA=inicio # capitalAcotado
inicio2=90000
cI=inicio2 #Capital Infinito
flujo=0
apuesta=1
t = 100 #número de tiradas
c = 10 #número de corridas
fc= np.zeros((c,t+1))
fcI= np.zeros((c,t+1))
fcF= np.zeros((c,t+1))
fcFI= np.zeros((c,t+1))
fcD= np.zeros((c,t+1))
fcDI= np.zeros((c,t+1))
frecuencias= np.zeros((c,t))
fGanancia=18/37



for i in range(0, c):
    numeros= np.random.randint(0, 37, t)
    print(numeros)
    #capital finito
    fc[i][0] = inicio
    cA=inicio
    apuesta = 1
    #capital infinito
    fcI[i][0] = inicio2
    cI = inicio2
    apuestaInf=1
    #fibonacci
    fcF[i][0] = inicio
    cAF = inicio
    apuestaFib = 1
    racha = 0
    # fibonacci infinito
    fcFI[i][0] = inicio2
    cAFI = inicio2
    apuestaFibI = 1
    rachaI = 0
    #D'Alembert
    fcD[i][0] = inicio
    cAD = inicio
    apuestaD = 1
    # D'Alembert infinito
    fcDI[i][0] = inicio2
    cADI = inicio2
    apuestaDI = 1
    #frecuencia
    frecuenciaAbs=0
    #Martingala capital finito
    for n in range(0, t):
        if(numeros[n] in r):
            cA+=apuesta
            apuesta=1
            print('ganaste {}'.format(cA))
        else:
            cA -= apuesta
            apuesta *= 2
            print('perdiste, tenes: {}, apostas:{}'.format(cA, apuesta))

            if cA<=0 or apuesta>cA:
                print("apuesta:{}> Ca:{}".format(apuesta, cA))
                #fc[i][n + 1] = cA
                for f in range(n+1, t+1):
                    fc[i][f] = cA
                break
        fc[i][n+1] = cA
    #Martingala capital infinito
    for n in range(0, t):
        if(numeros[n] in r):
            cI+=apuestaInf
            apuestaInf=1
            print('ganaste {}'.format(cI))
        else:
            cI -= apuestaInf
            apuestaInf *= 2
            print('perdiste, tenes: {}, apostas:{}'.format(cI, apuestaInf))
            if cI<=0 or apuestaInf>cI:
                print("apuesta:{}> Ca:{}".format(apuestaInf, cI))
                #fcI[i][n + 1] = cI
                for f in range(n+1, t+1):
                    fcI[i][f] = cI
                break
        fcI[i][n+1] = cI
    #fibonacci
    for n in range(0, t):
        if(numeros[n] in r):
            if(racha==0 or racha==1):
                apuestaFib=1
                racha=0
            else:
                apuestaFib=fib(racha)
                racha -= 2
            cAF += apuestaFib

            print('ganaste {}'.format(cAF))
        else:

            if (racha == 0 or racha == 1):
                apuestaFib = 1
            else:
                apuestaFib = fib(racha+1)
            racha += 1
            cAF -= apuestaFib
            print('perdiste, tenes: {}, apostas:{}'.format(cAF, apuestaFib))
            if cAF<=0 or apuestaFib>cAF:
                print("apuesta:{}> cAF:{}".format(apuestaFib, cAF))
                for f in range(n+1, t+1):
                    fcF[i][f] = cAF
                break
        fcF[i][n+1] = cAF

    # fibonacci infinito
    print("fibonacci infinito")
    for n in range(0, t):
        if (numeros[n] in r):
            if (rachaI == 0 or rachaI == 1):
                apuestaFibI = 1  # cambiar si se gana se vuelve 2 atras
                rachaI = 0
            else:
                apuestaFibI = fib(rachaI)
                rachaI -= 2
            cAFI += apuestaFibI

            print('ganaste {}'.format(cAFI))
        else:

            if (rachaI == 0 or rachaI == 1):
                apuestaFibI = 1  # cambiar si se gana se vuelve 2 atras
            else:
                apuestaFibI = fib(rachaI + 1)
            rachaI += 1
            cAFI -= apuestaFibI
            print('perdiste, tenes: {}, apostas:{}'.format(cAFI, apuestaFibI))
            if cAFI <= 0 or apuestaFibI > cAFI:
                print("apuesta:{}> cAFI:{}".format(apuestaFibI, cAFI))
                for f in range(n + 1, t + 1):
                    fcFI[i][f] = cAFI
                break
        fcFI[i][n + 1] = cAFI
    print("-------------------")
    #D'Alembert
    print("D'Alambert")
    for n in range(0, t):
        if(numeros[n] in r):
            if(apuestaD==0 or apuestaD==1):
                apuestaD=1
            else:
                apuestaD-=1
            cAD += apuestaD

            print('ganaste {}, apostas:{}'.format(cAD, apuestaD))
        else:
            cAD -= apuestaD
            apuestaD += 1
            print('perdiste, tenes: {}, apostas:{}'.format(cAD, apuestaD))
            if cAD<=0 or apuestaD>cAD:
                print("apuesta:{}> cAD:{}".format(apuestaD, cAD))
                for f in range(n+1, t+1):
                    fcD[i][f] = cAD
                break
        fcD[i][n+1] = cAD

    # D'Alembert Ininito
    print("D'Alambert infinito")
    for n in range(0, t):
        if (numeros[n] in r):
            if (apuestaDI == 0 or apuestaDI == 1):
                apuestaDI = 1
            else:
                apuestaDI -= 1
            cADI += apuestaDI

            print('ganaste {}, apostas:{}'.format(cADI, apuestaDI))
        else:
            cADI -= apuestaDI
            apuestaDI += 1
            print('perdiste, tenes: {}, apostas:{}'.format(cADI, apuestaDI))
            if cADI <= 0 or apuestaDI > cADI:
                print("apuesta:{}> cADI:{}".format(apuestaDI, cADI))
                for f in range(n + 1, t + 1):
                    fcDI[i][f] = cADI
                break
        fcDI[i][n + 1] = cADI
    #frecuencia
    for n in range(0, t):
        if (numeros[n] in r):
            frecuenciaAbs += 1
        frecuencias[i][n] = frecuenciaAbs / (n+1)


print(frecuencias)

fig, axs = plt.subplots(ncols=2, nrows=4, constrained_layout=True, figsize=[9, 6])

axs[0, 0].set_title('capital finito')
axs[0, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[0, 0].set_ylim(bottom=np.min(fc), top=np.amax(fc))
for i in range(0, c):
    axs[0, 0].plot(range(0, t+1), fc[i])
axs[0, 0].axhline(y=inicio, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio,3)))


axs[0, 1].set_title('capital infinito')
axs[0, 1].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[0, 1].set_ylim(bottom=np.min(fcI), top=np.amax(fcI))
for i in range(0, c):
    axs[0, 1].plot(range(0, t+1), fcI[i])
axs[0, 1].axhline(y=inicio2, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio2,3)))

axs[1, 0].set_title('fibonacci')
axs[1, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[1, 0].set_ylim(bottom=np.min(fcF), top=np.amax(fcF))
for i in range(0, c):
    axs[1, 0].plot(range(0, t+1), fcF[i])
axs[1, 0].axhline(y=inicio, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio,3)))

axs[1, 1].set_title('fibonacci infinito')
axs[1, 1].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[1, 1].set_ylim(bottom=np.min(fcFI), top=np.amax(fcFI))
for i in range(0, c):
    axs[1, 1].plot(range(0, t+1), fcFI[i])
axs[1, 1].axhline(y=inicio2, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio2,3)))

axs[3, 1].set_title('frecuencias')
axs[3, 1].set(xlabel='Tiradas', ylabel='Frecuencia')
axs[3, 1].set_ylim(bottom=0, top=np.amax(frecuencias)+0.1)
for i in range(0, c):
    axs[3, 1].plot(range(0, t), frecuencias[i])
axs[3, 1].axhline(y=fGanancia, color='b', linestyle='-', label='Frecuancia ganancia: '+str(round(fGanancia,3)))

axs[2, 0].set_title("D'Alembert")
axs[2, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[2, 0].set_ylim(bottom=np.min(fcD), top=np.amax(fcD))
for i in range(0, c):
    axs[2, 0].plot(range(0, t+1), fcD[i])
axs[2, 0].axhline(y=inicio, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio,3)))

axs[2, 1].set_title("D'Alembert infinito")
axs[2, 1].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[2, 1].set_ylim(bottom=np.min(fcDI), top=np.amax(fcDI))
for i in range(0, c):
    axs[2, 1].plot(range(0, t+1), fcDI[i])
axs[2, 1].axhline(y=inicio2, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio2,3)))

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=t)
print(fcF)
print(fcFI)

plt.show()