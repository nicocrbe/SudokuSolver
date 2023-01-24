


def sudokuSolver(tab):

    posEnCero = celdaVacia(tab)
    if not posEnCero:
        return True
    else:
        fil, col = posEnCero

    for i in range(1,10):
        if validoEnTablero(tab, i, (fil, col)):
            tab[fil][col] = i

            if sudokuSolver(tab):
                return True

            tab[fil][col] = 0

    return False

def validoEnTablero(tab, num, pos):

        # mira fila
        for i in range(len(tab[0])):
            if tab[pos[0]][i] == num and pos[1] != i:
                return False

        # mira columnas
        for i in range(len(tab)):
            if tab[i][pos[1]] == num and pos[0] != i:
                return False
    
        # mira la posicion
        regionX = pos[1] // 3
        regionY = pos[0] // 3

        for i in range(regionY*3, regionY*3 + 3):
            for j in range(regionX * 3, regionX*3 + 3):
                if tab[i][j] == num and (i, j) != pos:
                    return False

        return True


def mostrarTablero(tab):

    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end= "")

            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")



def celdaVacia(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # fila, columna

    return None



