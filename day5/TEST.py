from intCode import add, multiply 
import copy

instructions = [
    3,225,
    1,225,6,6,
    1100,1,238,225,
    104,0,1101,37,34,224,
    101,-71,224,224,
    4,224,1002,223,
    8,223,101,6,
    224,224,1,224,
    223,223,1002,113,
    50,224,1001,224,
    -2550,224,4,224,
    1002,223,8,223,
    101,2,224,224,
    1,223,224,223,
    1101,13,50,225,
    102,7,187,224,
    1001,224,-224,224,
    4,224,1002,223,
    8,223,1001,224,
    5,224,1,224,
    223,223,1101,79,
    72,225,1101,42,
    42,225,1102,46,
    76,224,101,-3496,
    224,224,4,224,
    102,8,223,223,
    101,5,224,224,
    1,223,224,223,
    1102,51,90,225,
    1101,11,91,225,
    1001,118,49,224,
    1001,224,-140,224,
    4,224,102,8,
    223,223,101,5,
    224,224,1,224,
    223,223,2,191,
    87,224,1001,224,
    -1218,224,4,224,
    1002,223,8,223,
    101,4,224,224,
    1,224,223,223,
    1,217,83,224,
    1001,224,-124,224,
    4,224,1002,223,
    8,223,101,5,
    224,224,1,223,
    224,223,1101,32,
    77,225,1101,29,
    80,225,101,93,
    58,224,1001,224,
    -143,224,4,224,
    102,8,223,223,
    1001,224,4,224,
    1,223,224,223,
    1101,45,69,225,
    4,223,99,0,
    0,0,677,0,
    0,0,0,0,
    0,0,0,0,
    0,0,1105,0,
    99999,1105,227,247,
    1105,1,99999,1005,
    227,99999,1005,0,
    256,1105,1,99999,
    1106,227,99999,1106,
    0,265,1105,1,
    99999,1006,0,99999,
    1006,227,274,1105,
    1,99999,1105,1,
    280,1105,1,99999,
    1,225,225,225,
    1101,294,0,0,
    105,1,0,1105,
    1,99999,1106,0,
    300,1105,1,99999,
    1,225,225,225,
    1101,314,0,0,
    106,0,0,1105,
    1,99999,7,226,
    226,224,102,2,
    223,223,1005,224,
    329,101,1,223,
    223,108,677,226,
    224,102,2,223,
    223,1005,224,344,
    1001,223,1,223,
    1108,226,677,224,
    102,2,223,223,
    1005,224,359,1001,
    223,1,223,8,
    677,226,224,102,
    2,223,223,1006,
    224,374,1001,223,
    1,223,107,226,
    226,224,102,2,
    223,223,1006,224,
    389,101,1,223,
    223,1108,677,226,
    224,1002,223,2,
    223,1005,224,404,
    1001,223,1,223,
    108,677,677,224,
    102,2,223,223,
    1005,224,419,101,
    1,223,223,7,226,
    677,224,1002,223,
    2,223,1006,224,434,
    1001,223,1,223,
    107,226,677,224,
    102,2,223,223,
    1005,224,449,101,
    1,223,223,1108,677,
    677,224,1002,223,
    2,223,1006,224,464,
    101,1,223,223,
    7,677,226,224,102,
    2,223,223,1006,224,
    479,101,1,223,
    223,1007,677,677,
    224,1002,223,2,
    223,1005,224,494,
    101,1,223,223,
    1008,226,226,224,
    102,2,223,223,
    1006,224,509,1001,
    223,1,223,107,
    677,677,224,102,
    2,223,223,1006,224,
    524,1001,223,1,
    223,8,226,226,
    224,1002,223,2,
    223,1005,224,539,
    1001,223,1,223,
    1007,677,226,224,
    102,2,223,223,
    1006,224,554,1001,
    223,1,223,1007,
    226,226,224,1002,
    223,2,223,1005,
    224,569,1001,223,
    1,223,8,226,677,
    224,1002,223,2,
    223,1006,224,584,
    101,1,223,223,
    108,226,226,224,
    1002,223,2,223,
    1006,224,599,101,
    1,223,223,1107,677,
    226,224,1002,223,
    2,223,1005,224,614,
    1001,223,1,223,
    1107,226,677,224,
    102,2,223,223,
    1006,224,629,1001,
    223,1,223,1008,
    226,677,224,102,
    2,223,223,1005,224,
    644,101,1,223,
    223,1107,226,226,
    224,102,2,223,
    223,1006,224,659,
    1001,223,1,223,
    1008,677,677,224,
    102,2,223,223,
    1006,224,674,1001,
    223,1,223,4,
    223,99,226
]

