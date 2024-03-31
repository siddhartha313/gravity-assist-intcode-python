## gravity-assist-intcode-python

This repository is used for the Gravity Assist Incode Fix Program using Python as a coding language.
https://adventofcode.com/2019/day/2

## Overview

We have a project where a program that runs on an Intcode computer, which is basically a list of numbers(integers) that tells the computer what to do. The program has instructions (opcodes) like adding or multiplying numbers at positions 1st & 2nd in the list and storing the result in 3rd position.
A specific input list is provided by the code challenge which is to be used to achieve the output. The list is stored in input.txt.

In Part 1, we need to fix a program that has had an error (a "1202 program alarm") by replacing values 12 & 2 in Position 1 and 2 in the list provided(input). Then we run the program and find out what value is left at at position 0 when the program finishes.

In Part 2, we need to find a specific pair of inputs that, when used in the program, produce a specific output provided by the code challenge. we are given some rules on how to try different inputs and how to interpret the output.

In simple words, we are fixing and running a program to find a result in position 0, and then we're finding the inputs that give us a specific result.

## Technologies used and Installation

We need to have the below installations or requirements:

1. Python Latest version installation:
   Download the latest version of python for Windows/Linux/MacOS from the below link:
   https://www.python.org/downloads/
   From command line check version : python3 --version

2. GITHUB or any other VCS account.

## Technical Illustrations

The Project consists of below files:

Python files:
gravityassistintcode.py
variables.py
test_intcode.py

Input file provided by code challenge:
input.txt

YAML files used by GITHUB Actions pipeline:
gravityassistpython.yml

Solution:
1. 'gravityassistintcode.py' consists of the main python code.
2. We used two functions 'gravityassist_intcode' and 'find_input_for_output' to define Part 1 and Part 2 of the challenge respectively.
3. 'gravityassist_intcode' does the addition and multiplication logic along with the code break when the halt opcode appears.
4. 'find_input_for_output' does the does the search for the 2 inputs for a particular output(19690720) as provided in the challenge.
5. We have used for loops to iterate between integers and introduced error handling to catch errors.
6. We have used 'variables.py' to replace values in the code to avoid hardcoding in the actual code.
7. After the main code ran OK, we use the 'test_intcode.py' to perform unit test cases.
8. We have provided few test cases which passes if proper inputs are provided and comes as passed successfully.
9. We have put the whole solution as part of devops in a CI/CD pipeline using GITHUB actions.
10. 'gravityassistpython.yml' is used as a yaml file where instructions are given to run the whole program on any push or commit is done in the GIT repoesitory.
11. The CI pipeline will first perform the main execution and then perform unit tests.
12. We can see the outputs in the pipeline workflow.

## Launch or Running the Program:

Manual Run/Launch:
1. Goto the folder where the python files are available.
2. Run below commands for python:
python3 gravityassistintcode.py (to run the main python file)
python3 test_intcode.py (to run the unit test pythin file)

GITHUB CI Run/Launch:
Commit or push or make any pull request in the GIT repository 'Main' branch will trigger the GITHUB workflow which provides the output.
The solution results is provided with screenshots in the document present in the GIT Repository: Solution-Screenshots.docx

## Authors

Siddhartha Deb Roy
