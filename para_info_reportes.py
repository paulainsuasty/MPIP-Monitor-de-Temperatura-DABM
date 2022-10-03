# MPIP
# DABM 2022-2

from PIL import Image
import time
import matplotlib.pyplot as plt
#from statistics import mean
import statistics

print("Por favor digital el nombre del archivo del que desees recoger la información (No ingreses el .csv al final!)")
nombre_archivo_revisar = input(">>> ")
a = open(nombre_archivo_revisar+".csv", "r")
lineas = a.readlines()
print(lineas)
# print("El tipo de dato de datos es: ", lineas.type())
valores_temperatura = []
# datos.append(lineas)
for l in (lineas):
    # print(l)
    l = l.replace("\n", "")
    l = l.replace("", "")
    l = l.split(";")
    valores_temperatura.append(l)

#print("el valor maximo encontrado fue: ", valores_temperatura[])
#print(str(max(valores_temperatura)))
#print("el valor minimo encontrado fue: ")
#print(str(min(valores_temperatura)))

#print(str(statistics.mean(valores_temperatura)))
#print("el valor promedio es: ", mean(int(valores_temperatura)))
#print("El valor promedio es : ", str(mean(valores_temperatura)))

print("La fecha en la cual fueron tomados estos datos fue: (AAAA-MM-DD)", nombre_archivo_revisar[:10])
#nombre_archivo_revisar[:nombre_archivo_revisar.rfind("_")])

print("Presentando la imagen:")
time.sleep(1)
#print("Por favor digital el nombre de la imagen (no olvides agregar el jpg al final!)")
#nombre_imagen_presentar = input(">>> ")
#plt.show(nombre_imagen_presentar)
im = Image.open(nombre_archivo_revisar+".jpg")
im.show()