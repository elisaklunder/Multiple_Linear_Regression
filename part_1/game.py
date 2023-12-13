import sys
import os
sys.path.append(os.getcwd() + "/part_1/src")
from mastermind import Mastermind


if __name__ == "__main__":
    game = Mastermind(max_iterations=4)
    game.game()
