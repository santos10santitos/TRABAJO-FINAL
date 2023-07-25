from PIL import Image
class Nodo:
    def __init__(self, id):
        self.id = id
        self.adyacentes = []

    def agregar_arista(self, destino, peso):
        self.adyacentes.append((destino, peso))

class PriorityQueue:
    def __init__(self):
        self.cola = []

    def agregar(self, item, prioridad):
        self.cola.append((prioridad, item))

    def pop(self):
        indice_min = 0
        for i in range(1, len(self.cola)):
            if self.cola[i][0] < self.cola[indice_min][0]:
                indice_min = i
        return self.cola.pop(indice_min)[1]

    def esta_vacia(self):
        return len(self.cola) == 0

def dijkstra(nodo_inicial, nodo_final):
    
    distancias = {nodo: float('inf') for nodo in obtener_todos_los_nodos(nodo_inicial)}
    distancias[nodo_inicial] = 0

    
    padres = {nodo: None for nodo in obtener_todos_los_nodos(nodo_inicial)}

   
    cola_prioridad = PriorityQueue()
    cola_prioridad.agregar(nodo_inicial, 0)

    
    while not cola_prioridad.esta_vacia():
        nodo_actual = cola_prioridad.pop()

        if nodo_actual == nodo_final:
            break

        for arista in nodo_actual.adyacentes:
            nodo_destino = arista[0]
            peso_arista = arista[1]
            nueva_distancia = distancias[nodo_actual] + peso_arista
            if nueva_distancia < distancias[nodo_destino]:
                distancias[nodo_destino] = nueva_distancia
                padres[nodo_destino] = nodo_actual
                cola_prioridad.agregar(nodo_destino, nueva_distancia)

 
    distancia_total = distancias[nodo_final]
    print(f"Distancia más corta desde el nodo {nodo_inicial.id} al nodo {nodo_final.id}: {distancia_total}")


    nodo_actual = nodo_final
    camino = [nodo_actual]
    while nodo_actual != nodo_inicial:
        nodo_actual = padres[nodo_actual]
        camino.insert(0, nodo_actual)
    print("Camino más corto:")
    for nodo in camino:
        print(nodo.id, end=" -> ")
    print()

def obtener_todos_los_nodos(nodo_inicial):
    nodos = set()
    cola = [nodo_inicial]

    while cola:
        nodo = cola.pop()
        nodos.add(nodo)

        for arista in nodo.adyacentes:
            nodo_destino = arista[0]
            if nodo_destino not in nodos:
                cola.append(nodo_destino)

    return nodos


nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo8 = Nodo(8)
nodo9 = Nodo(9)
nodo10 = Nodo(10)
nodo11 = Nodo(11)
nodo12 = Nodo(12)
nodo13 = Nodo(13)
nodo14 = Nodo(14)
nodo15 = Nodo(15)
nodo16 = Nodo(16)
nodo17 = Nodo(17)
nodo18 = Nodo(18)
nodo19 = Nodo(19)
nodo20 = Nodo(20)
nodo21 = Nodo(21)
nodo22 = Nodo(22)
nodo23 = Nodo(23)
nodo24 = Nodo(24)
nodo25 = Nodo(25)
nodo26 = Nodo(26)
nodo27 = Nodo(27)
nodo28 = Nodo(28)
nodo29 = Nodo(29)


nodo1.agregar_arista(nodo2, 60)
nodo2.agregar_arista(nodo1, 60)

nodo1.agregar_arista(nodo6, 55)
nodo6.agregar_arista(nodo1, 55)

nodo2.agregar_arista(nodo3, 60)
nodo3.agregar_arista(nodo2, 60)

nodo3.agregar_arista(nodo4, 97)
nodo4.agregar_arista(nodo3, 97)

nodo4.agregar_arista(nodo5, 72)
nodo5.agregar_arista(nodo4, 72)

nodo2.agregar_arista(nodo8, 55)
nodo8.agregar_arista(nodo2, 55)

nodo3.agregar_arista(nodo9, 55)
nodo9.agregar_arista(nodo3, 55)

nodo4.agregar_arista(nodo10, 55)
nodo10.agregar_arista(nodo4, 55)

nodo11.agregar_arista(nodo5, 55)
nodo5.agregar_arista(nodo11, 55)

nodo6.agregar_arista(nodo7, 25)
nodo7.agregar_arista(nodo6, 25)

nodo7.agregar_arista(nodo8, 30)
nodo8.agregar_arista(nodo7, 30)

nodo8.agregar_arista(nodo9, 42)
nodo9.agregar_arista(nodo8, 42)

