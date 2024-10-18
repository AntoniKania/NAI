import numpy as np
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

pos2string = lambda ab: chr(65 + ab[0]) + str(ab[1] + 1)
string2pos = lambda s: np.array([ord(s[0]) - 65, int(s[1]) - 1])


class Chomp(TwoPlayerGame):
    def __init__(self, players, board_size):
        self.players = players
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype=int)
        self.current_player = 1

    def possible_moves(self):
        moves = [pos2string([r, c]) for r in range(self.board_size[0])
                 for c in range(self.board_size[1]) if self.board[r, c] == 0]
        return [move for move in moves if move != pos2string([0, 0])]

    def make_move(self, pos):
        row, col = string2pos(pos)
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
