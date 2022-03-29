from xml.dom import minidom
from Archivo import Carga

from Lista_Mapas import * ##importar clases de listas de mapas

from Lista_Drones import * #importar clases de listas de drones

llamado = Carga() ## llamado ventana de carga para obtener la direccion
listas = Lista() ##llamado listas de mapas

DronesM = ListaM() ##importar lista de unidades militares 
DronesR = ListaR() ##importar lista drones de rescate
DronesP = ListaP() ##importar lista de drones de recoleccion

class Manejo :


    def Datos (self):

        llamado.AbrirVentana()

        direccion = llamado.direccion #obtencion de direccion de archivo xml 

        if direccion == '':

            print('NO SE HA CARGADO NINGUN ARCHIVO XML') #en caso de no haber cargado un archivo 

        else:

            doc = minidom.parse(direccion)
            
            ##obtener los datos del piso

            Ciudades = doc.getElementsByTagName("listaCiudades") ##obtener las ciudaddes dentro de la lista de ciudades

            Robots = doc.getElementsByTagName("robots") ## obtener los robots de la lista de robots


            for i in range(len(Ciudades)):

                ciudad = Ciudades[i].getElementsByTagName("ciudad") #obtener los datos de cada ciudad por separado dentro de la lista de ciudades

                for j in range(len(ciudad)):

                    Uciudad = ciudad[j].getElementsByTagName("nombre") #obtener los datos nombre dentro de la ciudad 

                    Filas = ciudad[j].getElementsByTagName("fila") #obtener los datos filas dentro de la ciudad

                    Militares = ciudad[j].getElementsByTagName("unidadMilitar")

                    for k in range(len(Uciudad)):

                        name = Uciudad[k].firstChild.data ##nombre de la ciudad 

                        filas_ciudad = Uciudad[k].attributes['filas'].value  #numero de filas en la ciudad

                        columnas_ciudad = Uciudad[k].attributes['columnas'].value #numero de columnas en la ciudad

                        for l in range(len(Filas)):

                            N_Fila = Filas[l].attributes['numero'].value #obtener el numero de la fila
                            fila = Filas[l].firstChild.data #obtener la fila 

                            for m in range(len(fila)): ##recorrer la fila 

                                inside = ''

                                if fila[m] == '"':

                                    continue #en caso de ser el delimitador

                                elif fila[m] == '*':

                                    inside = 'Intransitable'

                                    listas.agregarL(N_Fila, m, inside, name) ##agregar a lista de mapas

                                elif fila[m] == ' ':

                                    inside = 'Transitable'

                                    listas.agregarL(N_Fila, m, inside, name) ##agregar a lista de mapas

                                elif fila[m] == 'E':

                                    inside = 'Entrada'

                                    listas.agregarL(N_Fila, m, inside, name) ##agregar a lista de mapas

                                elif fila[m] == 'C':

                                    inside = 'Unidad Civil'

                                    listas.agregarL(N_Fila, m, inside, name) ##agregar a lista de mapas

                                elif fila[m] == 'R':

                                    inside = 'Recurso'

                                    listas.agregarL(N_Fila, m, inside, name) ##agregar a lista de mapas

                                else: 

                                    continue

                    for a in range(len(Militares)):   

                        fila_unidadM = Militares[a].attributes['fila'].value #fila unidad militar

                        columna_unidadM = Militares[a].attributes['columna'].value #columna unidad militar

                        poder_unidadM = Militares[a].firstChild.data ##poder de unidad militar 

                        ##agregar a lista de drones

                        DronesM.agregarM(fila_unidadM, columna_unidadM, poder_unidadM) #agregar unidades militares


            ##drones aliados 
            for x in range(len(Robots)):

                Robot = Robots[x].getElementsByTagName("robot") ##obtener un robot dentro de la lista de robot

                for y in range(len(Robot)):

                    robot_nombre =  Robot[y].getElementsByTagName("nombre") ##obtener el dato robot nombre dentro del robot

                    for z in range(len(robot_nombre)):
                        
                        tipo_dron = robot_nombre[z].attributes['tipo'].value #obtener el tipo de dron 

                        if tipo_dron == 'ChapinFighter':

                            rnombre = robot_nombre[z].firstChild.data ##obtener el nombre del robot
                            capacidad = robot_nombre[z].attributes['capacidad'].value ##obtener la capidad del dron 

                            ##agregar dron pelea 
                            DronesP.agregarP(rnombre, capacidad)

                        elif tipo_dron == 'ChapinRescue':

                            rnombre = robot_nombre[z].firstChild.data ##obtener el nombre del robot 

                            ##agregar dron de rescate
                            DronesR.agregarR(rnombre)

    
                       

            

