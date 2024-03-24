#vamos a crear un diccionario
informacion_personal = {
    'nombre':'iron man',
    'edad':45,
    'ciudad': 'New York',
    'profesion':'genio',
    'poderes1':'volar',
    'poderDos':'super Fuerza',
    'telefono':'0983724861',
    'equipo':'avengers'
    }
#imprimimos
print(informacion_personal)
#cambiamos las claves:
informacion_personal['ciudad']='San Francisco'
print(informacion_personal)
informacion_personal['profesion']='Armamentista'

#agregamos un nuevo elemento que no existe
informacion_personal['estatura']='alto'
print(informacion_personal)

#verifica un elemento
if 'nombre papa' in informacion_personal:
    print('su papa es tony')
else:
    print('su papa no existe')

#elimino elementos
informacion_personal.pop('edad')
# imprimo mi diccionario final despues de realizar todas las acciones solicitadas.
print(informacion_personal)

# Iterar sobre las claves del diccionario
for clave in informacion_personal.keys():
    print(clave)

