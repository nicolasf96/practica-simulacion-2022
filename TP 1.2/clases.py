from random import randint

global apuesta_minima
apuesta_minima = 0

global negros
global rojos
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]


class Jugador:
    _last_id = 0

    @classmethod
    def gen_id(cls) -> int:
        cls._last_id += 1
        return cls._last_id

    def __init__(self, capital: float = 0) -> None:
        self.id = self.gen_id()
        self.capital = capital

    def apostar(self) -> None:
        """Se selecciona una tipo de apuesta entre par/impar, rojo/negro o primeros 18/ultimos 18"""
        selector = randint(1, 3)
        selector2 = randint(1, 36)
        if selector == 1:
            """Se apuesta por par o impar"""
            self.prox_apuesta = "impar"
            if selector2//2 == 0:
                self.prox_apuesta = "par"

        elif selector == 2:
            """Se apuesta por [1-18] o [19-36]"""
            self.prox_apuesta = "[1-18]"
            if selector2 in range(19, 37):
                self.prox_apuesta = "[19-36]"

        else:
            """Se apuesta por negro o rojo"""
            self.prox_apuesta = "rojo"
            if selector2 in negros:
                self.prox_apuesta = "negro"


class JugadorMG(Jugador):
    """Jugadores que siguen metodo martingala. 
    Cada apuesta seguira aleatoriamente negro/rojo o [1-18]/[19-36] o par/impar"""

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima) -> None:
        """La apuesta inicial es por defecto la minima"""
        super().__init__(capital)
        self.juegos_perdidos = 0
        self.apuesta_0 = apuesta_ini

    def preparar_apuesta(self) -> None:
        # se selecciona el monto a apostar
        apuesta = self.apuesta_0*(2**self.juegos_perdidos)

        if apuesta <= self.capital:
            self.monto_prox_apuesta = apuesta
        elif self.capital >= apuesta_minima:
            # se abandona temporalmente el sistema cuando ya no se posee el monto indicado por martngala
            self.monto_prox_apuesta = self.capital  # y se apuesta lo que se tiene
        else:
            self.monto_prox_apuesta = 0  # se deja de apostar cuando el capital se termina

        # se selecciona la forma de apuesta
        self.apostar()

    def jugar(self, num: int) -> None:
        self.preparar_apuesta()
        if (num//2 == 0 and self.prox_apuesta == "par") or (num//2 != 0 and self.prox_apuesta == "impar") or (
                num in negros and self.prox_apuesta == "negro") or (num in rojos and self.prox_apuesta == "rojo") or (
                num in range(1, 19) and self.prox_apuesta == "[1-18]") or (num in range(19, 37) and self.prox_apuesta == "[19-36]"):
            self.capital += self.monto_prox_apuesta
            # self.juegos_perdidos = 0  #setear en 0 si se debe reiniciar
        else:
            self.capital -= self.monto_prox_apuesta
            self.juegos_perdidos += 1


class JugadorParoli(Jugador):
    """Jugadores que siguen metodo Paroli
    Cada apuesta seguira aleatoriamente negro/rojo o [1-18]/[19-36] o par/impar"""

    def __init__(self, capital: float = 0, apuesta_ini: float = apuesta_minima) -> None:
        """La apuesta inicial es por defecto la minima"""
        super().__init__(capital)
        self.racha_positiva = 0
        self.apuesta_0 = apuesta_ini

    def preparar_apuesta(self) -> None:
        # se selecciona el monto a apostar
        apuesta = self.apuesta_0*(2**self.racha_positiva)

        if apuesta <= self.capital:
            self.monto_prox_apuesta = apuesta
        elif self.capital >= apuesta_minima:
            # se abandona temporalmente el sistema cuando ya no se posee el monto indicado por Paroli
            self.monto_prox_apuesta = self.capital  # y se apuesta lo que se tiene
        else:
            self.monto_prox_apuesta = 0  # se deja de apostar cuando el capital se termina

        # se selecciona la forma de apuesta
        self.apostar()

    def jugar(self, num: int) -> None:
        self.preparar_apuesta()
        if (num//2 == 0 and self.prox_apuesta == "par") or (num//2 != 0 and self.prox_apuesta == "impar") or (
                num in negros and self.prox_apuesta == "negro") or (num in rojos and self.prox_apuesta == "rojo") or (
                num in range(1, 19) and self.prox_apuesta == "[1-18]") or (num in range(19, 37) and self.prox_apuesta == "[19-36]"):
            self.capital += self.monto_prox_apuesta
            self.racha_positiva += 1
        else:
            self.capital -= self.monto_prox_apuesta
            self.racha_positiva = 0
