# -*- coding: utf-8 -*-

import sys
import time
sys.path.insert(0, './python-sudoku-generator-solver-master')

import sudoku as sud

def get_puzzle(sudoku):
    '''Prints out a sudoku in a format that is easy for a human to read'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    for i in range(81):
        if i in range(0,9):
            row1.append(sudoku[i].returnSolved())
        if i in range(9,18):
            row2.append(sudoku[i].returnSolved())
        if i in range(18,27):
            row3.append(sudoku[i].returnSolved())
        if i in range(27,36):
            row4.append(sudoku[i].returnSolved())
        if i in range(36,45):
            row5.append(sudoku[i].returnSolved())
        if i in range(45,54):
            row6.append(sudoku[i].returnSolved())
        if i in range(54,63):
            row7.append(sudoku[i].returnSolved())
        if i in range(63,72):
            row8.append(sudoku[i].returnSolved())
        if i in range(72,81):
            row9.append(sudoku[i].returnSolved())
    puzzle = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    return puzzle

def generate_puzzle(level):
    """ Input the level of difficulty of the sudoku puzzle. Difficulty levels
        include ‘Easy’ ‘Medium’ ‘Hard’ and ‘Insane’. Outputs a sudoku of desired
        difficulty."""
    t1 = time.time()
    n = 0
    if level == 'Easy':
        p = sud.perfectSudoku()
        s = sud.puzzleGen(p)
        if s[2] != 'Easy':
            return sud.main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return get_puzzle(s[0])
    if level == 'Medium':
        p = sud.perfectSudoku()
        s = sud.puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = sud.puzzleGen(p)
            if n > 50:
                return sud.main(level)
        if s[2] != 'Medium':
            return sud.main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return get_puzzle(s[0])
    if level == 'Hard':
        p = sud.perfectSudoku()
        s = sud.puzzleGen(p)
        while s[2] == 'Easy':
            n += 1
            s = sud.puzzleGen(p)
            if n > 50:
                return sud.main(level)
        while s[2] == 'Medium':
            n += 1
            s = sud.puzzleGen(p)
            if n > 50:
                return sud.main(level)
        if s[2] != 'Hard':
            return sud.main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return get_puzzle(s[0])
    if level == 'Insane':
        p = sud.perfectSudoku()
        s = sud.puzzleGen(p)
        while s[2] != 'Insane':
            n += 1
            s = sud.puzzleGen(p)
            if n > 50:
                return sud.main(level)
        t2 = time.time()
        t3 = t2 - t1
        print("Runtime is " + str(t3) + " seconds")
        print("Guesses: " + str(s[1]))
        print("Level: " + str(s[2]))
        return get_puzzle(s[0])
    else:
        raise(ValueError)

print(generate_puzzle('Easy'))