# Programa: Reserva de asientos de una sala de cine
# La sala dispone de 12 asientos organizados en 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# 1. Crear la matriz como una lista de listas.
# Todos los asientos comienzan libres, por eso se inicializan con 0.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Mostrar el título y las instrucciones del programa.
print("========================================")
print("       RESERVA DE ASIENTOS - CINE      ")
print("========================================")
print("0 = asiento libre")
print("1 = asiento reservado")
print()

# 2. Solicitar al usuario la fila y la columna.
# Los índices comienzan en 0:
# Filas: 0, 1 y 2
# Columnas: 0, 1, 2 y 3
fila = int(input("Ingrese la fila del asiento (0, 1 o 2): "))
columna = int(input("Ingrese la columna del asiento (0, 1, 2 o 3): "))

# Verificar que la fila y la columna estén dentro de los índices válidos.
if 0 <= fila < 3 and 0 <= columna < 4:

    # Acceder al asiento utilizando sus índices de fila y columna.
    if asientos[fila][columna] == 0:

        # 3. Marcar el asiento como reservado asignándole el valor 1.
        asientos[fila][columna] = 1

        print()
        print("¡Asiento reservado correctamente!")

    else:
        print()
        print("El asiento seleccionado ya está reservado.")

else:
    print()
    print("Error: la fila o columna ingresada no es válida.")

# 4. Mostrar la matriz completa utilizando bucles anidados.
print()
print("========================================")
print("          ESTADO COMPLETO DE LA SALA   ")
print("========================================")

# El primer bucle recorre las filas de la matriz.
for fila_actual in asientos:

    # El segundo bucle recorre los asientos de cada fila.
    for asiento in fila_actual:
        print(asiento, end=" ")

    # Saltar de línea al terminar cada fila.
    print()

print()
print("Fin del programa.")
