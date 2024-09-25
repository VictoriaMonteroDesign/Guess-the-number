import random
import time

def numeroRandom():
    return random.randint(1, 100)

def jugar():

    jugador = input("¡Hola jugador! Por favor ingresa tu nombre\n")
    print(f"Hola {jugador}")

    intentos_jugador = []
    intentos_computadora = []

    numeroRandomGenerado = numeroRandom()
    print("Se ha seleccionado un numero entre 1 y 100")
    juego = int(input("Adivinemos cual es este numero\n¡Buena Suerte!\n"))

    intentos_jugador.append(juego)

    while True:
        if juego > numeroRandomGenerado:
            print("Muy alto!")
        elif juego < numeroRandomGenerado:
            print("Muy bajo!")
        else:
            print("¡Acertaste!")
            print(f"Intentos del jugador: {intentos_jugador}")
            print(f"Intentos de la computadora: {intentos_computadora}")
            break

        time.sleep(0.5)

        intentoComputadora = random.randint(1, 100)
        print(f"\nLa computadora hace el intento con {intentoComputadora}")

        intentos_computadora.append(intentoComputadora)

        if intentoComputadora > numeroRandomGenerado:
            print("Muy alto!")
        elif intentoComputadora < numeroRandomGenerado:
            print("Muy bajo!")
        else:
            print("Ha acertado la computadora")
            print(f"Intentos del jugador: {intentos_jugador}")
            print(f"Intentos de la computadora: {intentos_computadora}")
            break

        time.sleep(0.5)

        juego = int(input("\nInténtalo nuevamente\n"))
        intentos_jugador.append(juego)

if __name__ == '__main__':
    jugar()