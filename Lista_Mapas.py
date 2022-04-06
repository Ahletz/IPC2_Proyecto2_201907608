

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



    def Imprimir_Entradas(self, ciudad):

        puntero = self.primero

        indice = 1

        while puntero != None:

            if puntero.celda == 'Entrada'and puntero.nombre == ciudad:

                print(str(indice)+'. Posicion: '+' - Linea: '+str(puntero.n)+ ' - Columna: '+ str(puntero.m) +' - Estado: '+ puntero.celda)
                indice +=1
            
            puntero = puntero.Siguiente

        print()

    def Seleccion_Entrada(self, numero, ciudad, posicion): ## numero = No de civil, ciudad = ciudad pertenece, Poscion = X o Y 

        contador = 0
        puntero = self.primero

        while puntero != None:

            if puntero.celda == 'Entrada' and puntero.nombre == ciudad:

                contador +=1

            if contador == numero:

                if posicion == 1:

                    print('Posicion en y de la Entrada: '+str(puntero.m))

                    return puntero.m #retorna la columna

                elif posicion == 2:

                    print('Posicion en x de la Entrada: '+str(puntero.n))

                    return puntero.n ##retorna la fila
            
            puntero = puntero.Siguiente
        print()



    def Mision_Rescate(self,tipo, Dx, Dy, posy, posx):

        ##logaritmo de tremaux

        #variables a trabajar
        tipo = tipo #tipo de dron 
        Dx = int(Dx) #destino y
        Dy = int(Dy) #destino x
        posx =int( posx) #posicion x
        posy = int(posy )#posicion y

        exito = False

        contador = 0


        while exito == False:

            contador +=1

            ##posiciones de las celdas 
            izquierda = int(posx)-1
            abajo = int(posy) + 1
            arriba = int(posy) - 1
            derecha = int(posx) + 1

            #estados de las celdas adyacentes
            estadoI = ''
            estadoA = ''
            estadoAb = ''
            estadoD = ''

            if posx == Dx and posy == Dy:

                print(' || MISION EXITOSA ||')
                exito = True

            elif posx > Dx and posy < Dy: #si esta a la izquierda y abajo

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

                    if derecha == puntero.m and posy == puntero.n : #celda de la iquierda 

                        estadoD = puntero.celda

                    
                    elif arriba == puntero.n and posx == puntero.m : #celda de abajo

                        estadoA = puntero.celda


                    puntero = puntero.Siguiente


                if estadoA == 'Transitable':

                    posy = arriba

                elif estadoD == 'Transitable':

                    posx = derecha
                
                

            elif posx > Dx and posy > Dy:#si esta a la derecha y abajo

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

        
                    if izquierda == puntero.m and posy == puntero.n : #celda de la iquierda 

                        estadoI = puntero.celda
                    

                    elif arriba == puntero.n and posx == puntero.m : #celda de arriba

                        estadoA = puntero.celda

                    puntero = puntero.Siguiente

                if estadoA == 'Transitable':

                    posy = arriba

                elif estadoI == 'Transitable':

                    posx = izquierda



            elif posx < Dx and posy > Dy: #si esta a la izquierda arriba

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

                    if derecha == puntero.m and posy == puntero.n : #celda de la iquierda 

                        estadoD = puntero.celda

                    
                    elif abajo == puntero.n and posx == puntero.m : #celda de abajo

                        estadoAb = puntero.celda


                    puntero = puntero.Siguiente


                if estadoAb == 'Transitable':

                    posy = arriba

                elif estadoD == 'Transitable':

                    posx = derecha
                
                

            elif posx > Dx and posy > Dy: #si esta a la derecha arriba

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

        
                    if izquierda == puntero.m and posy == puntero.n : #celda de la iquierda 

                        estadoI = puntero.celda
                    

                    elif abajo == puntero.n and posx == puntero.m : #celda de arriba

                        estadoAb = puntero.celda

                    puntero = puntero.Siguiente

                if estadoAb == 'Transitable':

                    posy = arriba

                elif estadoI == 'Transitable':

                    posx = izquierda    
                
                


            elif posx == Dx and posy > Dy:#si esta abajo

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

        
                    if arriba == puntero.n and posx == puntero.m : #celda de arriba

                        estadoA = puntero.celda

                    puntero = puntero.Siguiente

                if estadoA == 'Transitable':

                    posy = arriba

                



            elif posx < Dx and posy > Dy: #si esta arriba

                puntero = self.primero

                while puntero != None: ##ciclo para encontrar los estados de las celdas adyacentes

                    
                    if abajo == puntero.n and posx == puntero.m : #celda de abajo

                        estadoAb = puntero.celda


                    puntero = puntero.Siguiente


                if estadoAb == 'Transitable':

                    posy = arriba

                
                

                

            if contador == 1000:

                print(' || MISION Fallo ||')
                exito = True




           

            

            



            









                




        
        
        