## DESAFÍO 2: GENERADOR DE HISTOGRAMA
# Crear un programa que tome una lista de números y genere un histograma basado en esos números,
# usando asteriscos para crear las barras del histograma.


def histograma_por_intervalos(datos, ancho_barra):
    if not datos:
        return

    # Definimos el inicio y fin ordenados de menor a mayor
    minimo = int(min(datos) // ancho_barra) * ancho_barra
    maximo = int(max(datos) // ancho_barra) * ancho_barra

    print(f"\n--- Histograma (Intervalos de tamaño {ancho_barra}) ---")
    print(" Intervalo  | Frecuencia")
    print("-" * 30)

    # Recorremos cada intervalo de menor a mayor
    actual = minimo
    while actual <= maximo:
        siguiente = actual + ancho_barra

        # Contamos cuántos números (incluyendo decimales) caen en [actual, siguiente)
        frecuencia = 0
        for num in datos:
            if actual <= num < siguiente:
                frecuencia += 1

        print(f"[{actual:3d} - {siguiente:3d}) | {'*' * frecuencia}")
        actual = siguiente

# -----------------------------------------------------------------------------------
# EJEMPLO 1
# -----------------------------------------------------------------------------------

# Lista de valores
valores = [4.2, 8.7, 2.5, 6, 0.4, 5.5, 4.8, 2.1, 4.0, 9.1, 5.9, 1.2]


histograma_por_intervalos(valores, ancho_barra=2)

# -----------------------------------------------------------------------------------
# EJEMPLO 2
# -----------------------------------------------------------------------------------

valores2 = [
    12.5, 45.2, 78.9, 34.0, 23.1, 89.4, 56.7, 67.3, 91.2, 15.8,
    42.0, 51.3, 63.8, 72.1, 84.5, 29.6, 38.4, 49.9, 55.0, 61.2,
    77.7, 82.3, 95.6, 18.2, 27.4, 33.3, 47.8, 53.1, 68.9, 74.0,
    88.1, 19.5, 41.2, 58.6, 64.4, 70.2, 81.9, 93.0, 52.4, 66.8
]

histograma_por_intervalos(valores2, ancho_barra=10)