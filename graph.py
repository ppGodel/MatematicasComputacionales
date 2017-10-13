def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() # un conjunto
        self.E = dict() # un mapeo de pesos de aristas
        self.vecinos = dict() # un mapeo
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: # vecindad de v
            self.vecinos[v] = set() # inicialmente no tiene nada
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso # en ambos sentidos
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

	def shortest(self, v, w): # Dijkstra's algorithm
			q = [(0, v, ())] # arreglo "q" de las "Tuplas" de lo que se va a almacenar dondo 0 es la distancia, v el nodo y () el "camino" hacia el
			visited = set() #Conjunto de visitados
			while len(q) > 0: #mientras exista un nodo pendiente
				(l, u, p) = heappop(q) # Se toma la tupla con la distancia menor
				if u not in visited: # si no lo hemos visitado
					visited.add(u) #se agrega a visitados
					if u == w: #si es el nodo final#
						return list(flatten(p))[::-1] + [u] #se regresa el camino
				p = (u, p) #Tupla del nodo y el camino
				for n in self[u].neighbors: #Para cada hijo del nodo actual
					if n not in visited: #si no lo hemos visitado
						el = self.vecinos[u][n] #se toma la distancia del nodo acutal hacia el nodo hijo
						heappush(q, (l + el, n, p)) #Se agrega al arreglo "q" la distancia actual mas la ditanacia hacia el nodo hijo, el nodo hijo n hacia donde se va, y el camino
			return None