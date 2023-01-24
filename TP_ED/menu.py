import pickle

from sudokuSolver import sudokuSolver
from sudokuSolver import mostrarTablero
from tablero import adaptarTableros
from tablero import crearTableros
from leerYEscribirArchivo import leer_csv
from leerYEscribirArchivo import escribir_csv
import signal
import sys


boards=""
tablerosResueltos = 0

def menu():
    global boards
    global tablerosResueltos

    opcion = (input("Ingrese la opcion deseada \n"
                   "1 <=== Iniciar nueva ejecucion \n"
                   "2 <=== Cargar ejecucion guardada \n"
                    "3 <=== Salir \n"))
    try:
        if opcion == "1":
                csv_path = input("Ingrese el nombre del archivo .csv \n")
                csv_path += ".csv"
                tablerosResueltos = 0
                boards = adaptarTableros(csv_path)
                iniciarTablero(adaptarTableros(csv_path)) #si pongo boards como parametro, falla

        elif opcion == "2":

                load_path = input("Ingrese nombre de la ejecucion guardada \n ")
                load_path+= ".p"
                iniciarTablero(pickle.load(open(load_path,"rb")))


        elif opcion == "3":
            print('Ha cerrado el programa')
            return
        else:
            print("Opcion Incorrecta")
            menu()
    except FileNotFoundError:
        print("Oops! El nombre de archivo no existe. Proba de nuevo con un nombre de archivo valido")
        menu()
    except OSError:
        print("Oops! El nombre de archivo es invalido")
        menu()
    except TypeError:
        print('Nombre de archivo no valido')
        menu()

def keyboard_interrupt(signal, frame):

    global boards
    try:
        nuevosTableros = boards[tablerosResueltos:len(boards)]
        print("\n No se aceptan caracteres especiales, de lo contrario perdera el progreso")
        save_path = input("Guardar ejecucion como: \n ")
        if save_path == "":
            raise OSError
        save_path += ".p"
        print("Ejecucion guardada correctamente")
        pickle.dump(nuevosTableros,open(save_path,"wb"))
        menu()
    except OSError:
        print("Oops! El nombre de archivo es invalido , intente nuevamente la ejecucion")
        menu()

    sys.exit(0) # Si quieres detener la ejecución

signal.signal(signal.SIGINT, keyboard_interrupt)

def iniciarTablero(tableros):

    global tablerosResueltos
    cont_tableros = 1

    for tablero in tableros:
        print("TABLERO {}".format(tablerosResueltos+1))
        mostrarTablero(tablero)
        sudokuSolver(tablero)
        print("|")
        print("SOLUCION {}".format(tablerosResueltos+1))
        mostrarTablero(tablero)
        escribir_csv(tablero)
        tablerosResueltos+=1
        cont_tableros += 1
        print("|")

if __name__ == menu():
      menu()

        
