

class Nodo: ##lista de mapas

    def __init__(self, n, m, celda, nombre) : ##creacion de nodo

        self.n = n  #posicion linea  
        self.m = m #posicion columna
        self.celda = celda  # transitable, intransitable, civil, entrada, recurso o Unidad militar
        self.nombre = nombre ##nombre del mapa

        self.Siguiente = None

    def __str__(self) : #volver una funcion en string

        return (self.n, self.m, self.celda, self.nombre)

class Lista:

    def __init__(self):

        self.primero = None
        self.tamaño = 0

    def agregarL(self, n, m, celda, nombre): ## linea  y nombre del mapa 

        NuevoNodo = Nodo(n, m, celda, nombre)

        if self.tamaño == 0:

            self.primero = NuevoNodo

        else: 

            current = self.primero

            while current.Siguiente != None:

                current = current.Siguiente

            current.Siguiente = NuevoNodo
        
        self.tamaño+=1

        return NuevoNodo

    def TL(self): #tamaño de la lista
        return self.Tamaño


        
        
        