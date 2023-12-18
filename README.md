# OOP - 2023/24 - Assignment 2

This is the base repository for assignment 2.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/assignment%202_v1.1.pdf) for the content of the exercise.

## How to carry out your assignment

**PLEASE FOLLOW THESE STEPS:**

1. Use this template and create a private repository:
   ![](use_template.png)
2. Please add your partner and `oop-otoz` to the collaborators.
3. Create a new branch called `submission` **before adding any files**.
4. Add your code in the `main` branch (**IF YOU DO NOT ADD ANYTHING, THE PULL REQUEST WILL NOT WORK**).
5. Make sure that Actions are allowed: Settings -> Actions -> General -> Allow all actions and workflows.
6. Create a pull request from the `main` branch to your `submission` branch and check that your changes are captured.
7. Now finish your solution.
8. When you are ready to submit, add `oop-otoz` to the reviewers.

**Notes:**

- **Leave the \*\***init\***\*.py files untouched**.
- Do not move the `main.py` files.
- Do not move `requirements.txt`.
- Make the pull request AFTER SUBMITTING SOME CHANGES.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the `main` branch on to the `submission` branch. This means that `submission` is the base branch and `main` the compare branch. **Make sure to push your code only to `main`!**

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline.
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 main.py`. If your code does not throw any errors, it will be marked as reproducible. **Make sure it is reproducible before submission!**
3. Style - runs `flake8` on your code to ensure adherence to style guides.
4. Tests - runs `unittest` on your tests in `part_1/tests` to make sure all tests succeed.

---

## Your report
to do:
- write report for both p1 and p2
- comments (?) --> how much?
- double check type-hints/docstrings
- add typhints for @property in multiple linear regression + abc
- type checks for loss_function.py + check docstring some things are missng + raise errors
- raise an error in the model saver --> load weights if the given file has the wrong extention
- PUBLIC AND PRIVATE ATTRIBUTES IN THE METHODS

- REGRESSION PLOTTER SHOLD WORK AS WELL!!!!

Questions:
- should the gradient be in a separate class? --> if so do the loss functions as well
- should init be in the abc?
- is abc_ML correct ???
- should the @property be docstringed in teh abc class

##Part 1
Our implementation of the mastermind game consists of 3 files, one for each functinality of the class:
- codemaker: class taking care of the functionalities relative to providing a solution to the game
- mastermind: class taking care of the user input
- game: runs the game

**Codemaker
This class contains one constructor and 5 methods, all of which but one (get_code(self)) are private.

_guess_errors(): private method that raises the errors when the user input is not formatted correctly or is not valid. The method should not be accessible by the user since the format of the guess is given at the beginning.

_make_code(self): private method that generates a random combination of code given the accepted colors. The procedure to make the code or modify it should not be accessed by the user, if not through getters. Otherwise the goal of the game would be defeated.

 _correct_guesses_right_pos(): 
