from random import random
from typing import Dict
from GenDistribuido.MTransformada import ExponencialT, UniformeT
from GenDistribuido.MRechazo import EmpiricaR
from matplotlib import pyplot as plt

import numpy as np
import math


def generador_numpy(n):
    numbers = []
    for i in range(n):
        numbers.append(np.random.uniform(0, 1))
    return numbers


class Queue_mm1():

    def __init__(self, num_events, mean_interarrival, mean_service, num_delays_required, customers, cola_maxima=None):
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

    # C code for function initialize, queueing model
    def inicializar(self):
        self.sim_time = 0.0
        # Initialize the state variables.
        self.server_status = 0  # 0 libre(idle); 1 ocupado(busy)
        self.num_in_q = 0
        self.time_last_event = 0.0
        # Initialize the statistical counters.
        self.nums_custs_delayed = 0
        self.total_of_delays = 0.0
        self.area_num_in_q = 0.0
        self.area_server_status = 0.0
        # Initialize event list. Since no customers are present, the departure
        # (service completion) event is eliminated from consideration.
        self.time_next_event = [0.0, 0.0, 0.0]
        self.time_next_event[1] = self.sim_time + \
            self.expon(self.mean_interarrival)
        self.time_next_event[2] = 1 * 10 ** 30  # 1*10e+30
        # codigo libro no esta
        self.time_arrival = [0.0 for i in range(self.customers + 1)]

        self.min_time_next_event = 0.0
        self.next_event_type = 0

        self.clientes_denegados = 0

        self.qdet = []
        self.qdet.append(self.area_num_in_q)

    # C code for function timing, queueing model.
    def timing(self):  # Timing function.
        self.min_time_next_event = 1 * 10 ** 29  # 1*e+29
        self.next_event_type = 0
        # Determine the event type of the next event to occur.
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

    def arrive(self):  # Arrival event function.
        # Schedule next arrival.
        self.time_next_event[1] = self.sim_time + \
            self.expon(self.mean_interarrival)
        # Check to see whether server is busy
        if self.server_status == 1:
            # Server is busy, so increment number of customers in queue.
            self.num_in_q += 1

            # Si es mm1k y la cola está llena
            # Server is busy, so increment number of customers in queue.
            if (self.Q_LIMIT and self.num_in_q > self.Q_LIMIT):
                # The queue has overflowed, so stop the simulation.
                self.clientes_denegados += 1
                print(
                    f'Queue desbordada cantidad denegados:{self.clientes_denegados} tiempo:{self.sim_time}')
            else:
                # There is still room in the queue, so store the time of arrival of the
                # arriving customer at the (new) end of time_arrival.
                self.time_arrival[self.num_in_q] = self.sim_time

        else:
            # Server is idle, so arriving customer has a delay of zero. (The
            # following two statements are for program clarity and do not affect
            # the results of the simulation.)
            self.delay = 0.0
            self.total_of_delays += self.delay
            # Increment the number of customers delayed, and make server busy.
            self.nums_custs_delayed += 1
            self.server_status = 1
            # Schedule a departure (service completion).
            self.time_next_event[2] = self.sim_time + \
                self.expon(self.mean_service)

    def depart(self):  # Schedule a departure (service completion).
        # Check to see whether the queue is empty.
        if self.num_in_q == 0:
            # The queue is empty so make the server idle and eliminate the
            # departure (service completion) event from consideration.
            self.server_status = 0
            self.time_next_event[2] = 1 * 10 ** 30  # 1.0e+30
        else:
            # The queue is nonempty, so decrement the number of customers in queue.
            self.num_in_q -= 1
            # Compute the delay of the customer who is beginning service and update
            # the total delay accumulator.
            self.delay = self.sim_time - self.time_arrival[1]
            self.total_of_delays += self.delay
            # Increment the number of customers delayed, and schedule departure.
            self.nums_custs_delayed += 1
            self.time_next_event[2] = self.sim_time + \
                self.expon(self.mean_service)
            # Move each customer in queue (if any) up one place.
            for i in range(self.num_in_q):
                self.time_arrival[i] = self.time_arrival[i + 1]

    def report(self):  # Report generator function.
        # Compute and write estimates of desired measures of performance.
        print(
            f'Promedio de delay en queue: {self.total_of_delays / self.nums_custs_delayed}')
        print(
            f'Numero promedio en queue: {self.area_num_in_q / self.sim_time}')
        print(
            f'Utilizacion del servidor: {self.area_server_status / self.sim_time}')
        print(f'Tiempo final de simulacion: {self.sim_time}')
        print(f'Clientes denegados :{self.clientes_denegados}')

    # Update area accumulators for time-average statistics.
    def update_time_avg_stats(self):
        # Compute time since last event, and update last-event-time marker.
        self.time_since_last_event = self.sim_time - self.time_last_event
        self.time_last_event = self.sim_time
        # Update area under number-in-queue function.
        self.qdet.append(
            self.num_in_q * self.time_since_last_event / self.sim_time)
        self.area_num_in_q += self.num_in_q * self.time_since_last_event
        # Update area under server-busy indicator function.
        self.area_server_status += self.server_status * self.time_since_last_event


