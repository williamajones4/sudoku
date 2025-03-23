"This is a helper script for validating scripts"
import pandas as pd

def correct_array_checker(array):
    """checks to see if an array is correct, can be used for row, column, or square"""
    full = set((1,2,3,4,5,6,7,8,9))
    if full == set(array):
        return True
    else:
        return False

def correct_checker(dataframe):
    """checks to see if a puzzle is correct"""
    for i in range(9):
        # Checks rows
        if correct_array_checker(dataframe.iloc[i,:]) == False:
            return False
        # Checks Columns
        elif correct_array_checker(dataframe.iloc[:,i]) == False:
            return False
    # Checks Squares
    prime_positions = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    square_arrays = []
    for position in prime_positions:
        square_array = make_square_array(dataframe, position)
        square_arrays.append(square_array)
    for array in square_arrays:
        if correct_array_checker(array) == False:
            return False
    return True

def make_square_array(dataframe, position):
    """Returns array of all the arrays of squares in puzzle"""
    positions = []
    for s in [0,3,6]:
        for t in [0,3,6]:
            square = []
            for k in range(3):
                for l in range(3):
                    square.append(dataframe.iloc[k+s,l+t].item())
                    positions.append((k+s,l+t))
            if position in positions:
                return square
    return []
