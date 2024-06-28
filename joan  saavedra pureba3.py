import os
os.system("cls")
import random
multas = []
vehiculos = []

print("bienvenido a autos joan")
print("1.-guardar")
print("2.-buscar")
print("3.-certificados")
print("4.-salir")
while True:
    menu_opciones = int(input("que opcion desea"))
    if menu_opciones == 1:
        print("guardar")
        def guardar_vehiculo():
            print("guardando datos")
        nombre = input("ingrese Nombre y el Apellido: ")
        tipo = input("ingrese el tipo de vehiculo   auto,moto,camion,camioneta : ")
        run = input("ingrese el run del dueño")
        fecha_registro = input("ingrese la fecha de rigistro  dd/mm/aaaa")
        marca = input("ingrese marca  entre 2 a 25 caracteres")
        precio = int(input("ingrese el precio"))
        if precio <= 5000000:
            print("El precio del vehículo debe ser mayor a $5.000.000.")
        patente = input("ingrese patente debe contener 4 letras en las cuales no puede estar m,n,ñ y 2 numeros al final")
        multas = (input("ingrese la cifra de la multa y la fecha ejmplo  50.000  12/12/2020 : "   ))


       
        
        vehiculo = {
            "tipo": tipo,
            "nombre":nombre,
            "run":run,
            "fecha":fecha_registro,
            "marca":marca,
            "precio":precio,
            "patente":patente,
            "multas":multas
                    }
        vehiculos.append(vehiculo)
        print("auto guardado")
    
    
    elif menu_opciones == 2:
        print("buscar vehiculo")
        buscar_patente = input("ingrese patente")
        encontrado = False
        for vehiculo in vehiculos:
            if vehiculo["patente"] == buscar_patente:
                print("Vehículo encontrado:")
                print(vehiculo)
                encontrado = True
                break
            else:
                print("vehiculo no existe")
    
    elif menu_opciones == 3:
        print("1.-Emisión de contaminantes")
        print("2.-Amotaciones vigentes")
        certi = int(input("selecione la opcion"))
        if certi == 1:
                buscar_patente = input("ingrese patente")
                encontrado = False
                for vehiculo in vehiculos:
                    if vehiculo["patente"] == buscar_patente:
                        print("Vehículo encontrado:")
                        print(patente ,nombre,run,tipo,marca,  "contamina mucho")
                        encontrado = True
            
        elif certi ==2:
            buscar_patente = input("ingrese patente")
            encontrado = False
            for vehiculo in vehiculos:
                  if vehiculo["patente"] == buscar_patente:
                    print("Vehículo encontrado:")
                    print(multas," :3  )")
                    encontrado = True    
                  else:
                      print("error")
           
    
    elif menu_opciones ==4:
        print("saliendo del programa")
        break
    elif menu_opciones >4 or menu_opciones <1:
        print("error")
    
    
#fin del        
    
    
    
  

