class TicTacToeAction:
    """
    a tic-tac-toe action is simple - it only takes the value of the column and row to play
    """
    __row: int
    __col: int

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col
