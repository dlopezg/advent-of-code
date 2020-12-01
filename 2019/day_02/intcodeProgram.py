# Función para leer y separar por comas:
def readProgram(filename):
    return [int(x) for x in open(filename).read().split(",")]

# Función para ejecutar el programa:
def computeProgram(intcode):
    instructionPointer = 0

    while True:
        opcode = intcode[instructionPointer]
        param  = intcode[instructionPointer + 1]
        param_ = intcode[instructionPointer + 2]
        output = intcode[instructionPointer + 3]

        value =  intcode[param]
        value_ = intcode[param_]

        instructionPointer += 4

        if opcode == 1:
            intcode[output] = value + value_
        elif opcode == 2:
            intcode[output] = value * value_
        elif opcode == 99:
            return intcode

# Leer el programa del archivo de entrada:
intcode = readProgram("intcodeProgram.txt")
# Inicializamos la memoria:
intcode[1],intcode[2] = 12,2
# Ejecutamos el programa y mostramos la salida:     
print(computeProgram(intcode))