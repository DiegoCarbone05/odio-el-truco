import csv

def create_file(path:str, content:any):
    with open(path, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(content)

def read_file(path:str):
    data = []
    with open(path, "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            data.append(fila)
    return data
    
        
        