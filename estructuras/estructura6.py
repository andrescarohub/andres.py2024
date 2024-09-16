

"""Enunciado:
Escribe un programa que solicite al usuario ingresar números enteros indefinidamente. El
programa debe sumar los números siempre que sean pares, pero debe detenerse si el usuario
ingresa un número impar. Usa un ciclo while para lograr esto."""

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
