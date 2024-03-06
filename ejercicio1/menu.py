import monedas as m


def mainmenu():
    while True:
        m.os.system('cls')
        titulo = """
        ++++++++++++++++++++++++++++++
        + CASA DE CAMBIO CAMPUSLANDS +
        ++++++++++++++++++++++++++++++
        """
        opciones = '1. Pesos a Dolares\n2. Pesos a Euros\n3. Pesos a Yenes\n4. Salir'
        print (titulo)
        print(opciones)
        op = input('Ingrese el indice de la seccion a la que quiere ingresar <-> ')
        if op=='1':
            m.Dolar()
        elif op=='2':
            m.Euro()
        elif op=='3':
            m.yen()
        elif op=='4':
            m.os.system('exit')
        else:
            print('Error, ingrese un indice valido')
            m.os.system('pause')