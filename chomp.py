import numpy as np
from easyAI import TwoPlayerGame

pos2index = lambda s: tuple(int(x) - 1 for x in s.split())
index2pos = lambda idx: (idx[0] + 1, idx[1] + 1)

class Chomp(TwoPlayerGame):
    def possible_moves(self):
        endings = [self.player.pos + d for d in DIRECTIONS]
        return [pos2string(e) for e in endings  # all positions
                if (e[0] >= 0) and (e[1] >= 0) and
                (e[0] < self.board_size[0]) and
                (e[1] < self.board_size[1]) and  # inside the board
                self.board[e[0], e[1]] == 0]
    def scoring(self):
        return -100 if (self.possible_moves() == []) else 0

if __name__ == "__main__":
    user_input = input("Enter a space-separated position (e.g., '1 2'): ")

    result = pos2index(user_input)
    print("Converted position as tuple:", result)