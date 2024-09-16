
"""Enunciado:
Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los
primeros n números enteros. Utiliza un ciclo for para realizar la suma."""
# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializar la suma
suma = 0

# Calcular la suma de los primeros n números enteros
for i in range(1, n + 1):
    suma += i

# Mostrar el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")
