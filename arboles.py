import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        def _insertar(actual, dato):
            if dato < actual.dato:
                actual.izquierda = Nodo(dato) if actual.izquierda is None else _insertar(actual.izquierda, dato)
            elif dato > actual.dato:
                actual.derecha = Nodo(dato) if actual.derecha is None else _insertar(actual.derecha, dato)
            return actual
        self.raiz = Nodo(dato) if self.raiz is None else _insertar(self.raiz, dato)

    def insertar_hijo(self, padre_dato, hijo_dato):
        """Inserta un nodo hijo en el árbol en relación a un nodo padre dado."""
        nodo_padre = self.buscar_nodo(self.raiz, padre_dato)
        if nodo_padre:
            lado = 'izquierda' if hijo_dato < padre_dato else 'derecha'
            if getattr(nodo_padre, lado) is None:
                setattr(nodo_padre, lado, Nodo(hijo_dato))
            else:
                print(f"El nodo {lado} ya existe.")
        else:
            print(f"El nodo padre con dato {padre_dato} no existe.")

    def buscar_nodo(self, actual, dato):
        """Busca un nodo con el dato dado y lo retorna."""
        if actual is None or actual.dato == dato:
            return actual
        elif dato < actual.dato:
            return self.buscar_nodo(actual.izquierda, dato)
        else:
            return self.buscar_nodo(actual.derecha, dato)

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

    def graficar_arbol(self):
        if not self.raiz:
            return print("El árbol está vacío.")
        
        G, posiciones = nx.DiGraph(), {}
        def agregar_nodos(nodo, x=0, y=0, espaciado=1.5):
            if nodo:
                G.add_node(nodo.dato, pos=(x, y))
                if nodo.izquierda:
                    G.add_edge(nodo.dato, nodo.izquierda.dato)
                    agregar_nodos(nodo.izquierda, x - espaciado, y - 1, espaciado / 1.5)
                if nodo.derecha:
                    G.add_edge(nodo.dato, nodo.derecha.dato)
                    agregar_nodos(nodo.derecha, x + espaciado, y - 1, espaciado / 1.5)
        
        agregar_nodos(self.raiz)
        posiciones = {n: d['pos'] for n, d in G.nodes(data=True)}
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos=posiciones, with_labels=True, node_size=2000, node_color="mediumpurple", font_size=10)
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
        if not self.raiz:
            return True
        nivel = deque([self.raiz])
        while nivel:
            siguiente_nivel = deque(n for nodo in nivel for n in (nodo.izquierda, nodo.derecha) if n)
            if any(nodo.derecha and not nodo.izquierda for nodo in nivel) or len(nivel) != 2 ** len(siguiente_nivel):
                return False
            nivel = siguiente_nivel
        return True

    def eliminar_arbol(self):
        self.raiz = None
        print("Árbol eliminado.")

def menu():
    arbol = ArbolBusqueda()
    while True:
        print("\n--- MENÚ ÁRBOL BINARIO DE BÚSQUEDA ---")
        print("1. Insertar elemento \n2. Insertar hijo")
        print("3. Graficar árbol completo")
        print("4. Buscar un elemento en el árbol \n5. Recorrer el árbol en PreOrden")
        print("6. Recorrer el árbol en InOrden \n7. Recorrer el árbol en PostOrden")
        print("8. Eliminar un nodo (Predecesor) \n9. Eliminar un nodo (Sucesor)")
        print("10. Recorrer el árbol por niveles \n11. Altura del árbol")
        print("12. Cantidad de hojas \n13. Cantidad de nodos")
        print("14. Revisar si el árbol es completo \n15. Revisar si el árbol es lleno")
        print("16. Eliminar todo el árbol \n17. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            dato = int(input("Ingresa el número a insertar: "))
            arbol.insertar(dato)
        elif opcion == 2:
            padre_dato = int(input("Número del nodo padre: "))
            hijo_dato = int(input("Número del nodo hijo a insertar: "))
            arbol.insertar_hijo(padre_dato, hijo_dato)
        elif opcion == 3:
            arbol.graficar_arbol()
        elif opcion == 4:
            dato = int(input("Número a buscar: "))
            encontrado = arbol.buscar(dato)
            print(f"Elemento {'encontrado' if encontrado else 'no encontrado'}")
        elif opcion == 5:
            print("Recorrido PreOrden: ", end="")
            arbol.preorden()
            print()
        elif opcion == 6:
            print("Recorrido InOrden: ", end="")
            arbol.inorden()
            print()
        elif opcion == 7:
            print("Recorrido PostOrden: ", end="")
            arbol.postorden()
            print()
        elif opcion == 8:
            dato = int(input("Nodo a eliminar (Predecesor): "))
            arbol.eliminar(dato, metodo="predecesor")
        elif opcion == 9:
            dato = int(input("Nodo a eliminar (Sucesor): "))
            arbol.eliminar(dato, metodo="sucesor")
        elif opcion == 10:
            print("Recorrido por niveles: ", end="")
            arbol.recorrido_por_niveles()
        elif opcion == 11:
            print(f"Altura del árbol: {arbol.altura()}")
        elif opcion == 12:
            print(f"Cantidad de hojas: {arbol.cantidad_hojas()}")
        elif opcion == 13:
            print(f"Cantidad de nodos: {arbol.cantidad_nodos()}")
        elif opcion == 14:
            completo = arbol.es_completo()
            print(f"El árbol {'es' if completo else 'no es'} completo.")
        elif opcion == 15:
            lleno = arbol.es_lleno()
            print(f"El árbol {'es' if lleno else 'no es'} lleno.")
        elif opcion == 16:
            arbol.eliminar_arbol()
        elif opcion == 17:
            print("Saliendo...")
            break
        else:
            print("Opción inválida, por favor intenta nuevamente.")
menu()
