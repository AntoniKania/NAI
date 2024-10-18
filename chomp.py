import numpy as np
from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

pos2string = lambda ab: "ABCDEFGH"[ab[0]] + str(ab[1] + 1)
string2pos = lambda s: np.array(["ABCDEFGH".index(s[0]), int(s[1])-1])

class Chomp(TwoPlayerGame):
    def __init__(self, players, board_size=(5, 5)):
        self.players = players
        self.board_size = board_size
        self.board = np.zeros(board_size, dtype=int)
        self.current_player = 1

    def possible_moves(self):
        moves = [pos2string([r, c]) for r in range(self.board_size[0])
                 for c in range(self.board_size[1]) if self.board[r, c] == 0]
        return [move for move in moves if move != "A1"]

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
        print('\n' + '\n'.join(['  1 2 3 4 5'] +
              ['ABCDE'[k] +
               ' ' + ' '.join(['O' if self.board[k, i] == 0 else 'X'
               for i in range(self.board_size[1])])
               for k in range(self.board_size[0])] + ['']))

    def lose(self):
        return self.possible_moves() == []

    def scoring(self):
        if self.lose():
            return -100
        else:
            return 0

    def is_over(self):
        return self.lose()

if __name__ == "__main__":
    ai_algo = Negamax(6)
    game = Chomp([Human_Player(), AI_Player(ai_algo)], (5, 5))
    game.play()
    print(f"Player {game.current_player} loses.")
