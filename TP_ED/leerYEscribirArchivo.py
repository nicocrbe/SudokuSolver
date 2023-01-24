import csv



def leer_csv(csv_path):

        
    i_file = open(csv_path, 'r')
    reader = csv.reader(i_file, delimiter=';')
    lista = []
    for row in reader:
      lista.append(row)

    i_file.close()


    return lista


def escribir_csv(tablerosResueltos):
        o_file = open('salida.csv', 'a', newline="")
        writer = csv.writer(o_file,delimiter = ";")
        for tablero in tablerosResueltos:
            writer.writerow(tablero)
        o_file.close()


