"""Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo."""

# Solicitar al usuario un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Inicializar el resultado del factorial
factorial = 1

# Calcular el factorial del número
for i in range(1, n + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {n} es: {factorial}")
