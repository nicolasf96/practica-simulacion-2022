from random import random,seed
from numpy import log, average, median, std
from datetime import datetime
from clases import Queue_mm1

num_events = 2
mean_service = 0.5
num_delays_required = 1000
Q_LIMIT = 10000

tamaños_cola = [0 ,2 ,5 ,10 ,50]
par_mu = 1/ mean_service
tasas_arribos_relativas = [0.25, 0.5, 0.75, 1, 1.25]
tasas_arribos = [t * par_mu for t in tasas_arribos_relativas] ##[0.5, 1.0, 1.5, 2.0, 2.5]
corridas=10

for t in tasas_arribos:
    mean_interarrival = 1/t
    mm1 = Queue_mm1(num_events, mean_interarrival, mean_service, num_delays_required, Q_LIMIT)
    mm1.timing()
    metricas_simulacion = []
    frecuencias_cola = []
    frecuencias_sistema = []

    for i in range(corridas):


        # el if y el seed no se para que sirven
        if i % 10 == 0:
            print('Simulado ' + str(i) + '/' + str(corridas))

        seed(datetime.now())
        mm1.inicializar()

        historico_cola_simulacion = []
        historico_sistema_simuacion = []
        historico_cola_simulacion.append(0)
        historico_sistema_simuacion.append(0)

        while (mm1.nums_custs_delayed < mm1.num_delays_required):
            mm1.timing()
            mm1.update_time_avg_stats()

            if mm1.next_event_type == 1:
                mm1.arrive()
            elif mm1.next_event_type == 2:
                mm1.depart()

            # Para calcular la probabilidad de n clientes en cola
            historico_cola_simulacion.append(mm1.num_in_q)

            if mm1.server_status == 1:
                historico_sistema_simuacion.append(mm1.num_in_q + 1)
            else:
                historico_sistema_simuacion.append(mm1.num_in_q)

        mm1.report()


        frecuencias_cola_iteracion = [0 for i in range(7)]
        frecuencias_sistema_iteracion = [0 for i in range(7)]

        # Cuenta ocurrencias hasta 5, la siguiente será de cualquier numero mayor a 5
        for i in range(6):
            frecuencias_cola_iteracion[i] = historico_cola_simulacion.count(i)  # / len(historico_cola_simulacion)

        frecuencias_cola_iteracion[6] = sum(i > 5 for i in historico_cola_simulacion)

        # Cuenta ocurrencias hasta 5, la siguiente será de cualquier numero mayor a 5
        for i in range(6):
            frecuencias_sistema_iteracion[i] = historico_sistema_simuacion.count(
                i)  # / len(historico_sistema_simuacion)

        frecuencias_sistema_iteracion[6] = sum(i > 5 for i in historico_sistema_simuacion)

        # Añade las frecuencias de la corrida a las generales
        frecuencias_cola.append(frecuencias_cola_iteracion)
        frecuencias_sistema.append(frecuencias_sistema_iteracion)
