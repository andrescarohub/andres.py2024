
"""Enunciado: (random.randint(1, 100))
Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario
adivinarlo. El programa debe dar pistas si el número ingresado es mayor o menor que el número
secreto. Usa un ciclo while para permitir al usuario seguir intentando hasta que adivine el
número"""

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar la variable para la adivinanza del usuario
adivinanza = 0

# Permitir al usuario adivinar el número
while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 1 y 100): "))
    
    if adivinanza < numero_secreto:
        print("El número es mayor.")
    elif adivinanza > numero_secreto:
        print("El número es menor.")

# Informar al usuario que adivinó el número
print(f"¡Felicidades! Has adivinado el número: {numero_secreto}")
