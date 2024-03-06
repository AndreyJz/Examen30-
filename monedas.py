import os

def yen():
    os.system('cls')
    try:
        Npesos = float(input('Ingrese la cantidad de pesos que desea cambiar a yenes <-> '))
    except ValueError:
        print('El dato ingresado no es un numero')
    else:
        yenes = (Npesos)*(26.30)
        print(f'{Npesos} pesos es igual a {yenes} yenes')
        os.system('pause')
        opcionesS = ['s','S']
        while True:
            op = input('Desea seguir convirtiendo pesos a yenes? s(si) o Enter(no)')
            if not op:
                return
            else:
                if op in opcionesS:
                    break
                elif op != opcionesS:
                    print('Ingrese una opcion valida')
                    os.system('pause')
def Euro():
    os.system('cls')
    try:
        Npesos = float(input('Ingrese la cantidad de pesos que desea cambiar a euros <-> '))
    except ValueError:
        print('El dato ingresado no es un numero')
    else:
        euros = (Npesos*4279)
        print(f'{Npesos} pesos es igual a {euros} euros')
        os.system('pause')
        opcionesS = ['s','S']
        while True:
            op = input('Desea seguir convirtiendo pesos a euros? s(si) o Enter(no)')
            if not op:
                return
            else:
                if op in opcionesS:
                    break
                elif op != opcionesS:
                    print('Ingrese una opcion valida')
                    os.system('pause')
def Dolar():
    while True:
        os.system('cls')
        try:
            Npesos = float(input('Ingrese la cantidad de pesos que desea cambiar a dolares <-> '))
        except ValueError:
            print('El dato ingresado no es un numero')
        else:
            dolares = (Npesos)*(3944)
            print(f'{Npesos} pesos es igual a {dolares} dolares')
            os.system('pause')
            opcionesS = ['s','S']
            while True:
                op = input('Desea seguir convirtiendo pesos a dolares? s(si) o Enter(no)')
                if not op:
                    return
                else:
                    if op in opcionesS:
                        break
                    elif op != opcionesS:
                        print('Ingrese una opcion valida')
                        os.system('pause')