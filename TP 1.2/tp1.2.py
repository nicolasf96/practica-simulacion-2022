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
c = 2 #número de corridas
fc= np.zeros((c,t+1))
fcI= np.zeros((c,t+1))
frecuencias= np.zeros((c,t))
#frecuencia
fcourses = list()
fvalues = list()

for i in range(0, c):
    numeros= np.random.randint(0, 37, t)
    print(numeros)
    fc[i][0] = inicio
    cA=inicio
    apuesta = 1
    frecuenciaAbs=0
    for n in range(0, t):
        if(numeros[n] in r):
            cA+=apuesta
            apuesta=1
            fcourses.append(n)
            fvalues.append(1)
            frecuenciaAbs +=1
            print('ganaste {}'.format(cA))
        else:
            cA -= apuesta
            apuesta *= 2
            print('perdiste, tenes: {}, apostas:{}'.format(cA, apuesta))
            fcourses.append(n)
            fvalues.append(0)
            if cA<=0 or apuesta>cA:
                print("apuesta:{}> Ca:{}".format(apuesta, cA))
                #fc[i][n + 1] = cA
                for f in range(n+1, t+1):
                    fc[i][f] = cA
                    frecuencias[i][f-1] = frecuenciaAbs / (f)
                break
        frecuencias[i][n] = frecuenciaAbs / (n + 1)
        fc[i][n+1] = cA
print('numeros')
print(fc)
print("frecuencias")
print(frecuencias)
print("---------------------")
print(cI)
for i in range(0, c):
    numeros2= np.random.randint(0, 37, t)
    print(numeros2)
    fcI[i][0] = inicio2
    cI= inicio2
    apuesta = 1
    for n in range(0, t):
        if(numeros2[n] in r):
            cI+=apuesta
            apuesta=1
            print('ganaste {}'.format(cI))
        else:
            cI -= apuesta
            apuesta *= 2
            print('perdiste, tenes: {}, apostas:{}'.format(cI, apuesta))
            if cI<=0 or apuesta>cI:
                print("apuesta:{}> Ca:{}".format(apuesta, cI))
                #fcI[i][n + 1] = cI
                for f in range(n+1, t+1):
                    fcI[i][f] = cI
                break
        fcI[i][n+1] = cI
print(fcI)

print('----------------')
print('fibonacci')
fcF= np.zeros((c,t+1))
cAF=inicio
apuesta = 1
for i in range(0, c):
    numeros= np.random.randint(0, 37, t)
    print(numeros)
    fcF[i][0] = inicio
    cAF=inicio
    apuesta = 1
    racha=0
    for n in range(0, t):
        if(numeros[n] in r):
            if(racha==0 or racha==1):
                apuesta=1  # cambiar si se gana se vuelve 2 atras
                racha=0
            else:
                apuesta=fib(racha)
                racha -= 2
            cAF += apuesta
            fcourses.append(n)
            fvalues.append(1)
            print('ganaste {}'.format(cAF))
        else:

            if (racha == 0 or racha == 1):
                apuesta = 1  # cambiar si se gana se vuelve 2 atras
            else:
                apuesta = fib(racha+1)
            racha += 1
            cAF -= apuesta
            print('perdiste, tenes: {}, apostas:{}'.format(cAF, apuesta))
            fcourses.append(n)
            fvalues.append(0)
            if cAF<=0 or apuesta>cAF:
                print("apuesta:{}> Ca:{}".format(apuesta, cAF))
                #fc[i][n + 1] = cA
                for f in range(n+1, t+1):
                    fcF[i][f] = cAF
                break
        fcF[i][n+1] = cAF


fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])

axs[0, 0].set_title('capital finito')
axs[0, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[0, 0].set_ylim(bottom=np.min(fc), top=np.amax(fc))
for i in range(0, c):
    axs[0, 0].plot(range(0, t+1), fc[i])
axs[0, 0].axhline(y=inicio, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio,3)))
print(fc)

axs[0, 1].set_title('capital infinito')
axs[0, 1].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[0, 1].set_ylim(bottom=np.min(fcI), top=np.amax(fcI))
for i in range(0, c):
    axs[0, 1].plot(range(0, t+1), fcI[i])
axs[0, 1].axhline(y=inicio2, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio2,3)))
'''
axs[1, 0].set_title('frecuencia')
axs[1, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[1, 0].set_ylim(bottom=np.min(frecuencias), top=np.amax(frecuencias)+0.1)
for i in range(0, c):
    axs[1, 0].plot(range(0, t), frecuencias[i])
'''
axs[1, 0].set_title('fibonacci')
axs[1, 0].set(xlabel='Tiradas', ylabel='Cantidad de capital (cc)')
axs[1, 0].set_ylim(bottom=np.min(fcF), top=np.amax(fcF))
for i in range(0, c):
    axs[1, 0].plot(range(0, t+1), fcF[i])
axs[1, 0].axhline(y=inicio, color='b', linestyle='-', label='Cap Inicial: '+str(round(inicio,3)))

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=t)


plt.bar(fcourses, fvalues)

plt.ylabel('frecuencia')

plt.xlabel('tiradas')


plt.show()