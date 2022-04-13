import matplotlib.pyplot as plt
import numpy as np
import math
plt.style.use('Solarize_Light2')

#TP 1.1 Simulación de Una Ruleta
#Datos

def frecuenciaR(nro, valores):
    frecuenciaA = 0
    for n in valores:
        if n == nro:
            frecuenciaA+= 1
    freqRel= frecuenciaA/len(valores)
    return freqRel

frecuencia= 1/37
esperanza= np.arange(0, 37).mean()  #Media aritmética
desvio= np.arange(0, 37).std() #Desviación Estándar
varianza= np.arange(0, 37).var() #Varianza

t = 10000 #número de tiradas
c = 10 #número de corridas
nroEvaluar = 25 #np.random.randint(0,37)


frecuencias= [[0 for x in range(t)] for y in range(c)]
frecuenciasAbs= [[0 for x in range(t)] for y in range(c)]
medias= [[0 for x in range(t)] for y in range(c)]
desvios= [[0 for x in range(t)] for y in range(c)]
varianzas= [[0 for x in range(t)] for y in range(c)]




for i in range(0, c):
    numeros= np.random.randint(0, 37, t)
    print(numeros)
    for n in range(0, t):
        lista= numeros[:n+1]
        frecuencias[i][n]= frecuenciaR(nroEvaluar, lista)
        frecuenciasAbs[i][n]=numeros[n]
        medias[i][n]= lista.mean()
        desvios[i][n]= lista.std()
        varianzas[i][n]= lista.var()


frecuenciasTCL= np.sum(frecuenciasAbs, axis=0)/c
frecuenciasTCL2=np.sum(frecuenciasAbs, axis=0)



# Graficos
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])


axs[0, 0].set_title('Frecuencia Relativa (fr) respecto a 25')
axs[0, 0].set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia)+0.05)
for i in range(0, c):
    axs[0, 0].plot(range(1, t+1), frecuencias[i])#, label='corrida '+str(i+1)+'°')
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-', label='fre: '+str(round(frecuencia,3)))

axs[0, 1].set_title('Valor Promedio (vp)')
axs[0, 1].set(xlabel='Tiradas', ylabel='Valor Promedio (vp)')
for i in range(0, c):
    axs[0, 1].plot(range(1, t+1), medias[i])#, label='corrida '+str(i+1)+'°')
axs[0, 1].axhline(y=esperanza, color='b', linestyle='-', label='vpe: '+str(round(esperanza,3)))


axs[1, 0].set_title('Valor del Desvío (vd)')
axs[1, 0].set(xlabel='Tiradas', ylabel='Valor del Desvío (vd)')
for i in range(0, c):
    axs[1, 0].plot(range(1, t+1), desvios[i])#, label='corrida '+str(i+1)+'°')
axs[1, 0].axhline(y=desvio, color='b', linestyle='-', label='vde: '+str(round(desvio,3)))

axs[1, 1].set_title('Valor de la Varianza (vve)')
axs[1, 1].set(xlabel='Tiradas', ylabel='Valor de la Varianza (vv)')
for i in range(0, c):
    axs[1, 1].plot(range(1, t+1), varianzas[i])#, label='corrida '+str(i+1)+'°')
axs[1, 1].axhline(y=varianza, color='b', linestyle='-', label='vve: '+str(round(varianza,3)))

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=1, right=t)


plt.show()

#intervalo=round(math.sqrt(t))
for i in range(0, c):
    plt.hist(frecuenciasAbs[i], bins=37, edgecolor='black')
plt.xlabel('Numeros')
plt.ylabel('Frecuencia Absoluta')
plt.title('Histograma de Frecuencia Absoluta')
plt.xlim(0, 36)
plt.show()


intervalo=round(math.sqrt(len(frecuenciasTCL)))
plt.hist(frecuenciasTCL, bins= intervalo, edgecolor='black')
plt.xlabel('Numeros')
plt.ylabel('Frecuencia Absoluta')
plt.title(f'Histograma del TCL de {t} tiradas y {c} corridas ')
plt.axline((frecuenciasTCL.mean(), 0), (frecuenciasTCL.mean(), 1), linewidth=1, color='r', linestyle='--')
plt.show()

intervalo=round(math.sqrt(len(frecuenciasTCL2)))
plt.hist(frecuenciasTCL2, bins= intervalo, edgecolor='black')
plt.xlabel('Numeros')
plt.ylabel('Frecuencia Absoluta')
plt.title(f'Histograma del TCL de {t} tiradas y {c} corridas ')
plt.axline((frecuenciasTCL2.mean(), 0), (frecuenciasTCL2.mean(), 1), linewidth=1, color='r', linestyle='--')
plt.show()
