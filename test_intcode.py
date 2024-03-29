import unittest
from gravityassistintcode import gravityassist_intcode, find_input_for_output

class TestGravityAssistIntcode(unittest.TestCase):
    
    def test_gravityassist_intcode(self):
        # Test case 1: Addition operation
        program = [1, 0, 0, 0, 99]
        restored_program = program[:]
        restored_program[1] = 0
        restored_program[2] = 0
        expected_output = 2
        self.assertEqual(gravityassist_intcode(restored_program), expected_output)
        print("Test case 1 Part 1 Passed")

        # Test case 2: Multiplication operation
        program = [2, 3, 0, 3, 99]
        restored_program = program[:]
        restored_program[1] = 3
        restored_program[2] = 0
        expected_output = 2
        self.assertEqual(gravityassist_intcode(restored_program), expected_output)
        print("Test case 2 Part 1 Passed")

        # Test case 3: Combination of operations (Main Challenge Advent of Code)
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
        restored_program = program[:]
        restored_program[1] = 12
        restored_program[2] = 2
        expected_output = 3895705
        self.assertEqual(gravityassist_intcode(restored_program), expected_output)
        print("Test case 3 Part 1 Passed")

        # Test case 4: Combination of operations
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
        restored_program = program[:]
        restored_program[1] = 4
        restored_program[2] = 4
        expected_output = 1465707
        self.assertEqual(gravityassist_intcode(restored_program), expected_output)
        print("Test case 4 Part 1 Passed")

    def test_find_input_for_output(self):
        # Test case 1: Finding input for target output
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
        target_output = 19690720
        expected_noun = 64
        expected_verb = 17
        noun, verb = find_input_for_output(program, target_output)
        self.assertEqual(noun, expected_noun)
        self.assertEqual(verb, expected_verb)
        print("Test case 1 Part 2 Passed")


        # Test case 2: Finding input for target output
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
        target_output = 19690721
        expected_noun = 64
        expected_verb = 18
        noun, verb = find_input_for_output(program, target_output)
        self.assertEqual(noun, expected_noun)
        self.assertEqual(verb, expected_verb)
        print("Test case 2 Part 2 Passed")

        # Test case 2: No input found for target output
        program = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
        target_output = 10
        expected_noun = None
        expected_verb = None
        noun, verb = find_input_for_output(program, target_output)
        self.assertEqual(noun, expected_noun)
        self.assertEqual(verb, expected_verb)
        print("Test case 3 Part 2 Passed")

if __name__ == '__main__':
    unittest.main()