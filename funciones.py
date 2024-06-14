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


def listar_trabajador():
    pass

def exportar_archivo_txt():
    pass

def salir():
    print("gracias adios")
    exit()

#pueden hacer mas funciones 