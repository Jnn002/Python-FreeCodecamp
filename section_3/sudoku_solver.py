class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        # Convierte el tablero en una cadena de texto para su impresión
        board_str = ''
        for row in self.board:
            # Reemplaza los ceros con '*' para una mejor visualización
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self):
        # Encuentra la primera celda vacía (con valor 0) en el tablero
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        # Verifica si el número no está presente en la fila
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Verifica si el número no está presente en la columna
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Verifica si el número no está presente en el cuadrado 3x3
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Verifica si el número es válido en la celda vacía dada
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Resuelve el Sudoku utilizando backtracking
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                # Si no es válido, resetea la celda y prueba con el siguiente número
                self.board[row][col] = 0
        return False

def solve_sudoku(board):
    # Función principal para resolver el Sudoku
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

# Ejemplo de un puzzle de Sudoku a resolver
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Llama a la función para resolver el puzzle
solve_sudoku(puzzle)