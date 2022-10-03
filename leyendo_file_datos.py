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