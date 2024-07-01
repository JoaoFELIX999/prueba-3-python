import os
os.system("cls")
import random
programa_en_ejecucion = True
multas = []
vehiculos = []
#funcion para guardar auto :)
def guardar_vehiculo():
    print("guardando datos")
    nombre = input("ingrese Nombre y el Apellido: ")
    tipo = input("ingrese el tipo de vehiculo   auto,moto,camion,camioneta : ")
    if tipo not in ['auto', 'moto', 'camion', 'camioneta',"AUTO","MOTO","CAMION","CAMIONETA"]:
        print("Error: Debes ingresar uno de los tipos de vehículo especificados.")
        return    
    run = input("ingrese el run del dueño")
    fecha_registro = input("ingrese la fecha de rigistro  dd/mm/aaaa")
    marca = input("ingrese marca  entre 2 a 25 caracteres")
    if len(marca)>2 and len(marca)<16:
        print("continue")
    else:
        marca=input("ingrese una marca correcta")
    precio = int(input("ingrese el precio"))
    if precio <= 5000000:
        print("El precio del vehículo debe ser mayor a $5.000.000.")
        return
    patente = input("ingrese patente debe contener 4 letras en las cuales no puede estar m,n,ñ y 2 numeros al final")
    if patente=="M"or patente=="N"or patente=="Ñ":
        print("error")
        return
    multas = input("Tiene multa? (SI/NO): ").lower()

    monto_multa = None
    fecha_multa = None

    if multas == "si":
        monto_multa = float(input("Ingrese el monto de la multa: "))
        fecha_multa = input("Ingrese la fecha de la multa (DD/MM/AA): ")
    elif multas=="no":
        print("ciudadano ejemplar siga asi ")
    
    vehiculo = {
        "tipo": tipo,
        "nombre":nombre,
        "run":run,
        "fecha":fecha_registro,
        "marca":marca,
        "precio":precio,
        "patente":patente,
        "multas":multas,
        "fecha multa":fecha_multa,
        "monto multa":monto_multa
                }
    vehiculos.append(vehiculo)
    print("auto guardado")

#para buscar el auto
def buscar_vehiculo():
    buscar_patente = input("ingrese patente")
    for vehiculo in vehiculos:
        if vehiculo["patente"] == buscar_patente:
            print("Vehículo encontrado:")
            print(vehiculo)
            break
        else:
            print("vehiculo no existe")


def certificados():
    buscar_patente = input("ingrese patente")
    for vehiculo in vehiculos:
        if vehiculo["patente"] == buscar_patente:
            print("Vehículo encontrado:")
            print(vehiculo)
            print("multas 1")
            print("certificado de contaminantes: contamina mucho")
            print("amonestaciones: ninguna")
            break
        else:
            print("error")
          
            
while True:
    print("bienvenido a autos joan")
    print("1.-guardar")
    print("2.-buscar")
    print("3.-certificados")
    print("4.-salir")

    menu_opciones = int(input("que opcion desea"))
    if menu_opciones == 1:
        guardar_vehiculo()
    elif menu_opciones == 2:
        buscar_vehiculo()
    elif menu_opciones == 3:
        certificados()
    elif menu_opciones ==4:
        print("saliendo del programa")
        break

    elif menu_opciones >4 or menu_opciones <1:
        print("error")
        
        
    #fin del programa    