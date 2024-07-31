from collections import deque

#Crear una cola con deque
cola = deque()

#Agregar elementos a la cola
cola.append('a')
cola.append('b')
cola.append('c')

#Mostrar elementos de la cola
print("Cola después de agregar elementos:", list(cola))

#Eliminar elementos de la cola
elemento = cola.popleft()
print("Elemento removido:", elemento)
print("Cola después de eliminar un elemento:", list(cola))
