# Creamos un nuevo archivo llamado my_notes.txt en modo de escritura ('w')
my_notes = open('my_notes.txt', 'w')

# Escribimos al menos tres líneas de notas personales en el archivo
my_notes.write("Nota 1: Este es un recordatorio importante.\n")
my_notes.write("Nota 2: No olvides completar la tarea para mañana.\n")
my_notes.write("Nota 3: Revisar el correo electrónico antes de salir.\n")

# Cerramos el archivo
my_notes.close()

# Abrimos el archivo
my_notes = open('my_notes.txt', 'r')

# Leemos el contenido del archivo línea por línea utilizando readline()
# y mostramos cada línea en la consola
print("Contenido del archivo my_notes.txt:")
linea = my_notes.readline()  # leemos la primera línea
while linea:
    print(linea.strip())  # strip() para eliminar caracteres de nueva línea
    linea = my_notes.readline()  # leemos la siguiente línea

# Cerramos el archivo después de leer
my_notes.close()

# Ahora vamos a trabajar con el archivo my_notes3.txt
# Creamos un nuevo archivo llamado my_notes3.txt en modo de escritura ('w')
my_notes3 = open('my_notes3.txt', 'w')

# Escribimos al menos tres líneas de notas personales en el archivo
my_notes3.write("Nota 1: Toma mucha agua el día de hoy..\n")
my_notes3.write("Nota 2: Enfocate en terminar tus tareas.\n")
my_notes3.write("Nota 3: realiza una a la vez.\n")

# Cerramos el archivo después de escribir
my_notes3.close()

# Abrimos el archivo my_notes3.txt en modo de lectura ('r')
my_notes3 = open('my_notes3.txt', 'r')

# Leemos el contenido del archivo utilizando un bucle for
print("\nContenido del archivo my_notes3.txt:")
for linea in my_notes3:
    print(linea.strip())  # strip() para eliminar caracteres de nueva línea

# Cerramos el archivo después de leer
my_notes3.close()
