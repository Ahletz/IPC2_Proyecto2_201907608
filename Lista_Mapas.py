

from pkg_resources import NullProvider


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


    def Imprimir(self):

        puntero = self.primero

        while puntero != None:

            print(puntero.nombre+ ', '+str(puntero.n) + ', '+str(puntero.m) + ', '+puntero.celda)
            
            puntero = puntero.Siguiente

        print()

    def Imprimir_Civiles(self, ciudad):

        puntero = self.primero

        indice = 1

        while puntero != None:

            if puntero.celda == 'Unidad Civil'and puntero.nombre == ciudad:

                print(str(indice)+'. Posicion: '+' - Linea: '+str(puntero.n)+ ' - Columna: '+ str(puntero.m) +' - Estado: '+ puntero.celda)
                indice +=1
            
            puntero = puntero.Siguiente

        print()

    def Seleccion_Civil(self, numero, ciudad, posicion): ## numero = No de civil, ciudad = ciudad pertenece, Poscion = X o Y 

        contador = 0
        puntero = self.primero

        while puntero != None:

            if puntero.celda == 'Unidad Civil' and puntero.nombre == ciudad:

                contador +=1

            if contador == numero:

                if posicion == 1:

                    print('Posicion en x de la unidad civil: '+str(puntero.m))

                    return puntero.m #retorna la columna

                elif posicion == 2:

                    print('Posicion en y de la unidad civil: '+str(puntero.n))

                    return puntero.n ##retorna la fila
            
            puntero = puntero.Siguiente
        print()

    
    def Imprimir_Recursos(self,ciudad):

        puntero = self.primero

        indice = 1

        while puntero != None:

            if puntero.celda == 'Recurso'and puntero.nombre == ciudad:

                print(str(indice)+'. Posicion: '+' - Linea: '+str(puntero.n)+ ' - Columna: '+ str(puntero.m) +' - Estado: '+ puntero.celda)
                indice +=1
            
            puntero = puntero.Siguiente

        print()

    def Seleccion_Recurso(self, numero, ciudad, posicion): #numero = No del recurso, Ciudad = ciudad del recurso, posicion = X o Y

        contador = 0
        puntero = self.primero

        while puntero != None:

            if puntero.celda == 'Recurso' and puntero.nombre == ciudad:

                contador +=1

            if contador == numero:

                if posicion == 1:

                    print('Posicion en x del Recurso: '+str(puntero.m))

                    return puntero.m #retorna la columna

                elif posicion == 2:

                    print('Posicion en y del Recurso: '+str(puntero.n))

                    return puntero.n ##retorna la fila
            
            puntero = puntero.Siguiente
        print()
                




        
        
        