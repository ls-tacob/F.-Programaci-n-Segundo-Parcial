#conjuntos
conjunto = set()
conjunto = {1,12,2,3,"hola",4.55,True,1,2}
#recuerda que solo lee una sola ves cada elemento en caso de que haya repetidos
#no puede haber elementos duplicados
matriz = [1,2,3,7,8,9]
#agregar elementos al conjunto
conjunto.add(9)
#eliminar los elementos del conjunto
conjunto.discard(2)
#para limpiar se utiliza conjunto.clear

#pregunto un boleano en negacion. jeje
print(4.55 not in conjunto)

#union de elementos

# Definir dos conjuntos
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Obtener la unión de los conjuntos
union_set = set1.union(set2)

# Imprimir el resultado
print(union_set)
