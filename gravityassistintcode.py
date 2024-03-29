import variables
#Part1 Function: Restoring IntCode 
def gravityassist_intcode(program):
    for i in range(0, len(program), 4): # for loop to iterate all the input with diferrences by 4 positions
        opcode = program[i]

        if opcode == 99:  # Halt the Program
            break
        elif opcode == 1:  # Addition of position 1 & 2 and result in position 3
            try:
                pos1 = program[i+1]
                pos2 = program[i+2]
                pos3 = program[i+3]
                program[pos3] = program[pos1] + program[pos2]
            except IndexError: # Error Handling if index is out of range 
                print("Error: Index out of range.")
                return None
        elif opcode == 2:  # Multiplication of position 1 & 2 and result in position 3
            try:
                pos1 = program[i+1]
                pos2 = program[i+2]
                pos3 = program[i+3]
                program[pos3] = program[pos1] * program[pos2]
            except IndexError: # Error Handling if index is out of range
                print("Error: Index out of range.")
                return None
        else:
            print(f"Error: Unknown opcode {opcode}") # unknown opcode
            return None

    return program[0]

#Part2 Function: Finding input from target output
def find_input_for_output(program_copy, target_output):
    for noun in range(100): # for loop used provide range of noun between 0-99
        for verb in range(100): # for loop used provide range of verb between 0-99
            # Make a copy of the program
            program = program_copy[:]
            # Set noun and verb
            program[1] = noun
            program[2] = verb
            try:
                output = gravityassist_intcode(program)
                if output == target_output:
                    return noun, verb
            except ValueError as e: # Error Handling in case of value error
                print(f"Error: {e}")
                return None, None
    return None, None


#Finding outputs for both Part1 and Part2
# Fetching input from file
with open('./input.txt', 'r') as _file:
  strInputs = _file.read().split(',')
inputs = list(map(lambda str: int(str), strInputs))

# Part 1 Output: Restore the gravity assist program
restored_program=inputs[:]
# Before running the program, replace position 1 and 2 with 12 and 2 respectively
restored_program[1] = variables.restored_program1 #Replacing variables
restored_program[2] = variables.restored_program2 #Replacing variables

result = gravityassist_intcode(restored_program)
if result is not None:
      print(f"Value left at position 0 after the program halts: {result}")
else:
      print("Execution failed.")


# Part 2 Output: Find the inputs for the target output
target_output = variables.target_output
noun, verb = find_input_for_output(inputs, target_output)
if noun is not None and verb is not None:
        result1 = 100 * noun + verb
        print("Noun:", noun)
        print("Verb:", verb)
        print(f"The solution result after addition of noun & verb multiplied by 100: {result1}")
else:
        print("Failed to find input for the target output.")