# sudokuHacker
Python program with Tkinter GUI that can solve Sudoku Puzzles

*Introduction:

-The objective is to fill a nine-by-nine (9x9) grid with digits so that each row, column and 3x3 section contain number between 1 and 9
-Each number is used once and only once in each section 
-The Sudoku game players are provided with partially filled grid meant to be solved

*About:

-This Script is a Sudoku Sovler that solves almost any Sudoku Puzzle's by utilizing the Backtracking Algorithm
-Runs in Python, no additional modules required

*Working:

-Every time the program is executed an empty board is created
-Every entry has a default value of 0 which represents an unknown value
-Reference the puzzle you are trying to solve and enter the known values in the matching box in the program
-When all known values are entered, and there are zeros entered for the unknown values, press the solve button
-The program will output a solved puzzle
-Press the clear button to erase the existing grid so you can start over
-The script has no error checking so any invalid input will likely cause an error or an incorrect solution

*Requirements:

-Python

*Execution:

python sudokuHacker.py

OR

python3 sudokuHacker.py
