# MPIP
# DABM 2022-2
import serial

puerto = serial.Serial("COM3", 9600)

archivo = open("parametros_temperatura.csv", "r")
lineas = archivo.readlines()
datos = []
datos.append(lineas)
for l in (lineas):
    # print(l)
    l = l.replace("\n", "")
    l = l.split(";")
    datos.append(l)

print("los datos son", datos)
print("los datos son", datos[0][0])

print("los datos son HIPO MEN", datos[1][0])
print("los datos son HIPO MAY", datos[1][1])

print("los datos son NORM MEN", datos[2][0])
print("los datos son NORMA MAY", datos[2][1])

print("los datos son FIEB MEN", datos[3][0])
print("los datos son FIEB MAY", datos[3][1])

def control():
    dato = int(puerto.readline().decode().strip())
    print("Temperatura = ", dato)
    if dato >= int(datos[1][0]) and dato <= int(datos[1][1]):
        temp = "H"
    elif dato > int(datos[2][0]) and dato <= int(datos[2][1]):
        temp = "N"
    elif dato > int(datos[3][0]):
        temp = "F"

    print("Categoria: ", temp)
    puerto.write(temp.encode())
    # delay(200)
    control()

control()

# def control():
#
#     dato = int(puerto.readline().decode().strip())
#     print("Temperatura = ", dato)
#     if dato >= 15 and dato <= 32:
#         temp = "H"
#     elif dato > 32 and dato <= 36:
#         temp = "N"
#     elif dato > 36:
#         temp = "F"
#     print("Categoria: ", temp)
#     puerto.write(temp.encode())
#     # delay(200)
#     control()
#
# control()