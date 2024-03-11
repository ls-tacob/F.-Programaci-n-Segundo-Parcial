# Datos de temperaturas por semanas y ciudades
temperaturas_costa = [
    [
        [30, 31, 29, 28, 30, 32, 33],  # Guayaquil, semana 1
        [31, 32, 30, 29, 31, 33, 34],  # Guayaquil, semana 2
        [32, 33, 31, 30, 32, 34, 35],  # Guayaquil, semana 3
        [33, 34, 32, 31, 33, 35, 36]   # Guayaquil, semana 4
    ],
    [
        [29, 30, 28, 27, 29, 31, 32],  # Santo Domingo, semana 1
        [28, 29, 27, 26, 28, 30, 31],  # Santo Domingo, semana 2
        [27, 28, 26, 25, 27, 29, 30],  # Santo Domingo, semana 3
        [26, 27, 25, 24, 26, 28, 29]   # Santo Domingo, semana 4
    ]
]

temperaturas_sierra = [
    [
        [15, 14, 16, 15, 13, 15, 16],  # Latacunga, semana 1
        [16, 15, 14, 13, 15, 17, 16],  # Latacunga, semana 2
        [17, 16, 15, 14, 16, 18, 17],  # Latacunga, semana 3
        [18, 17, 16, 15, 17, 19, 18]   # Latacunga, semana 4
    ],
    [
        [22, 21, 23, 22, 21, 23, 24],  # Quito, semana 1
        [23, 22, 21, 20, 22, 24, 25],  # Quito, semana 2
        [24, 23, 22, 21, 23, 25, 24],  # Quito, semana 3
        [25, 24, 23, 22, 24, 26, 25]   # Quito, semana 4
    ]
]

temperaturas_oriente = [
    [
        [27, 28, 26, 25, 27, 29, 30],  # Tena, semana 1
        [28, 29, 27, 26, 28, 30, 31],  # Tena, semana 2
        [29, 30, 28, 27, 29, 31, 32],  # Tena, semana 3
        [30, 31, 29, 28, 30, 32, 33]   # Tena, semana 4
    ],
    [
        [15, 14, 16, 15, 13, 15, 16],  # Papallacta, semana 1
        [16, 15, 14, 13, 15, 17, 16],  # Papallacta, semana 2
        [17, 16, 15, 14, 16, 18, 17],  # Papallacta, semana 3
        [18, 17, 16, 15, 17, 19, 18]   # Papallacta, semana 4
    ]
]

# Función para sumar las temperaturas por semana
def sumar_temperaturas(temperaturas):
    suma_semanal = []
    for region in temperaturas:
        for ciudad in region:
            for semana in ciudad:
                suma_semana = sum(semana)
                suma_semanal.append(suma_semana)
    return suma_semanal

# Función para calcular el promedio de las temperaturas por semana
def promedio_temperaturas(temperaturas):
    promedio_semanal = []
    for region in temperaturas:
        for ciudad in region:
            for semana in ciudad:
                promedio_semana = sum(semana) / len(semana)
                promedio_semanal.append(promedio_semana)
    return promedio_semanal

# Calcular suma y promedio de temperaturas
suma_semanal = sumar_temperaturas([temperaturas_costa, temperaturas_sierra, temperaturas_oriente])
promedio_semanal = promedio_temperaturas([temperaturas_costa, temperaturas_sierra, temperaturas_oriente])

# Mostrar resultados
print("Suma de temperaturas por semana:")
print(suma_semanal)
print("\nPromedio de temperaturas por semana:")
print(promedio_semanal)
