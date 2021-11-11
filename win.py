#driver function for checking wins
def checkIfWon(location, playerTurn, grid):
    won = 0
    for x in range(4):
        won += wonH(x, location, playerTurn, grid)
        won += wonV(x, location, playerTurn, grid)
        won += wonDiagDecrease(x, location, playerTurn, grid)
        won += wonDiagIncrease(x, location, playerTurn, grid)
    return won

#check if horizontal win surrounding most recent piece played
def wonH(offset, location, playerTurn, grid):
    count = 0
    if (location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            if (grid[location[0] - x + offset][location[1]] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

#check if vertical win surrounding most recent piece played
def wonV(offset, location, playerTurn, grid):
    count = 0
    if (location[1] - 3 + offset >= 0 and location[1] + offset <= 5):
        for x in range(4):
            if (grid[location[0]][location[1] - x + offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

#check if diagonal decreasing win surrounding most recent piece played
def wonDiagDecrease(offset, location, playerTurn, grid):
    count = 0
    if (location[1] - 3 + offset >= 0 and location[1] + offset <= 5 and location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            if (grid[location[0] - x + offset][location[1] - x + offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

#check if diagonal increasing win surrounding most recent piece played
def wonDiagIncrease(offset, location, playerTurn, grid):
    count = 0
    if (location[1] + 3 - offset <= 5 and location[1] - offset >= 0 and location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            if (grid[location[0] - x + offset][location[1] + x - offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0