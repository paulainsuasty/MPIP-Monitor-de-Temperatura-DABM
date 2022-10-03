# MPIP
# DABM 2022-2

import serial
#from control_leds import control
import matplotlib.pyplot as plt
import subprocess
import matplotlib.animation as animation
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

print("datos son",datos)
#def intento():
    #lineas = archivo.readlines()
    # datos = []
    # datos.append(lineas)
    # for l in (lineas):
    #     # print(l)
    #     l = l.replace("\n", "")
    #     l = l.split(";")
    #     datos.append(l)
    #
    # print("los datos son", datos)
    # print("los datos son", datos[0][0])
    #
    # print("los datos son HIPO MEN", datos[1][0])
    # print("los datos son HIPO MAY", datos[1][1])
    #
    # print("los datos son NORM MEN", datos[2][0])
    # print("los datos son NORMA MAY", datos[2][1])
    #
    # print("los datos son FIEB MEN", datos[3][0])
    # print("los datos son FIEB MAY", datos[3][1])

    #  p.leer()
    # print("Temperatura = ", int(punto))
    # #print("mostrando datos",datos[1][0])
    # #print("mostrando datos", datos[1][1])
    # print("valor de punto es:", punto)
    # if int(punto) >= int(datos[1][0]) and int(punto) <= int(datos[1][1]):
    #     temp = "H"
    # elif int(punto) > int(datos[2][0]) and int(punto) <= int(datos[2][1]):
    #     temp = "N"
    # elif int(punto) > int(datos[3][0]):
    #     temp = "F"
    #
    # print("Categoria: ", temp)
    # puerto.write(temp.encode())
    # # delay(200)
    # intento()

#puerto = serial.Serial("COM3",9600)

num_data_adquisicion = int(input("Ingresa la cantidad de datos que deseas adquirir: "))
valores_temperatura = []
fig, ax = plt.subplots()
ydata = []

pausa = False

#e = datetime.now()
e = datetime.now()
nombre_archivo = str(date.today())+str(e.hour)+str("_")+str(e.minute)+str("_")+str(e.second)

for i in range(num_data_adquisicion):
    if not pausa:
        #global datos
        #punto = p.leer()
        #print(punto)
        punto = puerto.readline().decode().strip() # leer del puerto
        valores_temperatura.append(float(punto))
        #print(punto)
        ydata.append(punto)
        ax.clear() # que la vaya limpiando y ploteando la lista
        ax.plot(ydata)
        #control()
        #ani = animation.FuncAnimation(fig, ydata)
        #plt.show()

        ###
        if int(punto) >= int(datos[0][0]) and int(punto) <= int(datos[0][1]):
            temp = "H"
        elif int(punto) > int(datos[1][0]) and int(punto) <= int(datos[1][1]):
            temp = "N"
        elif int(punto) > int(datos[2][0]):
            temp = "F"

        print("Temperatura y Categoria: ", punto, temp)
        puerto.write(temp.encode())
        plt.savefig( nombre_archivo + ".jpg")
        time.sleep(1)
        ###
    if i == num_data_adquisicion:
        print("terminé")
        pausa = True
    i = i+1
    #intento()

#ani = animation.FuncAnimation(fig, ydata)
plt.title("Temperatura (C)")
plt.xlabel("Numero de datos")
plt.ylabel("Temperatura")
plt.show()

#### GUARDANDO EN .CSV #########
#valores_temperatura = []
print("La fecha de hoy es: ", date.today())

# for i in range(num_data_adquisicion):
#     dato = p.leer()
#     print(dato)
#     valores_temperatura.append(float(dato))

print("Los", num_data_adquisicion , "valores de temperatura que solicitaste son: ")
print(valores_temperatura)

print("Guardando info en csv: ... ")

f = open(nombre_archivo+".csv", "w")
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

#Puerto.close()

print("Se ha guardo la información y la imagen correctamente en el archivo: ", nombre_archivo+".csv")

retornar= int(input(("Deseas retornar al menu principal? 1. Si 2. No   ")))

if retornar == 1:
    subprocess.call(['python36', "main.py"])
elif retornar == 2:
    exit()
else :
    print("Opción invalida, retornando al menu principal ...")
    subprocess.call(['python36', "main.py"])