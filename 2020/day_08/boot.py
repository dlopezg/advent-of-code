def parseInstruction(file):
    bootProgram = [line.strip() for line in open(file).readlines()]
    for idx,instruction in enumerate(bootProgram):
        action,buffer = instruction.split(' ')
        bootProgram[idx] = list((action,int(buffer)))
    return bootProgram

def executeInstruction(instruction):
    action,offset = instruction
    if action == 'nop':
        return(1,0)
    if action == 'acc':
        return(1,offset)
    if action == 'jmp':
        return(offset,0)

def execute(program):
    pointer,accumulator = 0,0
    executionList = [False] * len(program)
    while True:
        if pointer == len(program):
            return accumulator

        if executionList[pointer]:
            # Return accumulator for exercise 1
            # Return False for exercise 2
            return False  
        
        p,o = executeInstruction(program[pointer])
        executionList[pointer] = True
        pointer += p
        accumulator += o

def debug(programToDebug):
    modProg = programToDebug.copy() 
    for pointer,instruction in enumerate(modProg):
        action,offset = instruction
        
        # Change instruction:
        if action == 'nop':
            modProg[pointer][0] = 'jmp'
        if action == 'jmp':
            modProg[pointer][0] = 'nop'

        # Try the new program:
        terminated = execute(modProg)
        if terminated: 
            return terminated

        # Reset the instruction to initial values
        if action == 'nop':
            modProg[pointer][0] = 'nop'
        if action == 'jmp':
            modProg[pointer][0] = 'jmp'

# Exercise 1:
# print(execute(parseInstruction('boot.txt')))
# Exercise 2:
print(debug(parseInstruction('boot.txt')))