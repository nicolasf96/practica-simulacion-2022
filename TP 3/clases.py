from random import random

import numpy as np
import math 


class Queue_mm1():

    def __init__(self, num_events, mean_interarrival, mean_service, num_delays_required, customers, cola_maxima = None):
        self.num_events = num_events
        self.mean_interarrival = mean_interarrival
        self.mean_service = mean_service
        self.num_delays_required = num_delays_required
        self.customers = customers
        self.parameter_lambda = 1 / self.mean_interarrival
        self.parameter_mu = 1 / self.mean_service
        self.Q_LIMIT = cola_maxima

        self.inicializar()

    def expon(self, mean):
        return -mean * math.log(np.random.uniform(0, 1))

    #C code for function initialize, queueing model
    def inicializar(self):
        self.sim_time = 0.0
        #Initialize the state variables.
        self.server_status = 0  #0 libre(idle); 1 ocupado(busy)
        self.num_in_q = 0
        self.time_last_event = 0.0
        #Initialize the statistical counters.
        self.nums_custs_delayed = 0
        self.total_of_delays = 0.0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        #Initialize event list. Since no customers are present, the departure
        #(service completion) event is eliminated from consideration.
        self.time_next_event = [0.0,0.0,0.0]
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)
        self.time_next_event[2] =1* 10 ** 30 #1*10e+30
        #codigo libro no esta
        self.time_arrival = [0.0 for i in range(self.customers + 1)]

        self.min_time_next_event = 0.0
        self.next_event_type = 0

        self.clientes_denegados = 0

        self.qdet = []
        self.qdet.append(self.area_num_in_q)

    #C code for function timing, queueing model.
    def timing(self): #Timing function.
        self.min_time_next_event =1* 10 ** 29 #1*e+29
        self.next_event_type = 0
        #Determine the event type of the next event to occur.
        for i in range(1, self.num_events+1):
            if self.time_next_event[i] < self.min_time_next_event:
                self.min_time_next_event = self.time_next_event[i]
                self.next_event_type = i

        # Check to see whether the event list is empty
        if self.next_event_type == 0:
            # The event list is empty, so stop the simulation.
            print(f'Lista de eventos vacía en ese momento  {self.sim_time}')
            exit()
        # The event list is not empty, so advance the simulation clock
        self.sim_time = self.min_time_next_event

    def arrive(self): #Arrival event function.
        #Schedule next arrival.
        self.time_next_event[1] = self.sim_time + self.expon(self.mean_interarrival)
        #Check to see whether server is busy
        if self.server_status == 1:
            #Server is busy, so increment number of customers in queue.
            self.num_in_q += 1

            # Si es mm1k y la cola está llena
            #Server is busy, so increment number of customers in queue.
            if (self.Q_LIMIT and self.num_in_q > self.Q_LIMIT):
                #The queue has overflowed, so stop the simulation.
                self.clientes_denegados += 1
                print(f'Queue desbordada cantidad denegados:{self.clientes_denegados} tiempo:{self.sim_time}')
            else:
                #There is still room in the queue, so store the time of arrival of the
                #arriving customer at the (new) end of time_arrival.
                self.time_arrival[self.num_in_q] = self.sim_time

        else:
            #Server is idle, so arriving customer has a delay of zero. (The
            # following two statements are for program clarity and do not affect
            # the results of the simulation.)
            self.delay = 0.0
            self.total_of_delays += self.delay
            #Increment the number of customers delayed, and make server busy.
            self.nums_custs_delayed += 1
            self.server_status = 1
            # Schedule a departure (service completion).
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)

    def depart(self): # Schedule a departure (service completion).
        # Check to see whether the queue is empty.
        if self.num_in_q == 0:
            #The queue is empty so make the server idle and eliminate the
            #departure (service completion) event from consideration.
            self.server_status = 0
            self.time_next_event[2] =1* 10 ** 30 #1.0e+30
        else:
            # The queue is nonempty, so decrement the number of customers in queue.
            self.num_in_q -= 1
            #Compute the delay of the customer who is beginning service and update
            #the total delay accumulator.
            self.delay = self.sim_time - self.time_arrival[1]
            self.total_of_delays += self.delay
            #Increment the number of customers delayed, and schedule departure.
            self.nums_custs_delayed += 1
            self.time_next_event[2] = self.sim_time + self.expon(self.mean_service)
            # Move each customer in queue (if any) up one place.
            for i in range(self.num_in_q):
                self.time_arrival[i] = self.time_arrival[i + 1]

    def report(self):#Report generator function.
        # Compute and write estimates of desired measures of performance.
        print(f'Promedio de delay en queue: {self.total_of_delays / self.nums_custs_delayed}')
        print(f'Numero promedio en queue: {self.area_num_in_q / self.sim_time}')
        print(f'Utilizacion del servidor: {self.area_server_status / self.sim_time}')
        print(f'Tiempo final de simulacion: {self.sim_time}')
        print(f'Clientes denegados :{self.clientes_denegados}')

    def update_time_avg_stats(self): #Update area accumulators for time-average statistics.
        # Compute time since last event, and update last-event-time marker.
        self.time_since_last_event = self.sim_time - self.time_last_event
        self.time_last_event = self.sim_time
        # Update area under number-in-queue function.
        self.qdet.append(self.num_in_q * self.time_since_last_event / self.sim_time)
        self.area_num_in_q += self.num_in_q * self.time_since_last_event
        # Update area under server-busy indicator function.
        self.area_server_status += self.server_status * self.time_since_last_event