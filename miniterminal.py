#! /usr/bin/python

import sys
import getopt
import serial
import consola_io
import threading

# Caracter empleado para salir del terminarl
EXITCHARCTER = '\x04'                # ctrl+D
fin = 0     # Variable para indicar al thread que termine

#-----------------------------------------------------------------------------
#-- Este thread se ejecuta infinitamente. Esta todo el rato leyendo datos
#-- del puerto serie e imprimiendo en consola
#-----------------------------------------------------------------------------


def reader():
    #-- Cuando fin=1 se termina el thread
    while not(fin):
        try:
            data = s.read()
            sys.stdout.write(data)
            sys.stdout.flush()
        except:
            print "Excepcion: Abortando..."
            break


#-------------------------------------------------------------------------
#-- Este es el bucle principal. Todos los caracteres que llegan por la
#-- consola se envian por el puerto serie
#-------------------------------------------------------------------------


def writer():
    while 1:
        try:
            # Esperar a que se pulse una tecla.
            c = consola_io.getkey()
            # Si es la tecla de fin se termina.
            if c == EXITCHARCTER:
                break
            else:
                # Enviar tecla por el puerto serie.
                s.write(c)
        except:  # Si se ha pulsado control-c terminar.
            print "Abortando..."
            break


#--------------------------------
#-- Imprimir mensaje de ayuda
#--------------------------------


def help():
    sys.stderr.write("""Uso: miniterm [opciones]
    Miniterminal de comunicaciones en python

    opciones:
    -p, --port=PORT: Puerto serie a emplear. Bien un numero o una cadena

    Ejemplo:
      miniterm -p 0          --> Usar el primer puerto serie (Linux/Windos)
      miniterm -p /dev/ttyS1 --> Especificar el dispositivo serie (Linux)

     """)

#-----------------------------------------------------
#--  Analizar los argumentos pasados por el usuario
#-----------------------------------------------------


def Analizar_argumentos():
    #-- Valor por defecto del puerto a usar
    Puerto = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:],
         "hp:",
         ["help", "port="]
        )
    except getopt.GetoptError:
        # print help information and exit:
        help()
        sys.exit(2)
    #-- Leer argumentos pasados
    for o, a in opts:
        if o in ("-h", "--help"):
            help()
            sys.exit()
        elif o in ("-p", "--port"):
            try:
                Puerto = int(a)
            except ValueError:
                Puerto = a
    return Puerto

#----------------------
#   MAIN
#----------------------

#-- Analizar los argumentos pasados por el usuario
Puerto = Analizar_argumentos()

#--------------------------------------
#-- Abrir el puerto serie
#--------------------------------------
try:
    s = serial.Serial(Puerto, 19200)
    #-- Timeout: 1 seg
    s.timeout = 1
except serial.SerialException:
    #-- Error al abrir el puerto serie
    sys.stderr.write("Error al abrir puerto: " + str(Puerto))
    sys.exit(1)
print ("Puerto serie (%s): %s") % (str(Puerto), s.portstr)
print ("--- Miniterminal --- Ctrl-D para terminar\n")
#-- Lanzar el hilo que lee del puerto serie y saca por pantalla
r = threading.Thread(target=reader)
r.start()

#-- Ejecutar el bucle principal. Lee de la consola y envia por el puerto
#-- serie
writer()
fin = 1       #-- Indicar al trhead the termine y esperar
r.join()
s.close()      #-- Cerrar puerto serie.
