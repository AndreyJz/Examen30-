import productos as p


def mainmenu(producto:dict):
    global productos
    productos = producto
    while True:
        p.os.system('cls')
        titulo = """
        ++++++++++++++++++++++++++++++
        + TIENDA VIVERES CAMPUSLANDS +
        ++++++++++++++++++++++++++++++
        """
        opciones = '1. Agregar Producto\n2. Salir'
        print (titulo)
        print(opciones)
        op = input('Ingrese el indice de la seccion a la que quiere ingresar <-> ')
        if op=='1':
            p.AdProducts(productos)
        elif op=='2':
            break
        else:
            print('Error, ingrese un indice valido')
            p.os.system('pause')