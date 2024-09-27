import random

def numeroRandom():
    return(random.randint(1, 100))

numeroRandomGenerado = numeroRandom()
print("Se ha seleccionado un numero entre 1 y 100")

def respuesta(jugador, numeroIntentado, numeroRandomGenerado):
    if numeroIntentado > numeroRandomGenerado:
        print("¡Muy alto!")
    elif numeroIntentado < numeroRandomGenerado:
        print("¡Muy bajo!")
    else:
        print("¡Acertaste!")
        return True
    return False 
