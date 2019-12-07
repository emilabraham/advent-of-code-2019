import copy
#Instructions

instructions =[
        1,12,2,3,
        1,1,2,3,
        1,3,4,3,
        1,5,0,3,
        2,1,9,19,
        1,10,19,23,
        2,9,23,27,
        1,6,27,31,
        2,31,9,35,
        1,5,35,39,
        1,10,39,43,
        1,10,43,47,
        2,13,47,51,
        1,10,51,55,
        2,55,10,59,
        1,9,59,63,
        2,6,63,67,
        1,5,67,71,
        1,71,5,75,
        1,5,75,79,
        2,79,13,83,
        1,83,5,87,
        2,6,87,91,
        1,5,91,95,
        1,95,9,99,
        1,99,6,103,
        1,103,13,107,
        1,107,5,111,
        2,111,13,115,
        1,115,6,119,
        1,6,119,123,
        2,123,13,127,
        1,10,127,131,
        1,131,2,135,
        1,135,5,0,
        99,2,14,0,0]

def run2(program):
    for n in range(0,100):
        for v in range(0,100):
            tempProgram = copy.copy(program)
            tempProgram[1] = n
            tempProgram[2] = v
            if run(tempProgram) == 19690720:
                return 100 * n + v

def run(myinstructions):
    program = copy.copy(myinstructions)
    head = 0
    halt = False
    while not halt:
        if program[head] == 99: #halt
            halt = True
        elif program[head] == 1: #add
            head = add(head, program)
        elif program[head] == 2: #multiply
            head = multiply(head, program)
        else:
            print("Something went wrong!")
            print("Head: % 3d, Value: % 3d" % (head, program[head]))
            halt = True

    return program[0]

#add 2 positions and store them in the third. Return new head position
def add(head, program):
    program[program[head+3]] = program[program[head+1]] + program[program[head+2]]
    return head+4

#multiply 2 positions and store them in the third. Return new head position
def multiply(head, program):
    program[program[head+3]] = program[program[head+1]] * program[program[head+2]]
    return head+4

#print(run(instructions))
#print(run2(instructions))
