# Read each line of the input file as an integer
masses = [int(x) for x in open("fuel.txt").readlines()]

# For each mass, we need to calculate the required amount of fuel:
totalFuel = sum([int(m / 3) - 2 for m in masses])

# Print the final solution:
print(totalFuel)