nodo9.agregar_arista(nodo10, 97)
nodo10.agregar_arista(nodo9, 97)

nodo10.agregar_arista(nodo11, 72)
nodo11.agregar_arista(nodo10, 72)

nodo11.agregar_arista(nodo5, 55)
nodo5.agregar_arista(nodo11, 55)

nodo12.agregar_arista(nodo6, 55)
nodo6.agregar_arista(nodo12, 55)

nodo7.agregar_arista(nodo13, 55)
nodo13.agregar_arista(nodo7, 55)

nodo9.agregar_arista(nodo15, 55)
nodo15.agregar_arista(nodo9, 55)

nodo11.agregar_arista(nodo18, 55)
nodo18.agregar_arista(nodo11, 55)

nodo12.agregar_arista(nodo13, 28)
nodo13.agregar_arista(nodo12, 28)

nodo13.agregar_arista(nodo14, 30)
nodo13.agregar_arista(nodo14, 30)

nodo14.agregar_arista(nodo15, 42)
nodo15.agregar_arista(nodo14, 42)

nodo16.agregar_arista(nodo15, 67)
nodo15.agregar_arista(nodo16, 67)

nodo16.agregar_arista(nodo17, 42)
nodo17.agregar_arista(nodo16, 42)

nodo18.agregar_arista(nodo17, 50)
nodo17.agregar_arista(nodo18, 50)

nodo18.agregar_arista(nodo29, 110)
nodo29.agregar_arista(nodo18, 110)

nodo29.agregar_arista(nodo28, 50)
nodo28.agregar_arista(nodo29, 50)

nodo23.agregar_arista(nodo28, 55)
nodo28.agregar_arista(nodo23, 55)

nodo23.agregar_arista(nodo17, 55)
nodo17.agregar_arista(nodo23, 55)

nodo23.agregar_arista(nodo22, 42)
nodo22.agregar_arista(nodo23, 42)

nodo16.agregar_arista(nodo22, 55)
nodo22.agregar_arista(nodo16, 55)

nodo27.agregar_arista(nodo22, 55)
nodo22.agregar_arista(nodo27, 55)

nodo27.agregar_arista(nodo28, 42)
nodo28.agregar_arista(nodo27, 42)

nodo27.agregar_arista(nodo26, 67)
nodo26.agregar_arista(nodo27, 67)

nodo21.agregar_arista(nodo26, 55)
nodo26.agregar_arista(nodo21, 55)

nodo21.agregar_arista(nodo22, 67)
nodo22.agregar_arista(nodo21, 67)

nodo21.agregar_arista(nodo15, 55)
nodo15.agregar_arista(nodo21, 55)

nodo21.agregar_arista(nodo20, 60)
nodo20.agregar_arista(nodo21, 60)

nodo14.agregar_arista(nodo20, 65)
nodo20.agregar_arista(nodo14, 65)

nodo13.agregar_arista(nodo20, 65)
nodo20.agregar_arista(nodo13, 65)

nodo25.agregar_arista(nodo20, 55)
nodo20.agregar_arista(nodo25, 55)

nodo25.agregar_arista(nodo26, 60)
nodo26.agregar_arista(nodo25, 60)

nodo25.agregar_arista(nodo24, 60)
nodo24.agregar_arista(nodo25, 60)

nodo19.agregar_arista(nodo24, 55)
nodo24.agregar_arista(nodo19, 55)

nodo19.agregar_arista(nodo12, 55)
nodo12.agregar_arista(nodo19, 55)

nodo19.agregar_arista(nodo20, 60)
nodo20.agregar_arista(nodo19, 60)


nodos = {nodo1, nodo2, nodo3, nodo4, nodo5, nodo6, nodo7, nodo8, nodo9, nodo10, nodo11, nodo12, nodo13, nodo14,
          nodo15, nodo16, nodo17, nodo18, nodo19, nodo20, nodo21, nodo22, nodo23, nodo24, nodo25, nodo26, nodo27, nodo28, nodo29}


nodo_inicial = int(input("Ingrese el número del nodo inicial: "))
nodo_final = int(input("Ingrese el número del nodo final: "))


nodo_inicial = next((nodo for nodo in nodos if nodo.id == nodo_inicial), None)
nodo_final = next((nodo for nodo in nodos if nodo.id == nodo_final), None)

if nodo_inicial is not None and nodo_final is not None:

    dijkstra(nodo_inicial, nodo_final)
else:
    print("Nodo inicial o nodo final no válido.")

im = Image.open('foto.jpeg')
  
im.show()