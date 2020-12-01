# Importamos las funciones necesarias:
from intcodeProgram import readProgram, computeProgram

# Función para buscar el par de valores:
def findValues():
    for i in range(0,99):
        for j in range(0,99):
            # Inicializamos el programa:
            intcode = readProgram("intcodeProgram.txt")
            intcode[1],intcode[2] = i,j

            # Ejecutamos el programa:
            intcode = computeProgram(intcode)

            # Comprobamos la respuesta:
            if intcode[0] == 19690720:
                return 100 * intcode[1] + intcode[2]
    return "Error"

print(findValues())