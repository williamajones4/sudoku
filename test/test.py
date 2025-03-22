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
        print(solution)
        print(main.main_solver('data/problem2.csv'))
        self.assertEqual(solution.equals(main.main_solver('data/problem2.csv')), True)

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
