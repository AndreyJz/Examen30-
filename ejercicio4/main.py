import menu as me
import corefiles as cf

inventario = {}

empleados = cf.checkFile('empleados.json',inventario)

if __name__ == '__main__':
    me.mainmenu(empleados)