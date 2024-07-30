#Ejemplo de uso de una pila

class Stack:
    
    #Inicia la pila
    def __init__(self):
        self.items = [] #Se inicia como una lista vacía (1)

    #Verifica si está vacía
    def is_empty(self):
        return len(self.items) == 0

    
    #Añade un elemento a la pila (2)
    def push(self, item):
        self.items.append(item)

    #Elimina el elemento superior de la pila
    def pop(self):
        if self.is_empty():
            #Y devuelve un error si no hay nada
            raise IndexError("pop from empty stack")
        return self.items.pop()

    #Devuelve el elemento superior sin eliminarlo (3)
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

#Añadimos elementos a la pila (push) (2)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print("Después de push:", stack) 

#Vemos el elemento superior de la pila (peek) (3)
print("Elemento en la parte superior:", stack.peek()) 


#Eliminamos elementos de la pila (pop) (4) (5)
print("Elemento eliminado:", stack.pop())
print("Después de pop:", stack)

#Verificamos si la pila está vacía (is_empty) (6)
print("¿La pila está vacía?:", stack.is_empty())

#Obteneemos el tamaño de la pila (size) (7)
print("Tamaño de la pila:", stack.size())

"""
El resultado debe ser el siguiente:

Mi pila: [] (1) Debido a que inicialmente la pila está vacía.
Después de push: [1, 2, 3, 4, 5] (2) Hacemos stack.push(n) para añadir valores a la pila, por eso nos devuelve esto.
Elemento en la parte superior: 5 (3) Devuelve el elemento de la parte de arriba, en nuestro caso, 5.
Elemento eliminado: 5 (4) Elimina el elemento de la parte de arriba y te da el elemento eliminado, en nuestro caso, 5.
Después de pop: [1, 2, 3, 4] (5) Te da el estado de la pila después de hacer pop al 5.
¿La pila está vacía?: False (6) Solo devuelve "True" Cuando no hay ningún elemento, si comentamos la parte (2) menos el primer push, aquí nos devolverá True.
Tamaño de la pila: 4 (7) La pila tiene los valores 1,2,3 y 4. Ergo su tamaño es 4.
"""
