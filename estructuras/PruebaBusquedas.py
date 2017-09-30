class Fila:
    def __init__(self):
        self.fila= []
    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

class Pila:
    def __init__(self):
        self.pila= []
    def obtener(self):
        return self.pila.pop()
    def meter(self,e):
        self.pila.append(e)
        return len(self.pila)
    @property
    def longitud(self):
        return len(self.pila)


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


def DFS(g,ni):
	visitados =[]
	f=Pila()
	f.meter(ni)
	while(f.longitud>0):
		na =f.obtener()
		visitados.append(na)
		ln = g.vecinos[na]
		for nodo in ln:
			if nodo not in visitados:
				f.meter(nodo)
	return visitados

def BFS(g,ni):
	visitados =[]
	f=Fila()
	f.meter(ni)
	while(f.longitud>0):
		na =f.obtener()
		visitados.append(na)
		ln = g.vecinos[na]
		for nodo in ln:
			if nodo not in visitados:
				f.meter(nodo)
	return visitados


g= Grafo()
g.conecta('a','b',3)
g.conecta('a','c',3)
g.conecta('a','d',a)
g.conecta('a','d',2)
g.conecta('b','e',2)
g.conecta('b','f',2)
g.conecta('c','g',2)
g.conecta('e','h',2)

BFS(g,'a')
DFS(g,'b')
