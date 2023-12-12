import re

def verificar_nombre(nombre):
  valido= r'^[a-zA-Z\s]+$'
  if len(nombre)<3 or len(nombre)>10:
      return False
  if re.match(valido,nombre):
    return True
  return False

def crear_nombre():
    nombre= input('Ingrese nombre y apellido del paciente a registrar:')
    while verificar_nombre(nombre) == False:
        print('El nombre ingresado no es valido. Intente de nuevo.')
        nombre= input('Ingrese el nombre del paciente a registrar:')
    return nombre
    
def crear_obra_social(obras_validas):
    while True:
        obra= input('Ingrese la obra social del paciente: ').upper()
        if obra not in obras_validas:
            print('El laboratorio no trabaja con esa obra social')
        else:
            break
    return obra

def crear_telefono(tel_cargados):
    while True:
        telefono= input('Ingrese el telefono del paciente: ')
        if len(telefono)<5 or len(telefono)>15:
            print('El telefono ingresado no es valido')
            continue
        elif not telefono.isdigit():
            print('Ingrese números unicamente')
        elif telefono in tel_cargados:
            print('El telefono ingresado ya existe')
        else:
            return telefono


  

def crear_dni(dni_cargados):
    while True:
        dni= input('Ingrese el DNI del paciente: ')
        if len(dni)<8 or len(dni)>11:
            print('El DNI ingresado no es valido')
            continue
        elif not dni.isdigit():
            print('Ingrese números unicamente')
        elif dni in dni_cargados:
            print('El DNI ingresado ya existe')
        else:
            return dni
