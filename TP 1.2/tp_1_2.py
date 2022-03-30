from clases import negros, rojos, randint, apuesta_minima, JugadorMG, JugadorParoli, JugadorGuetting
import matplotlib as plt


def tirada() -> int:
    return randint(0, 36)


apuesta_minima = 1  # float(input("Ingresar monto minimo de apuesta: "))

monto_inicial = 100  # float(input("Ingresar monto inicial de cada jugador: "))

martingala = []
paroli = []
guetting = []

cant_jugadores = 2  # por tipo de jugador

for i in range(cant_jugadores):
    martingala.append(JugadorMG(capital=monto_inicial,
                      apuesta_ini=apuesta_minima))
    paroli.append(JugadorParoli(
        capital=monto_inicial, apuesta_ini=apuesta_minima))
    guetting.append(JugadorGuetting(
        capital=monto_inicial, apuesta_ini=apuesta_minima))

juegos = 0
while True:
    juegos += 1
    numero = tirada()
    print(f'Tirada{juegos}---> Sale {numero}')
    for i in range(cant_jugadores):
        j1: JugadorMG = martingala[i]
        j2: JugadorParoli = paroli[i]
        j3: JugadorGuetting = guetting[i]
        print(
            f"{juegos}-1-1: Jugador Nº{j1.id}-->Monto prejuego={j1.capital}|| apuesta={j1.prox_apuesta}", end='')
        j1.jugar(numero)
        print(f"-->Monto posjuego={j1.capital}")
        print(
            f"{juegos}-1-2: Jugador Nº{j2.id}-->Monto prejuego={j2.capital}||", end=' ')
        j2.jugar(numero)
        print(f"apuesta={j2.prox_apuesta}-->Monto posjuego={j2.capital}")
        print(
            f"{juegos}-1-3: Jugador Nº{j3.id}-->Monto prejuego={j3.capital}||", end=' ')
        j3.jugar(numero)
        print(f"apuesta={j3.prox_apuesta}-->Monto posjuego={j3.capital}")

    print("\n\n\n")
    if int(input("Continuar *0* :")) == 0:
        break
