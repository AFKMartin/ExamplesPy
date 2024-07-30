#Ejemplo de uso de una pila

class Stack:
    
    #Inicia la pila
    def __init__(self):
        self.items = [] #Se inicia como una lista vacía

    #Verifica si está vacía
    def is_empty(self):
        return len(self.items) == 0

    
    #Añade un elemento a la pila
    def push(self, item):
        self.items.append(item)

    #Elimina el elemento superior de la pila
    def pop(self):
        if self.is_empty():
            #Y devuelve un error si no hay nada
            raise IndexError("pop from empty stack")
        return self.items.pop()

    #Devuelve el elemento superior sin eliminarlo 
    def peek(self):
        if self.is_empty():
            #Excepción si está vacío
            raise IndexError("peek from empty stack")
        return self.items[-1]

    #Devuelve el tamaño de la pila
    def size(self):
        return len(self.items)

    #Devuelve una representación de la pila en forma de cadena
    def __str__(self):
        return str(self.items)

#Creamos una pila llamada "Mi pila"
stack = Stack()
print("Mi pila:", stack)

#Añadimos elementos a la pila (push)
stack.push(1)
stack.push(2)
#stack.push(3)
#stack.push(4)
#stack.push(5)
print("Después de push:", stack)

#Vemos el elemento superior de la pila (peek)
print("Elemento en la parte superior:", stack.peek())


#Eliminamos elementos de la pila (pop)
print("Elemento eliminado:", stack.pop())
print("Después de pop:", stack)

#Verificamos si la pila está vacía (is_empty)
print("¿La pila está vacía?:", stack.is_empty())

#Obteneemos el tamaño de la pila (size)
print("Tamaño de la pila:", stack.size())