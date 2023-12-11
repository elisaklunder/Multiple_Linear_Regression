import sys
import os
sys.path.append(os.getcwd() + "/part_1/src")
from codemaker import Codemaker


if __name__ == "__main__":
    print("type the maximum number of attempts")
    max_iterations = input()
    opponent = Codemaker()
    opponent._make_code()
    
    print(max_iterations)
    for i in range(max_iterations):
        print("type the guess:")
        guess = list(input())

        wrong_position = opponent._correct_guesses_wrong_pos(guess)
        right_position = opponent._correct_guesses_right_pos(guess)
        print(f"the number of guesses in the right position with the right    \
            color is:{right_position}")
        print(f"the number of guesses in the wrong position with the right    \
           color is:{wrong_position}")

    print(f"the correct answer is {opponent.get_code()}")
