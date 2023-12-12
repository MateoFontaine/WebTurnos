#LIBRERIAS
import paciente as pc
import horario as hs
import turnero

#MANEJO DE ARCHIVOS-----------
def abrir_arch(nombre):
    salida=[]
    try:
        with open(nombre,'rt',encoding='utf-8-sig') as arch:
            for linea in arch:
                salida.append(linea.rstrip().split(';'))
    except FileNotFoundError:
        print(f'Aún no existe el archivo {nombre}. Creelo con la opción 1 para pacientes, y la 3 para turnos')
    except:
        print(f'Ocurrio un problema con el archivo {nombre}')
    return salida

def export_arch_at(nombre,matriz):
    try:
        with open(nombre,'at',encoding='utf-8-sig') as arch:
            for lista in matriz:
                txt=';'.join(lista)
                arch.write(txt + '\n')
    except:
        print('No se pudo guardar los cambios')
        
        
def export_arch_wt(nombre,m):
    try:
        with open(nombre,'wt',encoding='utf-8-sig') as arch:
            for linea in m:
                txt= ';'.join(linea) + '\n'
                arch.write(txt)
    except Exception as e:
        print('No se pudo exportar el archivo')
#-----------------
#OPCIONES DEL MENÚ------------------

def opciones():
    opc= ('Menú de opciones',
          '1-Crear nuevo paciente',
          '2-Reservar turnos',
          '3-Crear/Reiniciar turnos',
          '4-Ver turnos',
          '5-Ver pacientes',
          '0-Para salir'
          )
    for i in opc:
        print(i)
    print()


def opc1(pacientes,obras_validas,paci_cargados,tel_cargados,dni_cargados):
    while True:
        nombre=pc.crear_nombre()
        obra=pc.crear_obra_social(obras_validas)
        tel=pc.crear_telefono(tel_cargados)
        dni=pc.crear_dni(dni_cargados)
        print('¿Quiere registrar al siguiente paciente?:')
        print(f'Nombre: {nombre}\nObra social: {obra}\nTelefono: {tel}\nDNI: {dni}') 
        u= input('Ingrese 1 si los datos son correctos: ')
        if u == '1':
            break
    pacientes.append([nombre,obra,tel,dni])
    paci_cargados.append(nombre.upper())
    tel_cargados.append(tel)
    dni_cargados.append(dni)
    print('Se registro al paciente de manera exitosa')
    
    
def opc2(matriz,dias,horas,pacientes):
    if not matriz:
        print('Los turnos no han sido creados. Ejecute la opción 3')
        return
    hs.sacar_turno(matriz,dias,horas,pacientes)
    print()
    

def opc3():
    m=turnero.crear('turnos.csv')
    print('¡Se han creado los nuevos turnos de manera exitosa!')
    print('Salga del programa y vuelva a entrar para seguir trabajando.')
    return m


        
def opc_print(pacientes):
    for paciente in pacientes:
        print('| ',end='')
        print(' | '.join(paciente),'|')
  
#------------
#MENÚ---------
def menu():
    dias= ('Lunes','Martes','Miercoles','Jueves','Viernes')
    horas= tuple(f'{hora:02}:{minutos:02}' for hora in range(8,13) for minutos in range(00,60,30))
    obras_validas=('OSDE','SWISS MEDICAL', 'GALENO', 'MEDIFE', 'PAMI','IOMA')
    pacientes= abrir_arch('pacientes.csv')
    horarios= abrir_arch('turnos.csv')
    pacientes_cargados= [paciente[0].upper() for paciente in pacientes]
    tel_cargados= [tel[2].upper() for tel in pacientes]
    dni_cargados= [dni[3].upper() for dni in pacientes]
    while True:
        print()
        opciones()
        u= input('Ingrese la opción que desea ejecutar: ')
        print()
        if u == '1':
            opc1(pacientes,obras_validas,pacientes_cargados,tel_cargados,dni_cargados)
        elif u == '2':
            opc2(horarios,dias,horas,pacientes_cargados)
        elif u == '3':
            horarios= opc3()
        elif u == '4':
            if horarios:
                print('Lista de horarios:')
                opc_print(horarios)
            else:
                print('Los turnos no han sido creados. Ejecute la opción 3.')
        elif u == '5':
            if pacientes:
                print('Lista de pacientes:')
                opc_print(pacientes)
            else:
                print('No hay ningún paciente registrado')
        elif u == '0':
            break
        else:
            print('Error, ingrese una opción valida.')
        print()
    export_arch_at('pacientes.csv',pacientes)
    export_arch_wt('turnos.csv',horarios)
        
        
        
#CODIGO GENERAL--------
if __name__ == '__main__':
    menu()