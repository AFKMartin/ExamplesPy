import queue

# Crear una cola con queue.Queue
cola = queue.Queue()

# Agregar elementos a la cola
cola.put('a')
cola.put('b')
cola.put('c')

# Mostrar elementos de la cola
print("Cola después de agregar elementos:", list(cola.queue))

# Eliminar elementos de la cola
elemento = cola.get()
print("Elemento removido:", elemento)
print("Cola después de eliminar un elemento:", list(cola.queue))
