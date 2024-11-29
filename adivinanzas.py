import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intento = None
    while intento != numero_secreto:
        intento = int(input("Adivina el número entre 1 y 100: "))
        if intento < numero_secreto:
            print("Es más grande.")
        elif intento > numero_secreto:
            print("Es más pequeño.")
        else:
            print("¡Felicidades, has adivinado el número!")

juego_adivinanza()
