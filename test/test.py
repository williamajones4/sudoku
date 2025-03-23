"""These are the unit tests for main"""

import unittest
import pandas as pd
import main
import validate


class TestPossibilities(unittest.TestCase):
    "Test Object for unit test creation"

    def test_main_solver(self):
        """This test is for the main sudoku solver"""
        solution = pd.read_csv('data/solution2.csv', header=None)
        self.assertEqual(solution.equals(main.main_solver('data/problem2.csv')), True)
        self.assertEqual(solution.equals(main.main_solver('data/solution2.csv')), True)

    def test_possibilities_finder(self):
        """This test is for possibilities_finder"""
        row = [7,0,0,5,2,0,0,0,8]
        self.assertEqual([1,3,4,6,9], main.possibilities_finder(row))

    def test_correct_array_checker(self):
        """This test is to ensure validation of arrays"""
        correct_df = pd.read_csv('data/solution2.csv', header=None)
        self.assertEqual(True, validate.correct_array_checker(correct_df.iloc[0,:]))
        incorrect_df = pd.read_csv('data/wrong_solution1.csv', header=None)
        self.assertEqual(False, validate.correct_array_checker(incorrect_df.iloc[0,:]))

    def test_correct_checker(self):
        """This test is to ensure validation of overall puzzles"""
        correct_df = pd.read_csv('data/solution2.csv', header=None)
        self.assertEqual(True, validate.correct_checker(correct_df))
        incorrect_df = pd.read_csv('data/wrong_solution1.csv', header=None)
        self.assertEqual(False, validate.correct_checker(incorrect_df))
        incorrect_df = pd.read_csv('data/wrong_solution2.csv', header=None)
        self.assertEqual(False, validate.correct_checker(incorrect_df))
        incorrect_df = pd.read_csv('data/wrong_solution3.csv', header=None)
        self.assertEqual(False, validate.correct_checker(incorrect_df))

    def test_make_square_array(self):
        """This tests to make sure squares can be generated"""
        problem = pd.read_csv('data/problem1.csv', header=None)
        square_array = [7,0,0,0,5,6,0,4,0]
        self.assertEqual(square_array, validate.make_square_array(problem, (0,0)))
        self.assertEqual([], validate.make_square_array(problem, (9,9)))

    def test_print_puzzle(self):
        """tests printing a puzzle out nicely"""
        puzzle = pd.read_csv('data/problem1.csv', header=None)
        print( 
            """
            1 2 3 | 4 5 6 | 7 8 9,
            4 5 6 | 7 8 9 | 1 2 3,
            7 8 9 | 1 2 3 | 4 5 6,
            _____________________,
            1 2 3 | 4 5 6 | 7 8 9,
            4 5 6 | 7 8 9 | 1 2 3,
            7 8 9 | 1 2 3 | 4 5 6,
            _____________________,
            1 2 3 | 4 5 6 | 7 8 9,
            4 5 6 | 7 8 9 | 1 2 3,
            7 8 9 | 1 2 3 | 4 5 6,
            """
              )
