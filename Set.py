#Crear un conjunto
Conjunto = set()

#Agregar elementos al conjunto
Conjunto.add(1)
Conjunto.add(2)
Conjunto.add(3)

#Mostrar el conjunto
print("Conjunto después de agregar elementos:", Conjunto)

#Intentar agregar un elemento duplicado (no se agregará)
Conjunto.add(2)
print("Conjunto después de intentar agregar un duplicado:", Conjunto)

#Eliminar un elemento del conjunto
Conjunto.remove(2)
print("Conjunto después de eliminar un elemento:", Conjunto)

#Verificar si un elemento está en el conjunto
print("¿Está el número 3 en el conjunto?", 3 in Conjunto)
print("¿Está el número 2 en el conjunto?", 2 in Conjunto)

#Operaciones con conjuntos
otro_conjunto = {3, 4, 5}

#Unión de conjuntos
union_conjuntos = Conjunto | otro_conjunto
print("Unión de conjuntos:", union_conjuntos)

#Intersección de conjuntos
interseccion_conjuntos = Conjunto & otro_conjunto
print("Intersección de conjuntos:", interseccion_conjuntos)

#Diferencia de conjuntos
diferencia_conjuntos = Conjunto - otro_conjunto
print("Diferencia de conjuntos:", diferencia_conjuntos)

#Diferencia simétrica de conjuntos
diferencia_simetrica_conjuntos = Conjunto ^ otro_conjunto
print("Diferencia simétrica de conjuntos:", diferencia_simetrica_conjuntos)
