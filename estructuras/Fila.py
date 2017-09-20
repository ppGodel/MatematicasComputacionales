class Fila:
    def __init__(self):
        self.fila = []

    def obtener(self):
        return self.fila.pop()
    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)
    @property
    def longitud(self):
        return len(self.fila)

l = Fila()
l.meter(1)
l.meter(2)
l.meter(2)
l.meter(3)
l.meter(100)
l.meter(84563)

print(l.longitud)
print(l.obtener())
print(l.obtener())

