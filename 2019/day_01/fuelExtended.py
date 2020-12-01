# Fuel required for a given module:
def fuelForMass (mass):
    return int(mass / 3) - 2

# Recursive function to calculate extra fuel:
def fuelForFuel (fuel):
    extraFuel = fuelForMass(fuel)
    if extraFuel <= 0 :
        return fuel
    else:
        return  fuel + fuelForFuel(extraFuel)

# Read each line of the input file as an integer:
masses = [int(x) for x in open("fuelExtendedInput.txt").readlines()]
totalFuels = sum([fuelForFuel(fuelForMass(mass)) for mass in masses])
print(totalFuels)