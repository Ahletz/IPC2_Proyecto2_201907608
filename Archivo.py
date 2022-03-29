from tkinter import *
from tkinter import filedialog

class Carga:

    direccion = '' #varible con la ubicacion del archivo 
    #Metodo para abrir un archivo 
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/")
        self.direccion= archivo
        print(archivo)

        return self.direccion
        
    
    #Metodo abrir la vetana con boton        
    def AbrirVentana(self):
        raiz =Tk()
        raiz.geometry('200x200')
        boton = Button(raiz, text="Abrir Archivo",command=self.AbrirArchivo)
        boton.place(x=50,y=75)
        raiz.mainloop()