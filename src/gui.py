from tkinter import *
from tkinter import ttk
from os import path
import simpleaudio as sa
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
    ultimoNumero.set(numero_obtenido)
    archivo_sonido = "sounds/"+str(numero_obtenido)+".wav"
    # print(archivo_sonido)
    direccion_archivo = path.abspath(archivo_sonido)
    # print(direccion_archivo)
    direccion_archivo_corregida = (direccion_archivo).replace("\\", "/")
    # print(direccion_archivo_corregida)
    # direccion_archivo = str.replace('\', '/')
    # print(direccion_archivo)
    listaHistorica.set(cli.lista_historico[0:10])
    wave_obj = sa.WaveObject.from_wave_file(direccion_archivo_corregida)
    play_obj = wave_obj.play()
    # play_obj.wait_done()
    

cli.funcion_retorno = ultimo_valor

#Tabla registro de numeros
tabla = ttk.Treeview(height = 5, columns = 10)
tabla.grid(row = 4, column = 0, columnspan = 10)
tabla.heading('#0', text = "1", anchor = CENTER)
tabla.heading('#1', text = "2", anchor = CENTER)

#Entrada de ultimo numero y registro de ultimos 10 numeros salientes
ultimoNumero = StringVar()
mostrar_ultimo_numero = Entry(ventana, font = ("Calibri 20"), textvariable = ultimoNumero)
mostrar_ultimo_numero.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

listaHistorica = StringVar()
mostrar_lista_historica = Entry(ventana, font = ("Calibri 20"), textvariable = listaHistorica)
mostrar_lista_historica.grid(row = 1, column = 0, columnspan = 4, padx = 50, pady = 5)

#Botones
boton_Manual = Button(ventana, text = "Manual", width = 8, height = 2, command = lambda: Manual())              #A traves de lambda ejecuto la acción para este boton
boton_Detener = Button(ventana, text = "Detener", width = 8, height = 2, command = lambda: Detener())           #A traves de lambda ejecuto la acción para este boton
boton_Iniciar = Button(ventana, text = "Continuar", width = 8, height = 2, command = lambda: Continuar())       #A traves de lambda ejecuto la acción para este boton
boton_Reiniciar = Button(ventana, text = "Reiniciar", width = 8, height = 2, command = lambda: Reiniciar())     #A traves de lambda ejecuto la acción para este boton
boton_Automatico = Button(ventana, text = "Automatico", width = 8, height = 2, command = lambda: Automatico())  #A traves de lambda ejecuto la acción para este boton

#Botones en pantalla
boton_Manual.grid(row = 2, column = 0, padx = 10, pady = 10)
boton_Automatico.grid(row = 2, column = 1, padx = 10, pady = 10)
boton_Detener.grid(row = 2, column = 2, padx = 10, pady = 10)
boton_Iniciar.grid(row = 2, column = 3, padx = 10, pady = 10)
boton_Reiniciar.grid(row = 2, column = 4, padx = 10, pady = 10)

ventana.mainloop()