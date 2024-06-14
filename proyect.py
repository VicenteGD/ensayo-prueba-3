import os, time
from funciones import *


while True:
    print("menu trabajadores")
    print("1. registrar trabajador")
    print("2. listar todos los trabajadores")
    print("3. imprimir planilla de sueldos ")
    print("4. salir del programa")
    opc = int(input("ingrese opción: "))
    os.system("cls")
    if opc ==1:
        registrar_trabajador()
    elif opc==2:
       listar_trabajadores()
    elif opc == 3:
        pass
    else:
        salir()
       
    time.sleep(3)
