import os 
import csv 
import random
clean="cls"
menu_principal=1
saco_5kg=0
saco_10kg=0
saco_20kg=0
saco=1
os.system(clean)
pedido=[["N° Pedido", "Cliente", "Direccion", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]]
n_pedido=random.randint(1,1000)

def guardar_registro():
    with open("archivo.pedidos.csv", mode="w", newline="") as pedidos:
        guardar=csv.writer(pedidos)
        guardar.writerow(pedido)

def menu(): # Impresion del menu
    print("Bienvenido a CatPremium envios a domicilio.")
    print("1. Registrar pedido\n2. Listar todos los pedidos\n3. Imprimir hoja de ruta\n4. salir del programa y guardar")

def registro(): # Registro
    numero_pedido=n_pedido+1
    print(f"Su N° de pedido es {numero_pedido}")
    nombre_cliente=input("Ingrese su nombre: ").title()
    direccion=input("Ingrese su direccion: ").title()
    try:
        res=int(input("Seleccione su comuna.\n1. San Bernardo\n2. Calera de tango\n3. Buin\nRe: "))
        if res==1:
            sector="San Bernardo"
        elif res==2:
            sector="Calera de Tango"
        elif res==3:
            sector="Buin"
        else:
            print("Escoja una comuna valida")
    except ValueError:
        print("Escoja una opcion del 1 a 3")
    saco_5kg=int(input("Ingrese cuanto sacos de 5kg quiere: "))
    saco_10kg=int(input("Ingrese cuanto sacos de 10kg quiere: "))
    saco_20kg=int(input("Ingrese cuantos sacos de 20kg quiuere: "))
    pedido.append([numero_pedido,nombre_cliente,direccion,sector,  saco_5kg ,  saco_10kg  , saco_20kg]) 
    os.system(clean)
    print("Su pedido quedara de la siguiente forma:")
    for elemento in pedido:
        print(elemento)

def listar_pedidos(): # Imprime el pedido antes de guardarlo
    for elemento in pedido:
        print(elemento)

def imprimir_ruta(): # Imprime el pedido guardado en el archivo csv
    try:
        with open("archivo.pedidos.csv", mode="r", newline="") as pedidos:
            leer=csv.reader(pedidos)
            for i in leer:
                for fila in i:
                    print(fila)
    except FileNotFoundError:
        print("Archivo no encontrado")

while menu_principal==1:
    menu()
    try:
        opcion=int(input("Seleccione una opcion del menu: "))
        if opcion==1:
            os.system(clean)
            registro()
        elif opcion==2:
            os.system(clean)
            listar_pedidos()
        elif opcion==3:
            os.system(clean)
            imprimir_ruta()
        elif opcion==4:
            os.system(clean)
            print("Guardando pedidos")
            guardar_registro()
            menu_principal=0 
    except ValueError:
        print("Seleccione una opcion valida")
        continue