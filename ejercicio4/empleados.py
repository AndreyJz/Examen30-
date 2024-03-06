import corefiles as cf
import os
from tabulate import tabulate

cargo = ['Almacenista', 'Jefe IT', 'Administrador', 'Mensajero', 'Genrente']

def AdEmploye(inventario:dict):
    os.system('cls')
    id = cf.Try('Ingrese el id del empleado <-> ',int)
    nombre = cf.Try('Ingrese el nombre del empleado <-> ',str)
    for idx, item in enumerate(cargo):
            print(f'{idx+1}. {item}')
    isValueTrue= True
    while isValueTrue:
        try:
            op = int(input('Ingrese el cargo del empleado')) 
        except ValueError:
            print('No estas ingresando un numero')
            os.system('pause')
        else:
            if op > len(cargo) or op < 1: #comprobacion de opciones
                print('Error, opcion no invalida')
            else:
                break
    salario = cf.Try('Ingrese el salario del empleado <-> ',float)
    info = {
        'id': str(id),
        'nombre': nombre,
        'cargo': cargo[op-1],
        'salario': salario,
    }
    inventario.update({str(id):info})
    cf.updateData('empleados.json',inventario)

def salario(inventario:dict):
    os.system('cls')
    id = cf.Try('Ingrese el id del empleado al que asignara horas, dias y todo lo demas <-> ',int)
    if str(id) not in inventario:
        print('Ese usuario no esta registrado...')
        os.system('pause')
    else:
        diasTrabajados = cf.Try('Ingrese los dias Trabajados del empleado <-> ',int)
        horasExtras = cf.Try('Ingrese las horas Extras del empleado <-> ',int)
        valorDia = cf.Try('Ingrese el valor del Dia del empleado <-> ',float)
        descuentoxCafeteria = cf.Try('Ingrese el descuento por la cafeteria <-> ',float)
        cuotaPrestamo = cf.Try('Ingrese la cuota de Prestamo del empleado <-> ',float)
        totalHrasExtra = (horasExtras*5500)
        totalDIas = (diasTrabajados*valorDia)
        salario = (totalHrasExtra)-(descuentoxCafeteria+cuotaPrestamo)
        info = {
            'mesPagado': cf.Try('Ingrese el mes pagado <-> ',str),
            'fechaPago': cf.Try('Ingrese la fecha pagada <-> ',str),
            'sueldoBase': inventario[str(id)]['salario'],
            'valorTotalHrasExtras': totalHrasExtra,
            'cuotaPrestamo': cuotaPrestamo,
            'descuentoxCafeteria': descuentoxCafeteria,
            'totalAPagar': (inventario[str(id)]['salario'] + (totalDIas - inventario[str(id)]['salario'])) + salario
        }
        inventario[str(id)].update({'colillaPago':info})
        cf.updateData('empleados.json',inventario)

def SearchColilla(inventario: dict): #Busca personas/zonas/asig/activo
    isValueTrue = True
    tabla = []
    while isValueTrue:
        empleado = cf.Try('Ingrese el id del empleado al que revisara la colilla <-> ',int)
        if str(empleado) not in inventario:
            print('Ese usuario no esta registrado...')
            os.system('pause')
        else:
            diccionario = inventario[str(empleado)]['colillaPago']
            tabla.append(diccionario)
            print(tabulate(tabla, headers='keys', tablefmt='grid'))
            os.system('pause')
            return    

def sumatodo(inventario:dict):
    totalPrima = 0
    for key, value in inventario.items():
        totalPrima += inventario[key]['colillaPago']['totalAPagar']
    print(f'El total a pagar por todos los empleados es {totalPrima}')
    os.system('pause')
