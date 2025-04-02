#!/bin/bash
pylint main.py validate.py visualize.py test/test.py
coverage run -m unittest discover -s test
coverage report -m 
# pylint *.py