class Inventory():

    def __init__(self, S: int, s: int, inventory_0: int = 60, backlog_0: int = 0) -> None:
        """
        s :Minimum stock acceptable policy
        S :Reposition stock policy"""
        self.min_stock = s
        self.max_reposition = S
        self.Item_montly_costs = 1
        self.bklog_costs = 5
        self.Item_Order_costs = 3
        self.time = 0
        self.inventory = inventory_0
        self.backlog = backlog_0
        self.montly_inv_check = []
        self.montly_bklog_check = []
        self.montly_order_costs = []
        # (time to next reposition, increment of inventory)
        self.Total_cost = 0

    def inventory_level(self) -> int:
        return self.inventory-self.backlog

    def Check_Inventory(self) -> None:
        """Montly check to register inventory levels
        and make orders to suppliers
        returns: Size of order to suppliers"""
        self.montly_inv_check.append(self.inventory)
        self.montly_bklog_check.append(self.backlog)
        # order to suplier
        order_cost = 0
        next_order = 0
        if self.inventory_level() < self.min_stock:
            next_order = self.max_reposition-self.inventory
            order_cost = 32 + next_order*self.Item_Order_costs  # 32 setup cost
        self.montly_order_costs.append(order_cost)
        return next_order

    def Average_holding_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_inv_check[:m])/m
        return I*self.Item_montly_costs

    def Averge_bklog_cost(self, m: int) -> float:
        """m :number of month to check the avg cost
        ADVICE: 1 <= m <= round(self.time)"""
        I = sum(self.montly_bklog_check[:m])/m
        return I*self.bklog_costs

    def Run_Program(self) -> None:
        orders_delivered = 0
        items_demand = []
        customer_orders = generador_numpy(10000)
        customer_orders = ExponencialT(customer_orders, 10)
        order_sizes = generador_numpy(10000)
        order_sizes = EmpiricaR(order_sizes, 1, [1/6, 1/3, 1/3, 1/6])
        deliver_lags = generador_numpy(10000)

        order_times = generador_numpy(120)
        order_times = UniformeT(order_times, .5, 1)

        nxt_cust_order = customer_orders.pop(0)
        nxt_check = 1  # 1 check per month
        nxt_items_order = 0
        nxt_delivery = 0

        Z = 0  # size of the order requested to supplier
        # first event is when an order arrive or the first month end
        month_items_demand = 0
        self.time += min(nxt_check, nxt_cust_order)

        while True:
            if self.time == nxt_check:  # monthly check
                Z = self.Check_Inventory()
                items_demand.append(month_items_demand)
                month_items_demand = 0
                if Z > 0:
                    nxt_items_order = self.time+order_times.pop(0)
                nxt_check += 1

            if self.time == nxt_items_order:  # resuply the stock
                self.inventory += Z
                Z = 0
                nxt_items_order = 0

            if self.time == nxt_cust_order:  # customer order items
                o_size = order_sizes.pop(0)
                month_items_demand += o_size
                if self.inventory < o_size:
                    # backlog items will be delivered the next delivery possible
                    self.backlog += o_size
                else:
                    self.inventory -= o_size
                    nxt_delivery = self.time+deliver_lags.pop(0)
                nxt_cust_order = self.time+customer_orders.pop(0)

            if self.time == nxt_delivery:  # delivery time
                orders_delivered += 1
                if self.backlog > self.inventory > 0:
                    dlv_xtras = self.backlog-self.inventory
                    self.backlog -= dlv_xtras
                    self.inventory = 0
                elif self.inventory > self.backlog > 0:
                    self.inventory -= self.backlog
                    self.backlog = 0
                nxt_delivery = 0

            if self.time >= 120.:
                break
            next_events = [x for x in [nxt_check, nxt_cust_order,
                                       nxt_delivery, nxt_items_order] if x > 0]
            self.time = min(next_events)

        # data
        holding_costs = []
        bklog_costs = []
        monthly_total = []
        inv_level = []
        for i in range(len(self.montly_inv_check)):
            holding_costs.append(self.Average_holding_cost(1+i))
            bklog_costs.append(self.Averge_bklog_cost(1+i))
            inv_level.append(
                self.montly_inv_check[i]-self.montly_bklog_check[i])
            T = (self.montly_inv_check[i]*self.Item_montly_costs)+(
                self.montly_bklog_check[i]*self.bklog_costs)+self.montly_order_costs[i]
            monthly_total.append(T)
            # montly inv check es lista
            # montly order costs es la lista

        # graphics
        fig, axs = plt.subplots(
            ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])

        # nivel de inv
        ax1 = axs[0, 0]
        ax1.set_title("Niveles del inventario")
        ax1.set(xlabel='Mes', ylabel='Cantidad de items')
        ax1.plot(self.montly_inv_check, label='Items en inventario')
        ax1.plot(self.montly_bklog_check, label='Exceso de demanda')
        ax1.plot(inv_level, label='Nivel de inventario')

        # costo promedio
        ax2 = axs[0, 1]
        ax2.set_title("Costos promedios acumulados en el mes")
        ax2.set(xlabel='Mes', ylabel='Gasto promedio del mes $ por Item')
        ax2.plot(holding_costs, label='Gasto promedio por mantenimiento')
        ax2.plot(bklog_costs, label='Perdida promedio por exceso de demanda')

        # demanda items
        ax3 = axs[1, 0]
        ax3.set_title("Demanda en el tiempo")
        ax3.set(xlabel='Mes', ylabel='Items demandados en el mes')
        ax3.plot(items_demand, label='Items demandados')
        ax3.plot(self.montly_inv_check, label='Items disponibles')

        # costo mensual total
        ax4 = axs[1, 1]
        ax4.set_title("Gastos realizados")
        ax4.set(xlabel='Mes', ylabel='$ gastado')
        ax4.plot(monthly_total, label='Total mensual')
        ax4.plot(self.montly_order_costs, label='Gasto mensual en reposicion')
        bk_c = h_c = []
        for i in range(len(self.montly_inv_check)):
            bk_c.append(self.montly_bklog_check[i]*self.bklog_costs)
            h_c.append(self.montly_inv_check[i]*self.Item_montly_costs)
        ax4.plot(bk_c, label='Gasto mensual por exceso de demanda')
        ax4.plot(h_c, label='Gasto mensual por mantenimiento')
        for ax in axs.flat:
            ax.legend()
            ax.set_xlim(left=0, right=120)
        plt.show()


a = Inventory(S=60, s=60, inventory_0=140)
a.Run_Program()