testInstructions = [1002,4,3,4,33]
testInstructions2 = [3,0,4,0,99]

# Prompt for input and store at the next position's value. Return new head
# position
def inputoc(head, program):
    inVal = input("Please enter a value: ")
    program[program[head+1]] = inVal
    return head+2

# Print out the value at the next position's value. Return new head position
def output(head, program):
    print(program[program[head+1]])
    return head+2

def run(myinstructions):
    program = copy.copy(myinstructions)
    head = 0
    halt = False
    while not halt:
        if program[head] == 99: #halt
            print("Found a halt")
            print(program)
            halt = True
        elif program[head] == 1: #add
            #print("Current operation: %d, %d, %d, %d" % (program[head],
            #                                             program[head+1],
            #                                             program[head+2],
            #                                             program[head+3]))
            head = add(head, program)
        elif program[head] == 2: #multiply
            #print("Current operation: %d, %d, %d, %d" % (program[head],
            #                                             program[head+1],
            #                                             program[head+2],
            #                                             program[head+3]))
            head = multiply(head, program)
        elif program[head] == 3: #input
            #print("Current operation: %d, %d" % (program[head],
            #                                     program[head+1]))
            head = inputoc(head, program)
            #print(program[225])
        elif program[head] == 4: #output
            #print("Current operation: %d, %d" % (program[head],
            #                                     program[head+1]))
            head = output(head, program)
        else:
            head = parameterMode(head, program)    

    return program[0]

# TODO: Might need to handle 3. Not sure yet. Just make sure it isn't completely
# broken for now
def parameterMode(head, program):
    param = program[head]
    opcode = program[head] % 10
    opInstructions = opcodeParams(program[head])
    if opcode == 1:
        firstValue = checkMode(program[head+1], opInstructions[0], program)
        secondValue = checkMode(program[head+2], opInstructions[1], program)
        destination = program[head+3]
        #print("Current operation: %d, %d, %d, %d" % (program[head],
        #                                             firstValue,
        #                                             secondValue,
        #                                             destination))
        return addParam(head, firstValue, secondValue, destination, program)
    elif opcode == 2:
        firstValue = checkMode(program[head+1], opInstructions[0], program)
        secondValue = checkMode(program[head+2], opInstructions[1], program)
        destination = program[head+3]
        #print("Current operation: %d, %d, %d, %d" % (program[head],
        #                                             firstValue,
        #                                             secondValue,
        #                                             destination))
        return multiplyParam(head, firstValue, secondValue, destination, program)
    elif opcode == 4:
        value = checkMode(program[head+1], opInstructions[0], program)
        #print("Current operation: %d, %d" % (program[head],
        #                                     value))
        return outputParam(head, value)
    else:
        print("Something went wrong inside parameterMode")
        #print("Head: % 3d, Value: % 3d" % (head, program[head]))
        halt = True

# Based on the opcode return either the immediate or position
# code will be one of the items in the array returned by opcode function
def checkMode(param, code, program):
    return param if code == 1 else program[param]

def addParam(head, firstVal, secondVal, destination, program):
    program[destination] = firstVal + secondVal
    return head+4

def multiplyParam(head, firstVal, secondVal, destination, program):
    program[destination] = firstVal * secondVal
    return head+4

def outputParam(head, value):
    print(value)
    return head+2

# Return an array representing the array representation of the opcode
# 101 => [1, 0, 0]
# 1101 => [1, 1, 0]
# 10101 => [1, 0, 1]
# The array indicates the mode of each paramter from left to right
def opcodeParams(head):
    length = len(str(head))
    if length == 3:
        return [1, 0, 0]
    if length == 4:
        return [digitPlace(head, 3), 1, 0]
    if length == 5:
        return [digitPlace(head, 3), digitPlace(head, 4), 1]
    else:
        print("Something went wrong reading the opcode")

# Find the nth position in the given digit
def digitPlace(digit, position):
    divisor = (10 ** (position - 1))
    return (digit // divisor) % 10

#print(run(testInstructions))
#print(run(testInstructions2))
print(run(instructions))
