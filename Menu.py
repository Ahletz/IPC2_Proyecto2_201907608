from Archivo import *

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

    def Interaccion(self): ##selecciones usuario

        salir = False #ciclo para finalizar tarea

        llamado = Carga() ##lamado metodo de carga de archivos
        
        while salir == False:

            self.Principal() #llamado primer menu

            seleccion = int(input()) #variable de opcion seleccionada

            if seleccion == 1: ##CARGA DE DOCUMENTO XML

                llamado.AbrirVentana()

            elif seleccion ==2: ## MISIONES

                self.Secundario() ###  SELECCION DEL TIPO DE MISION

                Tmision = int(input())

            elif seleccion ==3: ##CRECION DE GRAPHVIZ

                print('hola')

            elif seleccion ==4: ## SALIR 

                salir = True

            else: 

                print('SELECCION NO VALIDA, VUELVA A INTRODUCIR UNA OPCION !')

            

