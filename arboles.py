import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, actual, dato):
        if dato < actual.dato:
            if actual.izquierda is None:
                actual.izquierda = Nodo(dato)
            else:
                self._insertar(actual.izquierda, dato)
        elif dato > actual.dato:
            if actual.derecha is None:
                actual.derecha = Nodo(dato)
            else:
                self._insertar(actual.derecha, dato)

    def insertar_hijo(self, padre_dato, hijo_dato):
        """Inserta un nodo hijo en el árbol en relación a un nodo padre dado."""
        nodo_padre = self.buscar_nodo(self.raiz, padre_dato)
        if nodo_padre is None:
            print(f"El nodo padre con dato {padre_dato} no existe.")
            return

        if hijo_dato < padre_dato:
            if nodo_padre.izquierda is None:
                nodo_padre.izquierda = Nodo(hijo_dato)
            else:
                print("El nodo izquierdo ya existe.")
        else:
            if nodo_padre.derecha is None:
                nodo_padre.derecha = Nodo(hijo_dato)
            else:
                print("El nodo derecho ya existe.")

    def buscar_nodo(self, actual, dato):
        """Busca un nodo con el dato dado y lo retorna."""
        if actual is None or actual.dato == dato:
            return actual
        elif dato < actual.dato:
            return self.buscar_nodo(actual.izquierda, dato)
        else:
            return self.buscar_nodo(actual.derecha, dato)

    def mostrar_arbol(self):
        self._mostrar_arbol(self.raiz, 0)

    def _mostrar_arbol(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol(nodo.derecha, nivel + 1)
            print('   ' * nivel + str(nodo.dato))
            self._mostrar_arbol(nodo.izquierda, nivel + 1)

    def buscar(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, actual, dato):
        if actual is None:
            return False
        if dato == actual.dato:
            return True
        elif dato < actual.dato:
            return self._buscar(actual.izquierda, dato)
        else:
            return self._buscar(actual.derecha, dato)

    def preorden(self):
        self._preorden(self.raiz)

    def _preorden(self, actual):
        if actual:
            print(actual.dato, end=" ")
            self._preorden(actual.izquierda)
            self._preorden(actual.derecha)

    def inorden(self):
        self._inorden(self.raiz)

    def _inorden(self, actual):
        if actual:
            self._inorden(actual.izquierda)
            print(actual.dato, end=" ")
            self._inorden(actual.derecha)

    def postorden(self):
        self._postorden(self.raiz)

    def _postorden(self, actual):
        if actual:
            self._postorden(actual.izquierda)
            self._postorden(actual.derecha)
            print(actual.dato, end=" ")

    def recorrido_por_niveles(self):
        if self.raiz is None:
            return
        cola = deque([self.raiz])
        while cola:
            nodo_actual = cola.popleft()
            print(nodo_actual.dato, end=" ")
            if nodo_actual.izquierda:
                cola.append(nodo_actual.izquierda)
            if nodo_actual.derecha:
                cola.append(nodo_actual.derecha)
        print()

    def graficar_arbol(self):
        if self.raiz is None:
            print("El árbol está vacío.")
            return

        # Crear un gráfico vacío y un grafo de networkx
        G = nx.DiGraph()
        posiciones = {}
        
        # Función auxiliar para añadir nodos y bordes al grafo
        def agregar_nodos_edges(nodo, pos_x=0, pos_y=0, nivel=0, espaciado=1.5):
            if nodo is not None:
                G.add_node(nodo.dato)
                posiciones[nodo.dato] = (pos_x, pos_y)
                
                if nodo.izquierda:
                    G.add_edge(nodo.dato, nodo.izquierda.dato)
                    agregar_nodos_edges(nodo.izquierda, pos_x - espaciado, pos_y - 1, nivel + 1, espaciado / 1.5)
                if nodo.derecha:
                    G.add_edge(nodo.dato, nodo.derecha.dato)
                    agregar_nodos_edges(nodo.derecha, pos_x + espaciado, pos_y - 1, nivel + 1, espaciado / 1.5)

        # Llamar a la función para agregar nodos y bordes
        agregar_nodos_edges(self.raiz)

        # Dibujar el grafo usando networkx y matplotlib
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos=posiciones, with_labels=True, arrows=False, node_size=2000, node_color="lightblue", font_size=10)
        plt.title("Árbol Binario de Búsqueda")
        plt.show()

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, actual):
        if actual is None:
            return 0
        return 1 + max(self._altura(actual.izquierda), self._altura(actual.derecha))

    def cantidad_nodos(self):
        return self._cantidad_nodos(self.raiz)

    def _cantidad_nodos(self, actual):
        if actual is None:
            return 0
        return 1 + self._cantidad_nodos(actual.izquierda) + self._cantidad_nodos(actual.derecha)

    def cantidad_hojas(self):
        return self._cantidad_hojas(self.raiz)

    def _cantidad_hojas(self, actual):
        if actual is None:
            return 0
        if actual.izquierda is None and actual.derecha is None:
            return 1
        return self._cantidad_hojas(actual.izquierda) + self._cantidad_hojas(actual.derecha)

    def es_completo(self):
        if self.raiz is None:
            return True
        cola = deque([self.raiz])
        encontrado_vacio = False
        while cola:
            actual = cola.popleft()
            if actual.izquierda:
                if encontrado_vacio:
                    return False
                cola.append(actual.izquierda)
            else:
                encontrado_vacio = True
            if actual.derecha:
                if encontrado_vacio:
                    return False
                cola.append(actual.derecha)
            else:
                encontrado_vacio = True
        return True

    def es_lleno(self):
        if self.raiz is None:
            return True
        nivel_actual = deque([self.raiz])
        nivel_siguiente = deque()
        while nivel_actual:
            for nodo in nivel_actual:
                if not nodo.izquierda and nodo.derecha:
                    return False
                if nodo.izquierda:
                    nivel_siguiente.append(nodo.izquierda)
                if nodo.derecha:
                    nivel_siguiente.append(nodo.derecha)
            if len(nivel_actual) != 2**len(nivel_siguiente):
                return False
            nivel_actual, nivel_siguiente = nivel_siguiente, deque()
        return True

    def eliminar_arbol(self):
        self.raiz = None
        print("Árbol eliminado.")

