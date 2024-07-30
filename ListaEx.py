# Crear una lista
numeros = [1, 2, 3, 4, 5]

# Acceder a elementos
print("Primer elemento:", numeros[0])  # Salida: 1
print("Último elemento:", numeros[4])  # Salida: 5

# Modificar elementos
numeros[4] = 10
print("Lista después de modificar el último elemento:", numeros)

# Agregar elementos
numeros.append(1)
numeros.append(22)
numeros.insert(2, 20)
print("Lista después de agregar elementos:", numeros)

# Eliminar elementos
numeros.remove(1)
numeros.remove(1)
ultimo_elemento = numeros.pop()
print("Lista después de eliminar elementos:", numeros)
print("Último elemento eliminado:", ultimo_elemento)

# Iterar sobre la lista
print("Elementos de la lista:")
for numero in numeros:
    print(numero)

# Usar otros métodos
tamaño = len(numeros)
numeros_ordenados = sorted(numeros)
numeros_copia = numeros.copy()

print("Tamaño de la lista:", tamaño)
print("Lista ordenada:", numeros_ordenados)
print("Copia de la lista:", numeros_copia)
