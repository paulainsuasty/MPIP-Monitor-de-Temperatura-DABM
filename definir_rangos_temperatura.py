# MPIP
# DABM 2022-2

import subprocess
# modulo definir rangos de temperatura
global nuevo_hipotermia_menor
global nuevo_hipotermia_mayor
global nuevo_normal_menor
global nuevo_normal_mayor
global nuevo_fiebre_menor
global nuevo_fiebre_mayor

def definir_rangos_temperatura_n():
    print("**")
    print("Presentando los valores actuales de rangos de temperatura:")
    presentando_datos_actuales()
    #print(datos)
    
    print("Definiendo nuevos rangos de temperatura")
    print("por favor ingresa los siguientes valores (Celsius)")
    
    print("*Para Hipotermia*")
    nuevo_hipotermia_menor = input("Ingresa el valor más bajo que será catalogado como hipotermia")
    nuevo_hipotermia_mayor = input("Ingresa el valor más alto que será catalogado como hipotermia")
    
    print("*Para Temperatura Normal*")
    nuevo_normal_menor = input("Ingresa el valor más bajo de temperatura normal")
    nuevo_normal_mayor = input("Ingresa el valor más alto de temperatura normal")
    
    print("*Para Fiebre*")
    nuevo_fiebre_menor = input("Ingresa el valor más bajo que será catalogado en el rango de fiebre")
    nuevo_fiebre_mayor = input("Ingresa el valor más alto que será catalogado en el rango de fiebre")

    print("Los nuevos valores son:")
    print("Nuevos valores de hipotermia: ", nuevo_hipotermia_menor, nuevo_hipotermia_mayor)
    #print(nuevo_hipotermia_menor)
    #print(nuevo_hipotermia_mayor)

    print("Nuevos valores de temperatura normal: ", nuevo_normal_menor, nuevo_normal_mayor)
    #print(nuevo_normal_menor)
    #print(nuevo_normal_mayor)

    print("Nuevos valores de fiebre: ", nuevo_fiebre_menor, nuevo_fiebre_mayor)

    print("Guardando los nuevos valores de rango de temperatura en archivo CSV")
    f = open("parametros_temperatura.csv", "w")
    linea = ";".join([nuevo_hipotermia_menor, nuevo_hipotermia_mayor, 'H'])
    f.write(linea + "\n")
    linea = ";".join([nuevo_normal_menor, nuevo_normal_mayor, 'N'])
    f.write(linea + "\n")
    linea = ";".join([nuevo_fiebre_menor, nuevo_fiebre_mayor, 'F'])
    f.write(linea + "\n")
    f.close()
    print("Los nuevos valores han sigo guardados con exito!")
    #save()

    retornar = int(input(("Deseas retornar al menu principal? 1. Si 2. No  ")))

    if retornar == 1:
        subprocess.call(['python36', "main.py"])
    elif retornar == 2:
        exit()
    else:
        print("Opción invalida, retornando al menu principal ...")
        subprocess.call(['python36', "main.py"])

def save():
    global nuevo_hipotermia_menor
    global nuevo_hipotermia_mayor
    global nuevo_normal_menor
    global nuevo_normal_mayor
    global nuevo_fiebre_menor
    global nuevo_fiebre_mayor
    print("Guardando los nuevos valores de rango de temperatura")
    f = open("parametros_temperatura", "w")
    linea = ";".join([nuevo_hipotermia_menor, nuevo_hipotermia_mayor, 'H'])
    f.write(linea + "\n")
    linea = ";".join([nuevo_normal_menor, nuevo_normal_mayor, 'N'])
    f.write(linea + "\n")
    linea = ";".join([nuevo_fiebre_menor, nuevo_fiebre_mayor, 'F'])
    f.write(linea + "\n")
    f.close()

def presentando_datos_actuales():
    global nuevo_hipotermia_menor
    global nuevo_hipotermia_mayor
    global nuevo_normal_menor
    global nuevo_normal_mayor
    global nuevo_fiebre_menor
    global nuevo_fiebre_mayor
    a = open("parametros_temperatura.csv", "r")
    lineas = a.readlines()
    print(lineas)
    #print("El tipo de dato de datos es: ", lineas.type())

    datos = []
    #datos.append(lineas)
    
    for l in (lineas):
        # print(l)
        l = l.replace("\n", "")
        l = l.replace("", "")
        l = l.split(";")
        datos.append(l)
        
    #print("estos si:")
    #print(datos)

    print("**")

    #print("HIPOTERMIA: ")
    hipotermia_menor_actual = (datos[0][0])
    hipotermia_mayor_actual = (datos[0][1])
    #print("TEMPERATURA NORMAL:")
    normal_menor_actual = (datos[1][0])
    normal_mayor_actual = (datos[1][1])
    #print("FIEBRE: ")
    fiebre_menor_actual = (datos[2][0])
    fiebre_mayor_actual = (datos[2][1])

    print("HIPOTERMIA:", hipotermia_menor_actual, hipotermia_mayor_actual)
    print("TEMPERATURA NORMAL:", normal_menor_actual, normal_mayor_actual)
    print("FIEBRE: ", fiebre_menor_actual, fiebre_mayor_actual)
    print("**")