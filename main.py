"This is the Main script for all"
import pandas as pd

def main_solver(problem_file):
    """Running the overall solver"""
    solution = pd.read_csv(problem_file, header=None)
    return solution


def possibilities_finder(array):
    """
    Desc: This function finds the possibilities left in an array

    Args: array - list that you want to check

    Return: result - list of possibilities
    """
    full = set((1,2,3,4,5,6,7,8,9))
    result = list(full - set(array))
    return result


if __name__ == "__main__":
    main_solver("data/problem2.csv")
