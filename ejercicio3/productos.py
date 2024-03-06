import corefiles as cf
import os

def AdProducts(inventario:dict):
    os.system('cls')
    id = cf.Try('Ingrese el id del producto <-> ',int)
    nombre = cf.Try('Ingrese el nombre del producto <-> ',str)
    valorUnitario = cf.Try('Ingrese el valor Unitario del producto <-> ',float)
    stockmin = cf.Try('Ingrese el stock minimo del producto <-> ',int)
    stockmax = cf.Try('Ingrese el stock maximo del producto <-> ',int)
    info = {
        'id': str(id),
        'nombre': nombre,
        'valorUnitario': valorUnitario,
        'stockmin': stockmin,
        'stockmax': stockmax,
    }
    inventario.update({str(id):info})
    cf.updateData('viveres.json',inventario)