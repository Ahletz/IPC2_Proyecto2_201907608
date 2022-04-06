
from LecturaXML import * ##manejas los datos xml

class Menus:


    def __init__(self) :

        print('BIENVENIDO!!')

    def Principal(self): ##Menu principal

        print('||------------------------------------||')
        print('SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: ')
        print('||------------------------------------||')
        print('|| 1. CARGAR ARCHIVO.                 ||')
        print('|| 2. MISIONES.                       ||')
        print('|| 3. GRAFICA.                        ||')
        print('|| 4. SALIR.                          ||')
        print('||------------------------------------||\n')


    def Secundario(self): #Menu seleccion #2

        print('||------------------------------------||')
        print('|| 1. RESCATE.                        ||')
        print('|| 2. EXTRACCION.                     ||')
        print('||------------------------------------||\n')

    def Mapa(self):

        print('|| SELECCIONE EL MAPA PARA REALIZAR LA MISION ||')

    def Unidad_civil(self):

        print('|| Seleccione el Civil a Rescatar: ')

    def Recurso(self):

        print('|| Seleccione el Recurso: ')

    def Seleccion_Dron(self):

        print('|| Seleccione el dron que realizara la mision: ')

    def Punto_Entrada(self):

        print('|| Seleccione el punto de entrada: ')



    def Interaccion(self): ##selecciones usuario

        salir = False #ciclo para finalizar tarea


        Datos = Manejo()
        
        while salir == False:

            self.Principal() #llamado primer menu

            seleccion = int(input()) #variable de opcion seleccionada

            if seleccion == 1: ##CARGA DE DOCUMENTO XML

                Datos.Datos() ##manejo de los datos xml

            elif seleccion ==2: ## MISIONES

                repetir = True


                while repetir ==  True:

                    self.Secundario() ###  SELECCION DEL TIPO DE MISION

                    Tmision = int(input())

                    if Tmision == 1: ##Mision rescate civil 

                        salida1 = True

                        while salida1 == True:

                            self.Mapa() #muestra mensaje

                            Datos.Ver_Mapas() #muestra los mapas para la seleccion 

                            No_mapa = int(input()) ##guarda la seleccion del mapa

                            ciudad = Datos.Seleccion_Mapa(No_mapa) ##Nombre de la ciudad seleccionada

                            if ciudad != 'No Definida':

                                salida1 = False



                        self.Unidad_civil() #mensaje

                        Datos.Unidad_Civil(ciudad) ##muestra unidades civiles en el mapa

                        No_Civil = int(input()) ##guarda la seleccion del civil 

                        ##posciones de la unidad civil 
                        civilx = Datos.Seleccion_Civil(No_Civil,ciudad,1) 
                        civily = Datos.Seleccion_Civil(No_Civil,ciudad,2)
                        print()


                        self.Seleccion_Dron() ##muestra mensaje

                        Datos.Impresion_DronesRescate() ##muestra los drones disponibles para la mision 

                        No_Dron = int(input()) #seleccion del usuario del dron 

                        DronR = Datos.Seleccion_Dron_Rescate(No_Dron) ## nombre del dron a realizar la mision

                        print('Dron seleccionado para cumplir la mision: '+DronR)

                        print()


                        self.Punto_Entrada() #mensaje

                        ent = Datos.Entrada(ciudad) #impresion de las entradas

                        No_entrada = int(input()) #dato de la entrada

                        Entradax = Datos.Seleccion_Entrada(No_entrada,ciudad,1) #entrada en x
                        Entraday = Datos.Seleccion_Entrada(No_entrada,ciudad,2) #entrada en y

                        print()


                        print('|| PROCESO DE SELECCION TERMINADO. COMIENZO DE MISION!')

                        print()


                        Datos.Mision(DronR,civilx, civily, Entradax,Entraday)



                        repetir = False #salir del bucle
                    
                    elif Tmision == 2: ##Mision extraccion de recursos 

                        salida2 = True

                        while salida2 == True:

                            self.Mapa() #muestra mensaje

                            Datos.Ver_Mapas() #muestra los mapas para la seleccion 

                            No_mapa = int(input()) ##guarda la seleccion del mapa

                            ciudad = Datos.Seleccion_Mapa(No_mapa) ##Nombre de la ciudad seleccionada

                            if ciudad != 'No Definida':

                                salida2 = False
                        
                        self.Recurso() #mensaje 

                        Datos.Unidad_Recurso(ciudad) #muestra los recursos disponibles en el mapa

                        No_Recurso = int(input()) #ingreso del recurso deseado 

                        ##posiciones del recurso 
                        Recux = Datos.Seleccion_Recursos(No_Recurso,ciudad,1) #posicion en x
                        Recux = Datos.Seleccion_Recursos(No_Recurso,ciudad,2) #posicion en y
                        print()

                        self.Seleccion_Dron() #mensaje

                        Datos.Impresion_DronesRecolectores() #drones disponibles para la mision

                        No_DronR = int(input()) #seleccion del usuario

                        Name_Dron = Datos.Seleccion_Dron_Atk(No_DronR, 1) ##nombre del dron recolector
                        Atk_Dron = Datos.Seleccion_Dron_Atk(No_DronR, 2) ##poder del dron recolector

                        print('Dron seleccionado para cumplir la mision: '+Name_Dron)

                        print()



                        print('|| PROCESO DE SELECCION TERMINADO. COMIENZO DE MISION!')

                        print()




                        
                        repetir = False #salir del bucle
                    else:

                        print('La Opcion que ingreso no es valida')


            elif seleccion ==3: ##CRECION DE GRAPHVIZ

                print('hola')

            elif seleccion ==4: ## SALIR 

                salir = True

            else: 

                print('SELECCION NO VALIDA, VUELVA A INTRODUCIR UNA OPCION !')

            

