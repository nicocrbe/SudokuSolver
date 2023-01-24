import unittest
from sudokuSolver import sudokuSolver
from sudokuSolver import mostrarTablero
from sudokuSolver import celdaVacia


board9x9 = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]



class TestsudokuSolver(unittest.TestCase):

    def test_celdaVacia(self):

        self.assertEquals(0,board9x9[0][1])

    def test_sudokuSolver(self):
        sudokuSolver(board9x9)

        mostrarTablero(board9x9)

        self.assertEqual(2,board9x9[0][1])

if __name__ == '__main__':
    unittest.main()
