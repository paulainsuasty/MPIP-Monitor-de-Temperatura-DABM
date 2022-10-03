# MPIP
# DABM 2022-2
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import subprocess
from puerto import Puerto
import csv
import statistics
from datetime import *
import time

puerto = serial.Serial("COM3",9600)
#p= Puerto("COM3", 9600)
#p.abrir()

archivo = open("parametros_temperatura.csv", "r")
lineas = archivo.readlines()
datos = []
#datos.append(lineas)
for l in (lineas):
   # print(l)
   l = l.replace("\n", "")
   l = l.split(";")
   datos.append(l)

print(datos)
valores_temperatura = []
#puerto = serial.Serial("COM3",9600)
pausa = False

def onclick(event):
    global pausa
    print("Pausa")
    pausa = True
    # ALMACENAR YDATA EN EL ARCHIVO

fig, ax = plt.subplots()
fig.canvas.mpl_connect("button_press_event", onclick)
ydata = []

e = datetime.now()

def update_data(i):
    if not pausa:
        punto = puerto.readline().decode().strip()  # leer del puerto
        valores_temperatura.append(float(punto))
        #punto = p.leer()
        print(punto)
        #valores_temperatura.append(float(punto))
        # punto = p.readline().decode().strip() # leer del puerto
        # print(punto)
        ydata.append(punto)
        ax.clear()  # que la vaya limpiando y ploteando la lista
        ax.plot(ydata)
        ###
        ### PARA LEDS

        print("datos actuales son: ", datos)
        if int(punto) >= int(datos[0][0]) and int(punto) <= int(datos[0][1]):
            temp = "H"
        elif int(punto) > int(datos[1][0]) and int(punto) <= int(datos[1][1]):
            temp = "N"
        elif int(punto) > int(datos[2][0]):
            temp = "F"


        print("Categoria: ", temp)
        puerto.write(temp.encode())
        time.sleep(1)
        plt.savefig(str(date.today()) + str(e.hour) + str("_") + str(e.minute) + str("_") + str(e.second) + ".jpg")
        ###

        ####
        #punto = puerto.readline().decode().strip() # leer del puerto
        #print(punto)
        #ydata.append(punto)
        #ax.clear() # que la vaya limpiando y ploteando la lista
        #ax.plot(ydata)
        plt.title("Temperatura (C)")
        plt.xlabel("Numero de datos")
        plt.ylabel("Temperatura")

ani = animation.FuncAnimation(fig,update_data)
plt.show()
#control()


print("La fecha de hoy es: ", date.today())

# for i in range(num_data_adquisicion):
#     dato = p.leer()
#     print(dato)
#     valores_temperatura.append(float(dato))

print("Los valores de temperatura que solicitaste son: ")
print(valores_temperatura)

print("Guardando info en csv: ... ")
e = datetime.now()
nombre_archivo = str(date.today())+str(e.hour)+str("_")+str(e.minute)+str("_")+str(e.second)+".csv"

## CON MEDIDAS !!!!

f = open(nombre_archivo, "w")
i = 0
for i in range (len(valores_temperatura)):
    linea = ";".join([str(valores_temperatura[i])])
    f.write(linea + "\n")
    i= i+1
f.write("el valor maximo encontrado fue: ")
f.write(str(max(valores_temperatura))+"\n")
f.write("el valor minimo encontrado fue: ")
f.write(str(min(valores_temperatura))+"\n")
f.write("el valor promedio es: ")
f.write(str(statistics.mean(valores_temperatura)) + "\n")
f.close()


## FIN MEDIDAS !!!
print("Se ha guardo la información correctamente en el archivo: ", nombre_archivo )


retornar= int(input(("Deseas retornar al menu principal? 1. Si 2. No  ")))

if retornar == 1:
    subprocess.call(['python36', "main.py"])
elif retornar == 2:
    print("Cerrando la ejecución")
    exit()
else :
    print("Opción invalida, retornando al menu principal ...")
    subprocess.call(['python36', "main.py"])