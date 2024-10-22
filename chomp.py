import numpy as np
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

def coordinatesToString(coordinates):
    """
    Converts a pair of numeric coordinates into a string representation.

    The function takes an array of two integers, where the first integer represents
    the column index and the second integer represents the row index.
    It converts the coordinates into a string that is user-frendly to type in
    the program, with contains colum (as a uppercase char) and row (as an integer)
    For example: "A1", "B7", "C9".

    Args:
        coordinates (array): A pair of integers representing the position, where
                            coordinates[0] is column index, and coordinates[1]
                            is the row index.

    Returns:
        str: A string representation of the coordinates, where the column is a letter
             (starting from 'A') and the row is an integer.

    Example:
        >>> coordinatesToString([0, 0])
        'A1'
        >>> coordinatesToString([2, 4])
        'C5'
    """
    return chr(65 + coordinates[0]) + str(coordinates[1] + 1)

def stringToCoordinates(s):
    """
    Converts a string representation of coordinates into a pair of numeric values.

    The function takes a string where the first character is an uppercase letter 
    representing the column (e.g., 'A' for 0, 'B' for 1, etc.), and the second 
    character is a 1-based number representing the row. It returns an array with 
    the column index and the row index. Function works correctlly when it's max 26 rows 
    and 9 columns - eg single character for coordinate

    Args:
        s (str): A string representing the coordinates, where the first character 
                 is a letter (column), and the second character is an integer (row,
                 up to 9)

    Returns:
        array: A pair of integers where the first value is column index 
               and the second value is the row index.

    Example:
        >>> stringToCoordinates('A1')
        (0, 0)
        >>> stringToCoordinates('C5')
        (2, 4)
    """
    return (ord(s[0]) - 65, int(s[1]) - 1)


class Chomp(TwoPlayerGame):
    def __init__(self, players, board_size):
        self.players = players
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype=int)
        self.current_player = 1

    def possible_moves(self):
        """
        Calculates possible moves that are correct from game logic perspective

        This method returns a list of all available (unoccupied) positions on the board.
        Result is converted to a string format using the `coordinatesToString` function.
        The resulting list excludes the position corresponding to [0, 0].

        Returns:
            array: A array of strings representing the valid moves, formated
            as string (for ex. "A2")

        Example:
            If the board is a 5x3 grid and the current state of the board is:
            
            [[0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1]]
            
            >>> possible_moves()
            ['A2', 'A3']
        """
        moves = [coordinatesToString([r, c]) for r in range(self.board_size[0])
                 for c in range(self.board_size[1]) if self.board[r, c] == 0]
        return [move for move in moves if move != coordinatesToString([0, 0])]

    def make_move(self, pos):
        row, col = stringToCoordinates(pos)
        for r in range(row, self.board_size[0]):
            for c in range(col, self.board_size[1]):
                self.board[r, c] = 1

    def ttentry(self):
        return tuple([tuple(row) for row in self.board])

    def ttrestore(self, entry):
        for x, row in enumerate(entry):
            for y, n in enumerate(row):
                self.board[x, y] = n

    def show(self):
        row_labels = ''.join(chr(65 + i) for i in range(self.board_size[0]))
        header = '  ' + ' '.join(str(i + 1) for i in range(self.board_size[1]))

        print('\n' + '\n'.join([header] +
                               [row_labels[k] +
                                ' ' + ' '.join(['O' if self.board[k, i] == 0 else 'X'
                                                for i in range(self.board_size[1])])
                                for k in range(self.board_size[0])] + ['']))

    def lose(self):
        return self.possible_moves() == []

    def scoring(self):
        return -100 if self.lose() else 0

    def is_over(self):
        return self.lose()


if __name__ == "__main__":
    ai_algo = Negamax(6)
    board_size = (4, 7)
    game = Chomp([Human_Player(), AI_Player(ai_algo)], board_size)
    game.play()
    print(f"Player {game.current_player} loses.")
