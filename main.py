# MONITOR DE TEMPERATURA
# MPIP
# DABM 2022-2

from threading import Thread
import subprocess
import serial
# import struct
import time
import sys
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from definir_rangos_temperatura import *
#from control_leds import control
#from grafica_tiempo_real_click import *
#from grafica_tiempo_real_click import *
#from graficas_tiempo_real_lab_3 import *

#numero_datos_registrar = 20
#puerto = serial.Serial("COM3", 9600)

def menu_temp():
    print("Bienvenido a la aplicación")
    print("MPIP DABM 2022-2")
    print("Por favor selecciona la opción que deseas que el programa realice")
    print("1. Captura de datos")
    print("2. Configuración de parámetros")
    print("3. Reportes")
    print("4. Salir")
    #print("5. LEDs")
    opcion = int(input(">>"))

    if opcion == 1:
        print("Seleccionaste la opción de captura de datos")
        print("Recuerda que esta información y su gráfica se almacenará en un .csv con la fecha y hora!")
        print("Del mismo modo, al final del .csv encontrarás el reporte del valor max, min y promedio")

        print("Selecciona: ")
        print("1. si deseas escoger una cantidad de datos que deseas capturar")
        print("2. Decidir hasta que momento se van a capturar datos durante la ejecución")
        opcion_2 = int(input(">>"))

        if opcion_2 == 2:
            print("2")
            print("Recuerda que deberás hacer click sobre la gráfica en el momento en el que desees detener la adquisición de datos")
            #graficando() #exec(open("graficas_tiempo_real_lab_3.py").read()) #graficas_tiempo_real_lab_3.py
            #t1 = Thread(target=subprocess.run, args=(['python36', "graficas_tiempo_real_lab_3.py"]))
            #t2 = Thread(target=subprocess.run, args=(["python", "control_leds.py"],))
            #t1.start()
            #t2.start()
            #t1.join()
            #t2.join()
            subprocess.call(['python36', "graficas_tiempo_real_lab_3.py"])  #, shell=True)

        elif opcion_2 == 1:
            #print("")
            #t1 = Thread(target=subprocess.run, args=(['python', "grafica_limitada_usuario.py"]))
            #t2 = Thread(target=subprocess.run, args=(["python", "control_leds.py"],))
            #t1.start()
            #t2.start()
            #t1.join()
            #t2.join()
            subprocess.call(['python36', "grafica_limitada_usuario.py"])  # , shell=True)

        else:
            print("Opción invalida. Saliendo de la ejecución ...")
            exit()

    elif opcion == 2:
        print("Seleccionaste la opción de definir los parámetros para rangos de temperatura")
        definir_rangos_temperatura_n()

    elif opcion == 3:
        print("Escogiste la opción de registro")
        subprocess.call(['python36', "para_info_reportes.py"])

print("MONITOR DE TEMPRATURA")
menu_temp()

# OPCIÓN THREADING PARA HILOS:
# from threading import Thread
# import subprocess
#
# t1 = Thread(target=subprocess.run, args=(["python", "script1.py"],))
# t2 = Thread(target=subprocess.run, args=(["python", "script2.py"],))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
