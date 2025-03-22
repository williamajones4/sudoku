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
    for s in [0,3,6]:
        for t in [0,3,6]:
            square = []
            for k in range(3):
                for l in range(3):
                    square.append(dataframe.iloc[k+s,l+t])
            if correct_array_checker(square) == False:
                return False
    return True
