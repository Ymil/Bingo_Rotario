from tkinter import *
from tkinter import ttk
import cli
import threading

ventana = Tk()
ventana.title("Bingo")

def Manual():
    cli.obtener_numero()                                           
    return

def Detener():
    cli.flag_auto=False
    return

def Automatico():
    cli.tiempo_usuario = int (input ('Seleccione tiempo: '))
    cli.flag_auto = True
    t1 = threading.Thread(name="obtener", target=cli.obtener_auto)
    t1.start()
    return

def Continuar():
    cli.flag_auto = True
    t1 = threading.Thread(name="obtener", target=cli.obtener_auto)
    t1.start()
    return

def Reiniciar():
    return

def ultimo_valor(numero_obtenido):
    entryText.set(numero_obtenido)
    historicoText.set(cli.lista_historico[0:10])

cli.funcion_retorno = ultimo_valor

#Tabla registro de numeros
tabla = ttk.Treeview(height = 5, columns = 10)
tabla.grid(row = 4, column = 0, columnspan = 10)
tabla.heading('#0', text = "1", anchor = CENTER)
tabla.heading('#1', text = "2", anchor = CENTER)

#Entrada
entryText = StringVar()
e_texto = Entry(ventana, font = ("Calibri 20"), textvariable = entryText)
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)
historicoText = StringVar()
e_texto = Entry(ventana, font = ("Calibri 20"), textvariable = historicoText)
e_texto.grid(row = 1, column = 0, columnspan = 4, padx = 50, pady = 5)

#Botones
boton_Manual = Button(ventana, text = "Manual", width = 8, height = 2, command = lambda: Manual())             #A traves de lambda ejecuto la acción para este boton
boton_Detener = Button(ventana, text = "Detener", width = 8, height = 2, command = lambda: Detener())          #A traves de lambda ejecuto la acción para este boton
boton_Iniciar = Button(ventana, text = "Continuar", width = 8, height = 2, command = lambda: Continuar())      #A traves de lambda ejecuto la acción para este boton
boton_Reiniciar = Button(ventana, text = "Reiniciar", width = 8, height = 2, command = lambda: Reiniciar())    #A traves de lambda ejecuto la acción para este boton
boton_Automatico = Button(ventana, text = "Automatico", width = 8, height = 2, command = lambda: Automatico()) #A traves de lambda ejecuto la acción para este boton

#Botones en pantalla
boton_Manual.grid(row = 2, column = 0, padx = 10, pady = 10)
boton_Automatico.grid(row = 2, column = 1, padx = 10, pady = 10)
boton_Detener.grid(row = 2, column = 2, padx = 10, pady = 10)
boton_Iniciar.grid(row = 2, column = 3, padx = 10, pady = 10)
boton_Reiniciar.grid(row = 2, column = 4, padx = 10, pady = 10)


ventana.mainloop()