import empleados as p


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
        opciones = '1. Agregar Producto\n2. Añadir horas/dias trabajados\n3. Buscar colilla\n4. Total pagado\n5. Salir'
        print (titulo)
        print(opciones)
        op = input('Ingrese el indice de la seccion a la que quiere ingresar <-> ')
        if op=='1':
            p.AdEmploye(productos)
        elif op=='2':
            p.salario(productos)
        elif op=='3':
            p.SearchColilla(productos)
        elif op=='4':
            p.sumatodo(productos)
        elif op=='':
            break
        else:
            print('Error, ingrese un indice valido')
            p.os.system('pause')