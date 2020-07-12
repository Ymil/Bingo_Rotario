# Programación de bingo por consola


# from random import randint
import random
import threading
import time
import logging
import bisect

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

funcion_retorno = None

#Funcion para obtener numeros de manera aleatoria
def obtener_numero():
    logging.info('Verificando obtencion de numero')
    if len(lista_numeros) == 0:                    #Establezco que si la lista de numeros se vacia, se finalice la obtencion de numeros
        return False
    numero_obtenido = random.choice(lista_numeros) #Obtengo un numero de forma aleatoria de la lista de numeros establecidos
    lista_numeros.remove(numero_obtenido)                                   #El numero que obtengo de la lista, lo elimino de dicha lista para reducir posibilidades
    bisect.insort(lista_historico, numero_obtenido, 0, 0)    #A una nueva lista, agrego los numeros que van saliendo
    # lista_historico.reverse()                                             #Intento registrar numeros a medida que salen pero se altera el orden. VERIFICAR
    print(numero_obtenido)                         #Muestro por consola el numero obtenido
    print(lista_historico)                         #Muestro por consola la lista de numeros que van saliendo
    funcion_retorno(numero_obtenido)               #Permito la finalizacion del programa
    return numero_obtenido

flag_auto = False                                  #Declaro un flag para cuando quiera cortar ejecucion automatica de obtencion de numeros

#Defino funcion para la obtencion automatica de numeros
def obtener_auto():
    while flag_auto:                               #Mientras flag se mantenga en True, ejecuta
        if not obtener_numero():                   #SI la funcion obtener_numero detecta que la lista_numeros se vacio, finaliza con el break
            break
        time.sleep(tiempo_usuario)                 #Tiempo de espera entre obtencion de numeros

numero_obtenido = 0
lista_numeros = list(range( 1 , 21 ))              #Lista inicial que contiene los numeros necesarios para el bingo
lista_historico = []                               #Creo la lista que registrara, en orden, los numeros que se obtendran aleatoriamente de la lista inicial
i = 0

t1 = threading.Thread(name = "obtener_auto" , target = obtener_auto)

if __name__=="__main__":                           #Para indicar que se ejecuta el index.py

    while 1:
        #Menu sencillo de juego
        print("Bienvenido al Bingo")
        print("")
        print("Elige lanzamiento Manual o Automatico")
        print("")
        print("1- Manual")
        print("2- Automatico")
        print("  3- Detener")
        print("  4- Continuar")
        print("5- Reiniciar")
        print("")
        opcion = int(input('Elija su opción: '))
        
        #Acciones en base a la opcion elegida
        if opcion == 1:                             #Verifico el modo de lanzamiento elegido
            lanzar_manual = 'Pulse 1 para obtener un numero: '
            
            '''Mientras el usuario ingrese el numero 1, el programa arrojara de manera aleatoria, los numeros de la lista inicial
            Si en algun momento ingresa otro valor por teclado, se corta el lanzamiento'''
            while i < 20:
                manual = input(lanzar_manual)
                if manual != '1':
                    break
                else:
                    obtener_numero()
                    i+=1

        elif opcion == 2:
            tiempo_usuario = int (input ('Seleccione tiempo: '))
            flag_auto = True
            t1 = threading.Thread(name="obtener", target=obtener_auto)
            t1.start()
        elif opcion == 3:
            flag_auto = False
        elif opcion == 4:
            flag_auto = True
            t1 = threading.Thread(name="obtener", target=obtener_auto)
            t1.start()
