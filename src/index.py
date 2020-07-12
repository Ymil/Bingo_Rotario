from tkinter import *
from tkinter import ttk
import consola
import threading

ventana = Tk()
ventana.title("Bingo")

def Manual():
    consola.obtener_numero()                                           
    return

def Detener():
    consola.flag_auto=False
    return

def Automatico():
    consola.tiempo_usuario = int (input ('Seleccione tiempo: '))
    consola.flag_auto = True
    t1 = threading.Thread(name="obtener", target=consola.obtener_auto)
    t1.start()
    return

def Continuar():
    consola.flag_auto = True
    t1 = threading.Thread(name="obtener", target=consola.obtener_auto)
    t1.start()
    return

def Reiniciar():
    return

def ultimo_valor(numero_obtenido):
    entryText.set(numero_obtenido)

consola.funcion_retorno = ultimo_valor

#Tabla registro de numeros
tabla = ttk.Treeview(height= 5, columns=10)
tabla.grid(row = 4, column = 0, columnspan=10)
tabla.heading('#0', text = "1", anchor= CENTER)
tabla.heading('#1', text = "2", anchor= CENTER)

#Entrada
entryText = StringVar()
e_texto = Entry(ventana, font=("Calibri 20"), textvariable=entryText)
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady= 5)

#Botones
boton_Manual = Button(ventana, text="Manual", width=8, height=2, command = lambda: Manual())            #A traves de lambda ejecuto la acción para este boton
boton_Detener = Button(ventana, text="Detener", width=8, height=2, command = lambda: Detener())         #A traves de lambda ejecuto la acción para este boton
boton_Iniciar = Button(ventana, text="Continuar", width=8, height=2, command = lambda: Continuar())     #A traves de lambda ejecuto la acción para este boton
boton_Reiniciar = Button(ventana, text="Reiniciar", width=8, height=2, command = lambda: Reiniciar())   #A traves de lambda ejecuto la acción para este boton
boton_Automatico = Button(ventana, text="Automatico", width=8, height=2, command = lambda: Automatico()) 

#Botones en pantalla
boton_Manual.grid(row=1, column=0, padx = 10, pady=10)
boton_Automatico.grid(row=1, column=1, padx = 10, pady=10)
boton_Detener.grid(row=1, column=2, padx = 10, pady=10)
boton_Iniciar.grid(row=1, column=3, padx = 10, pady=10)
boton_Reiniciar.grid(row=1, column=4, padx = 10, pady=10)


ventana.mainloop()