def menu():
    arbol = ArbolBinarioBusqueda()
    while True:
        print("\n--- MENÚ ÁRBOL BINARIO DE BÚSQUEDA ---")
        print("1. Insertar elemento")
        print("2. Insertar hijo")
        print("3. Mostrar árbol completo acostado con la raíz a la izquierda")
        print("4. Graficar árbol completo")
        print("5. Buscar un elemento en el árbol")
        print("6. Recorrer el árbol en PreOrden")
        print("7. Recorrer el árbol en InOrden")
        print("8. Recorrer el árbol en PostOrden")
        print("9. Eliminar un nodo (Predecesor)")
        print("10. Eliminar un nodo (Sucesor)")
        print("11. Recorrer el árbol por niveles (Amplitud)")
        print("12. Altura del árbol")
        print("13. Cantidad de hojas")
        print("14. Cantidad de nodos")
        print("15. Revisar si el árbol es completo")
        print("16. Revisar si el árbol es lleno")
        print("17. Eliminar todo el árbol")
        print("18. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            dato = int(input("Ingresa el número a insertar: "))
            arbol.insertar(dato)
        elif opcion == 2:
            padre_dato = int(input("Número del nodo padre: "))
            hijo_dato = int(input("Número del nodo hijo a insertar: "))
            arbol.insertar_hijo(padre_dato, hijo_dato)
        elif opcion == 3:
            arbol.mostrar_arbol()
        elif opcion == 4:
            arbol.graficar_arbol()
        elif opcion == 5:
            dato = int(input("Número a buscar: "))
            encontrado = arbol.buscar(dato)
            print(f"Elemento {'encontrado' if encontrado else 'no encontrado'}")
        elif opcion == 6:
            print("Recorrido PreOrden: ", end="")
            arbol.preorden()
            print()
        elif opcion == 7:
            print("Recorrido InOrden: ", end="")
            arbol.inorden()
            print()
        elif opcion == 8:
            print("Recorrido PostOrden: ", end="")
            arbol.postorden()
            print()
        elif opcion == 9:
            dato = int(input("Nodo a eliminar (Predecesor): "))
            arbol.eliminar(dato, metodo="predecesor")
        elif opcion == 10:
            dato = int(input("Nodo a eliminar (Sucesor): "))
            arbol.eliminar(dato, metodo="sucesor")
        elif opcion == 11:
            print("Recorrido por niveles: ", end="")
            arbol.recorrido_por_niveles()
        elif opcion == 12:
            print(f"Altura del árbol: {arbol.altura()}")
        elif opcion == 13:
            print(f"Cantidad de hojas: {arbol.cantidad_hojas()}")
        elif opcion == 14:
            print(f"Cantidad de nodos: {arbol.cantidad_nodos()}")
        elif opcion == 15:
            completo = arbol.es_completo()
            print(f"El árbol {'es' if completo else 'no es'} completo.")
        elif opcion == 16:
            lleno = arbol.es_lleno()
            print(f"El árbol {'es' if lleno else 'no es'} lleno.")
        elif opcion == 17:
            arbol.eliminar_arbol()
        elif opcion == 18:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, por favor intenta nuevamente.")
menu()
