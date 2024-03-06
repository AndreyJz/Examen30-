import menu as me
import corefiles as cf

inventario = {}

productos = cf.checkFile('viveres.json',inventario)

if __name__ == '__main__':
    me.mainmenu(productos)