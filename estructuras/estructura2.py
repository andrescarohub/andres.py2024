"""Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i,
o, u) contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta."""
# Solicitar al usuario una cadena de texto
texto = input("Introduce una cadena de texto: ")

# Inicializar el contador de vocales
contador_vocales = 0

# Contar las vocales en la cadena
for caracter in texto:
    if caracter.lower() in 'aeiou':
        contador_vocales += 1

# Mostrar el resultado
print(f"El número de vocales en la cadena es: {contador_vocales}")
