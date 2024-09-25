import random

def numeroRandom():
    return(random.randint(1, 100))

numeroRandomGenerado = numeroRandom()

jugador = input("¡Hola jugador! Por favor ingresa tu nombre\n")
print(f"Hola {jugador}")


print("Voy a elegir un número entre 1 y 100\nAhora adivina.")

for intento in range(4):
    if intento == 0:
        juego = int(input("¿Qué número es el que escogí? Tienes 5 intentos\n¡Buena Suerte!\n"))
    else:
        juego = int(input("Inténtalo nuevamente\n"))

    if juego == numeroRandomGenerado:
        print("¡Acertaste!")
        break
    elif juego > numeroRandomGenerado:
        print("Muy alto.")
    else:
        print("Muy bajo.")

#intentos = intento[0,1,2,3,4]

if juego != numeroRandomGenerado:
    print(f"Lo siento, se te acabaron los intentos. El número era {numeroRandomGenerado}")