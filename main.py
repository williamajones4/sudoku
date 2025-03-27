"This is the Main script for all"
import sys
import pandas as pd
import validate

def main_solver(problem_file):
    """Running the overall solver"""
    solution = pd.read_csv(problem_file, header=None)
    solved = False
    cycle=1
    while not solved:
        solved_spots=0
        for i in range(9):
            for j in range(9):
                if solution.iloc[i,j] == 0:
                    square_potentials = set(possibilities_finder(validate.make_square_array(solution, (i,j))))
                    row_potentials = set(possibilities_finder(solution.iloc[i,:]))
                    column_potentials = set(possibilities_finder(solution.iloc[:,j]))
                    potentials = row_potentials & column_potentials & square_potentials
                    if len(potentials) == 1:
                        print(i, j, potentials)
                        solution.iloc[i,j] = potentials.pop()
                        solved_spots+=1
        if validate.correct_checker(solution):
            print(solution)
            return solution
        if solved_spots==0:
            print("Solved as much as possible")
            print(solution)
            return solution
        print(cycle)
        cycle+=1

def possibilities_finder(array):
    """
    Desc: This function finds the possibilities left in an array

    Args: array - list that you want to check

    Return: result - list of possibilities
    """
    full = set((1,2,3,4,5,6,7,8,9))
    result = list(full - set(array))
    return result

def print_solution(puzzle):
    """
    Desc: this prints out a puzzle nicely

    Args: puzzle - given any sudoku dataframe given

    Return: Printable puzzle
    """
    p_puz = puzzle.to_string(index=False, header=False).replace('0', ' ')
    # printable_puzzle = printable_puzzle.replace('0', ' ')
    p_puz = p_puz[:6] + "|" + p_puz[6:14] + "|" + p_puz[14:]
    print(p_puz)
    return p_puz


if __name__ == "__main__":
    main_solver(sys.argv[1])
