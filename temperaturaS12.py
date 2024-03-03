# Datos de temperaturas por semanas y ciudades
temperaturas_costa = [
    [
        [30, 31, 29, 28, 30, 32, 33],  # Guayaquil, semana 1
        [31, 32, 30, 29, 31, 33, 34]  # Guayaquil, semana 2
    ],
    [
        [29, 30, 28, 27, 29, 31, 32],  # Santo Domingo, semana 1
        [28, 29, 27, 26, 28, 30, 31]  # Santo Domingo, semana 2
    ]
]

temperaturas_sierra = [
    [
        [15, 14, 16, 15, 13, 15, 16],  # Latacunga, semana 1
        [16, 15, 14, 13, 15, 17, 16]  # Latacunga, semana 2
    ],
    [
        [22, 21, 23, 22, 21, 23, 24],  # Quito, semana 1
        [23, 22, 21, 20, 22, 24, 25]  # Quito, semana 2
    ]
]

temperaturas_oriente = [
    [
        [27, 28, 26, 25, 27, 29, 30],  # Tena, semana 1
        [28, 29, 27, 26, 28, 30, 31]  # Tena, semana 2
    ],
    [
        [15, 14, 16, 15, 13, 15, 16],  # Papallacta, semana 1
        [16, 15, 14, 13, 15, 17, 16]  # Papallacta, semana 2
    ]
]

# Nombres de las regiones y ciudades
nombres_regiones = ['Costa', 'Sierra', 'Oriente']
nombres_ciudades = [['Guayaquil', 'Santo Domingo'], ['Latacunga', 'Quito'], ['Tena', 'Papallacta']]

# Matriz de temperaturas
temperaturas = [temperaturas_costa, temperaturas_sierra, temperaturas_oriente]

# Preguntar al usuario si desea conocer todos los datos o de una ciudad específica
opcion = input("¿Desea conocer todos los datos (T) o de una ciudad específica (C)? (T/C): ").upper()

if opcion == 'T':
    # Calcular el promedio de temperaturas para cada región y semana
    for idx_region, ciudades_region in enumerate(temperaturas):
        nombre_region = nombres_regiones[idx_region]
        print(f'Región {nombre_region}:')
        for idx_semana, ciudad_semanal in enumerate(ciudades_region, start=1):
            promedio_semana = []
            for idx_ciudad, temperaturas_ciudad in enumerate(ciudad_semanal, start=1):
                promedio_temp_ciudad = sum(temperaturas_ciudad) / len(temperaturas_ciudad)
                promedio_semana.append(promedio_temp_ciudad)
                nombre_ciudad = nombres_ciudades[idx_region][idx_ciudad - 1]
                print(
                    f'  Ciudad {nombre_ciudad}: Promedio de temperatura para semana {idx_semana} = {promedio_temp_ciudad:.2f}')
            promedio_region_semana = sum(promedio_semana) / len(promedio_semana)
            print(
                f'  Promedio de temperatura de la región {nombre_region} para semana {idx_semana} = {promedio_region_semana:.2f}')
elif opcion == 'C':
    ciudad_elegida = input(
        "Ingrese el nombre de la ciudad (Guayaquil, Santo Domingo, Latacunga, Quito, Tena, Papallacta): ")
    semana_elegida = int(input("Ingrese el número de la semana (1 o 2): "))

    # Encontrar índice de la ciudad
    for idx_region, ciudades_region in enumerate(nombres_ciudades):
        for idx_ciudad, nombre_ciudad in enumerate(ciudades_region, start=1):
            if nombre_ciudad.lower() == ciudad_elegida.lower():
                idx_ciudad_elegida = idx_ciudad
                idx_region_elegida = idx_region
                break
        else:
            continue
        break

    promedio_temp_ciudad = sum(temperaturas[idx_region_elegida][idx_ciudad_elegida - 1][semana_elegida - 1]) / len(
        temperaturas[idx_region_elegida][idx_ciudad_elegida - 1][semana_elegida - 1])
    print(
        f"El promedio de temperatura en {ciudad_elegida} para la semana {semana_elegida} es: {promedio_temp_ciudad:.2f}")
else:
    print("Opción no válida.")
