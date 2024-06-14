trabajadores=[] #función por opción
cargos= ("ceo", "desarrollador ", "analista")#

def registrar_trabajador():
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


def listar_trabajadores():
    if len (trabajadores)==0:
        print("lista vacia, registre un trabajador en la opción 1")
    else:
        print("\tlista de trabajadores")
        for t in trabajadores:
            print(f"nombre: {t[0]}\ncargo: {t[1]}\nbruto: {t[2]}\nsalud: {t[3]}\nafp: {t[4]}\nliquido: {t[0]}\n")


def exportar_archivo_txt():
    pass

def salir():
    print("gracias adios")
    exit()

#pueden hacer mas funciones 