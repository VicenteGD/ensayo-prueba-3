import os, time
trabajadores=[]
cargos= ("ceo", "desarrollador ", "analista")#
while True:
    print("menu trabajadores")
    print("1. registrar trabajador")
    print("2. listar todos los trabajadores")
    print("3. imprimir planilla de sueldos ")
    print("4. salir del programa")
    opc = int(input("ingrese opción: "))
    os.system("cls")
    if opc ==1:
        print("registro trabajador")
        nombre_apellido = input("ingrese ")
        cargo = int(input("ingrese cargo(1:ceo, 2:desarrollador, 3:analista): "))
        sueldo_bruto = int(input("ingrese sueldo bruto: "))
        desc_salud =7/100 * sueldo_bruto
        desc_afp =int (12/100 * sueldo_bruto)
        sueldo_liquido =sueldo_bruto-(desc_salud+desc_afp)
        trabajador=[nombre_apellido, cargos[cargo-1], sueldo_bruto, desc_salud, desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("trabajador registrado")

    elif opc==2:
        pass
    elif opc == 3:
        pass
    else:
        print("gracias adios")
        break
    time.sleep(3)
