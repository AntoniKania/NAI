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
        Calculates possible moves that are correct from game logic perspective.
        Mandatory for easyAI implementation.

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
        """
        Fills board with range based on pos argument.
        Mandatory for easyAI implementation.

        This method save 1 into the board array based on coordinate pased in
        pos argument. It iterates through all cells in the board starting
        from the specified position

        Returns:
            none

        Example:
            If the board is a 5x3 grid and the current state of the board is:
            
            [[0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]

            Executing method with this parameter:

            >>> self.make_move('A4')
            
            Will result to modify board attribute to:

            [[0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]

        """
        row, col = stringToCoordinates(pos)
        for r in range(row, self.board_size[0]):
            for c in range(col, self.board_size[1]):
                self.board[r, c] = 1

    def show(self):
        """
        Displays the current state of the board.

        The method prints the board as a grid where rows are labeled with
        letters (starting from 'A') and columns are labeled with numbers
        (starting from '1'). Each cell on the board is represented 
        by an 'O' if it is unoccupied, and an 'X' if it is already taken.

        Returns:
            none

        Example:
            If the board is a 5x3 grid and the current state of the board is:
            
            [[0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]

            Executing method:

            >>> self.show()

            Will result to print this on sandard output:

              1 2 3 4 5
            A O 0 O 0 0
            B O O 0 X X
            C 0 O O X X
        """
        row_labels = ''.join(chr(65 + i) for i in range(self.board_size[0]))
        header = '  ' + ' '.join(str(i + 1) for i in range(self.board_size[1]))

        print('\n' + '\n'.join([header] +
                               [row_labels[k] +
                                ' ' + ' '.join(['O' if self.board[k, i] == 0 else 'X'
                                                for i in range(self.board_size[1])])
                                for k in range(self.board_size[0])] + ['']))

    def is_over(self):
        """
        Checks if the player has lost the game. Mandatory for easyAI
        implementation

        The method determines if there are no possible moves left by calling
        the `possible_moves` method. If the list is empty, it means the player
        has no valid moves eg. he lost.

        Returns:
            bool: `True` if there are no possible moves left
            (indicating a loss), `False` otherwise.

        Example:
            >>> self.possible_moves()  # returns []
            >>> self.is_over()
            True

            >>> self.possible_moves()  # returns ['A2', 'B3']
            >>> self.is_over()
            False
        """
        return self.possible_moves() == []

    def scoring(self):
        '''
        Gives a score to the current game. Mandatory for easyAI implementation

        Returns:
            integer: -100 if there are no possible moves left
            (indicating a loss), 0 otherwise.
         Example:
            If there are no available moves left on the board return `True`
            otherwise - `False`. 

            >>> self.is_over()  # returns true
            >>> self.scoring()
            -100

            >>> self.is_over()  # returns false
            >>> self.scoring()
            0
        '''
        return -100 if self.is_over() else 0


if __name__ == "__main__":
    """
    Entry point of the script for running a game of Chomp with a human player and an AI player.

    The main idea of game is chomping a piece of chocolate by 2 players. The
    player gives the coordinates of the upper left corner of the chocolate bar
    that he wants to eat. The opposing player does the same. They do this in
    loop unless the last square of chocolate is present. The person who is
    forced to take the last piece of chocolate lose.

    - Initializes an AI player with the Negamax algorithm, set to a depth of 6 for decision-making.
    - The game board is created with a size of 4 rows and 7 columns.
    - Two players are initialized: one human player (`Human_Player()`) and one AI player (`AI_Player(ai_algo)`).
    - The game is played using the `Chomp` game class's `play()` method.
    - After the game concludes, it prints a message declaring the losing player.

    Example:
        Running this script will initiate the game with the following setup:
        - A 4x7 board for the game of Chomp.
        - One human player and one AI player.
        After the game ends, it will output the losing player, such as:

        Player 1 loses.

    """
    ai_algo = Negamax(6)
    board_size = (4, 7)
    game = Chomp([Human_Player(), AI_Player(ai_algo)], board_size)
    game.play()
    print(f"Player {game.current_player} loses.")
