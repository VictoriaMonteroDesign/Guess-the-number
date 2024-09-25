import random

def numeroRandom():
    return(random.randint(1, 100))

numeroRandomGenerado = numeroRandom()
print("Se ha seleccionado un numero entre 1 y 100")

def respuesta(jugador, numeroIntentado, numeroRandomGenerado):
    if numeroIntentado > numeroRandomGenerado:
        print(f"{jugador}: Muy alto!")
    elif numeroIntentado < numeroRandomGenerado:
        print(f"{jugador}: Muy bajo!")
    else:
        print(f"{jugador}: ¡Acertaste!")
        return True
    return False 

while True:
    juego = int(input("Adivinemos cual es este numero\n¡Buena Suerte!\n"))
    if respuesta("Usuario", juego, numeroRandomGenerado):
        break 


    intentoComputadora = random.randint(1, 100)
    print(f"\nLa computadora hace el intento con {intentoComputadora}")
    if respuesta("Computadora", intentoComputadora, numeroRandomGenerado):
        break

