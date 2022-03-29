class NodoM: ## Lista de Unidades Militares

    def __init__(self,posicionx, posiciony, poder, mapa) : ##creacion de nodo

        ##datos del dron enemigo
        self.posicionx = posicionx
        self.posiciony = posiciony
        self.poder = poder
        self.mapa = mapa

        self.Siguiente = None

    def __str__(self) : #volver una funcion en 

        return (self.linea, self.posicionx, self.posiciony, self.poder, self.mapa)

class ListaM:

    def __init__(self):

        self.primero = None
        self.tamaño = 0

    def agregarM(self, posicionx, posiciony, poder, mapa): ## linea  y nombre del dron 

        NuevoNodo = NodoM( posicionx, posiciony, poder, mapa)

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


    def Imprimir(self):

        puntero = self.primero

        while puntero != None:

         print(str(puntero.posicionx)+', '+str(puntero.posiciony)+', '+str(puntero.poder)+puntero.mapa)

         puntero = puntero.Siguiente

        print()



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

    def Imprimir(self):

        puntero = self.primero

        while puntero != None:

         print(puntero.nombre)

         puntero = puntero.Siguiente

        print()


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

    def Imprimir(self):

        puntero = self.primero

        while puntero != None:

         print(puntero.nombre+', '+str(puntero.poder))

         puntero = puntero.Siguiente

        print()

