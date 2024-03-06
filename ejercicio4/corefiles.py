import json
import os


BASE = 'ejercicio4/data/'
def checkFile(archivo:str, data):
    if(os.path.isfile(BASE+ archivo)): 
        with open(BASE + archivo, 'r') as br: 
            data = json.load(br)
            return data
    else: 
        with open(BASE + archivo ,"w") as bw: 
            json.dump(data,bw,indent=4)
            return data

def updateData(archivo:str,data):
    with open(BASE+archivo,"r+") as rwf:
        json.dump(data,rwf,indent=4)

def Try(msg, tipo):
    while True:
        try:
            val = tipo(input(msg))
        except ValueError:
            print("Error, ingrese un valor valido")
            os.system('pause')
        else:
            return val
            break

