def playMemoryGame(startingNumbers):
    # Initialize the memory:
    spoken = {}
    turn = 1
    for number in startingNumbers:
        spoken[number] = turn
        turn += 1

    spokenNumber = 0  # Hardcoded and start!

    for turn in range(len(startingNumbers)+1, 30000000):
        if spokenNumber in spoken:
            distance = turn - spoken[spokenNumber]
            spoken[spokenNumber] = turn
            spokenNumber = distance
            continue
        spoken[spokenNumber] = turn
        spokenNumber = 0
        continue

    return spokenNumber


startingNumbers = [1, 20, 8, 12, 0, 14]
print(playMemoryGame(startingNumbers))
