class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar(nodo.derecho, valor)

    def inorder(self, nodo):
        return (self.inorder(nodo.izquierdo) + [nodo.valor] + self.inorder(nodo.derecho)) if nodo else []

    def mostrar(self):
        return self.inorder(self.raiz)

#Crear un árbol binario
arbol = ArbolBinario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)

#Mostrar el recorrido en inorden del árbol
print("Recorrido en inorden del árbol binario:", arbol.mostrar())
