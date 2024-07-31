class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)

    def mostrar(self):
        return self.grafo

#Crear un grafo
grafo = Grafo()
grafo.agregar_nodo('A')
grafo.agregar_nodo('B')
grafo.agregar_nodo('C')
grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')

#Mostrar el grafo
print("Grafo:", grafo.mostrar())
