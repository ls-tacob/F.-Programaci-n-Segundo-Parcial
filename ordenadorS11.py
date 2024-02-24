def ordenador(matriz, fila=None):
    if fila is not None:
        matriz[fila].sort()
    else:
        for fila in matriz:
            fila.sort()

# Solicitar al usuario el tamaño de la matriz
num_filas = int(input("Ingrese el número de filas de la matriz: "))
num_columnas = int(input("Ingrese el número de columnas de la matriz: "))

# Crear una matriz vacía con el tamaño especificado
matriz = []
for _ in range(num_filas):
    fila = [0] * num_columnas
    matriz.append(fila)

# Solicitar al usuario el rango de los números
min_numero = int(input("Ingrese el número mínimo del rango: "))
max_numero = int(input("Ingrese el número máximo del rango: "))

# Llenar la matriz con números aleatorios dentro del rango especificado
import random
for i in range(num_filas):
    for j in range(num_columnas):
        matriz[i][j] = random.randint(min_numero, max_numero)

# Imprimir la matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Preguntar al usuario si desea ordenar toda la matriz
ordenar_toda_matriz = input("¿Desea ordenar toda la matriz? (sí/no): ").lower()

if ordenar_toda_matriz == "sí":
    ordenador(matriz)
else:
    # Solicitar al usuario la fila que desea ordenar
    fila_a_ordenar = int(input("Ingrese el número de fila que desea ordenar (0 a {}): ".format(num_filas - 1)))
    if 0 <= fila_a_ordenar < num_filas:
        ordenador(matriz, fila_a_ordenar)
    else:
        print("¡El número de fila ingresado está fuera del rango válido!")

# Imprimir la matriz ordenada
print("\nMatriz ordenada:")
for fila in matriz:
    print(fila)

