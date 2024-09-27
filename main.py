import random
import time

def numeroRandom():
    return random.randint(1, 100)

def validarIntento(juego, numeroRandomGenerado, intentosJugador, intentosComputadora):
    if juego > numeroRandomGenerado:
      print("Muy alto!")
      return False
    
    elif juego < numeroRandomGenerado:
      print("Muy bajo!")
      return False

    else:
      print("¡Acertaste!")
      print(f"Intentos del jugador: {intentosJugador}")
      print(f"Intentos de la computadora: {intentosComputadora}")
      return True


def jugar():

    # Funcion 1: que solicite el nombre del jugador lo imprima y lo retorne
    jugador = input("¡Hola jugador! Por favor ingresa tu nombre\n")
    print(f"Hola {jugador}")

    intentosJugador = []
    intentosComputadora = []

    numeroRandomGenerado = numeroRandom()
    print("Se ha seleccionado un numero entre 1 y 100")

    # Funcion 2: que solicite el intento, lo agregue al listado de intentos y lo retorne
    juego = int(input("Adivinemos cual es este numero\n¡Buena Suerte!\n"))
    intentosJugador.append(juego)

    while True:
        validacion = validarIntento(juego, numeroRandomGenerado, intentosJugador, intentosComputadora)
        if validacion == True:
          return
          break

        time.sleep(0.5)

        juegoComputadora = random.randint(1, 100)
        print(f"\nLa computadora hace el intento con {juegoComputadora}")

        intentosComputadora.append(juegoComputadora)

        validacion = validarIntento(juegoComputadora, numeroRandomGenerado, intentosJugador, intentosComputadora)
        if validacion == True:
          break


        time.sleep(0.5)

        juego = int(input("\nInténtalo nuevamente\n"))
        intentosJugador.append(juego)

if __name__ == '__main__':
    jugar()