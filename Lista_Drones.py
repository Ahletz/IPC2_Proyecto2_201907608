class NodoM: ## Lista de Unidades Militares

    def __init__(self,posicionx, posiciony, poder) : ##creacion de nodo

        ##datos del dron enemigo
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.poder = poder

        self.Siguiente = None

    def __str__(self) : #volver una funcion en 

        return (self.linea, self.posicionx, self.posiciony, self.poder)

class ListaM:

    def __init__(self):

        self.primero = None
        self.tamaño = 0

    def agregarM(self, posicionx, posiciony, poder): ## linea  y nombre del dron 

        NuevoNodo = NodoM( posicionx, posiciony, poder)

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



class NodoR: ## Lista de drones de rescate

    def __init__(self,nombre) : ##creacion de nodo

        ##datos del dron aliado
        self.nombre = nombre

        self.Siguiente = None

    def __str__(self) : #volver una funcion en 

        return (self.nombre)

class ListaR:

    def __init__(self):

        self.primero = None
        self.tamaño = 0

    def agregarR(self, nombre): ## linea  y nombre del dron 

        NuevoNodo = NodoR( nombre)

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


class NodoP: ## Lista de Pelea

    def __init__(self,nombre, poder) : ##creacion de nodo

        ##datos del dron aliado
        self.nombre = nombre
        self.poder = poder

        self.Siguiente = None

    def __str__(self) : #volver una funcion en 

        return (self.nombre, self.poder)

class ListaP:

    def __init__(self):

        self.primero = None
        self.tamaño = 0

    def agregarP(self, nombre, poder): ## linea  y nombre del dron 

        NuevoNodo = NodoP(nombre, poder)

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

