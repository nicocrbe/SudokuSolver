import csv
from leerYEscribirArchivo import leer_csv

def adaptarTableros(csv_path):

    tableros = crearTableros(leer_csv(csv_path))
    tamanio = len(tableros[0])
    lista_tab = [tableros[x:x + tamanio] for x in range(0, len(tableros), tamanio)]

    return lista_tab

def crearTableros(lista):

    tableroParaUsar = lista

    board = []

    for x in tableroParaUsar:

        board.append([int(j) for j in x])

    return board

