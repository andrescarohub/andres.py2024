








"""Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de
fin. El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa
un ciclo for para recorrer el rango."""

# Solicitar al usuario el valor de inicio y fin
inicio = int(input("Introduce el valor de inicio: "))
fin = int(input("Introduce el valor de fin: "))

# Imprimir los números pares en el rango
print("Números pares en el rango:")
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(i)
