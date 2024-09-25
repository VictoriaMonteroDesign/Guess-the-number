import random
import time

def numeroRandom():
    return(random.randint(1, 100))

numeroRandomGenerado = numeroRandom()
print("Se ha seleccionado un numero entre 1 y 100")
juego = int(input("Adivinemos cual es este numero\n¡Buena Suerte!\n"))

if __name__ == '__main__':
    numeroRandomGenerado = numeroRandom()

while True:
    
    if juego > numeroRandomGenerado:
        print("Muy alto!")
    elif juego < numeroRandomGenerado:
        print("Muy bajo!")
    else:
        print("¡Acertaste!")
        break

    time.sleep(0.5)

    intentoComputadora = random.randint(1, 100)
    print(f"\nLa computadora hace el intento con {intentoComputadora}")

    if intentoComputadora > numeroRandomGenerado:
        print("Muy alto!")
    elif intentoComputadora < numeroRandomGenerado:
        print("Muy bajo!")
    else:
        print("Ha acertado la computadora")
        break

    time.sleep(0.5)

    juego = int(input("\nInténtalo nuevamente\n"))