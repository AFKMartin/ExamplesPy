import queue

# Crear una cola de prioridad con queue.PriorityQueue
cola_prioridad = queue.PriorityQueue()

# Agregar elementos a la cola de prioridad
cola_prioridad.put((1, 'a'))  # (prioridad, elemento)
cola_prioridad.put((3, 'c'))
cola_prioridad.put((2, 'b'))

# Mostrar elementos de la cola de prioridad (no necesariamente en orden de prioridad)
print("Cola de prioridad después de agregar elementos:", list(cola_prioridad.queue))

# Eliminar elementos de la cola de prioridad
elemento = cola_prioridad.get()
print("Elemento removido:", elemento)
print("Cola de prioridad después de eliminar un elemento:", list(cola_prioridad.queue))
