#Crear un diccionario
mi_diccionario = {
    'nombre': 'Javier',
    'edad': 20,
    'ciudad': 'Santa Cruz de Tenerife'
}

#Mostrar el diccionario
print("Diccionario:", mi_diccionario)

#Acceder a un valor mediante una clave
nombre = mi_diccionario['nombre']
print("Nombre:", nombre)

#Agregar un nuevo par clave-valor
mi_diccionario['profesión'] = 'Ingeniero'
print("Diccionario después de agregar la clave 'profesión':", mi_diccionario)

#Modificar un valor existente
mi_diccionario['edad'] = 21
print("Diccionario después de modificar el valor 'edad':", mi_diccionario)

#Eliminar un par clave-valor
del mi_diccionario['ciudad']
print("Diccionario después de eliminar la clave 'ciudad':", mi_diccionario)

#Comprobar si una clave existe en el diccionario
existe_nombre = 'nombre' in mi_diccionario
print("¿Existe la clave 'nombre'?", existe_nombre)

#Iterar sobre las claves del diccionario
print("Claves en el diccionario:")
for clave in mi_diccionario:
    print(clave)

#Iterar sobre los valores del diccionario
print("Valores en el diccionario:")
for valor in mi_diccionario.values():
    print(valor)

#Iterar sobre los pares clave-valor del diccionario
print("Pares clave-valor en el diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

#Obtener un valor de manera segura con get()
ciudad = mi_diccionario.get('ciudad', 'No disponible')
print("Ciudad:", ciudad)

#Crear un diccionario a partir de una lista de tuplas
lista_de_tuplas = [('a', 1), ('b', 2), ('c', 3)]
diccionario_desde_tuplas = dict(lista_de_tuplas)
print("Diccionario creado desde una lista de tuplas:", diccionario_desde_tuplas)
