import pygame
pygame.init()
bounds = (1200,800)
window = pygame.display.set_mode(bounds)
block_size = 20

def insert(grid, col, numrows, player):
    numrows-=1
    successful = True
    location = (0,0)
    #Full Col
    if (grid[col][0] != 0):
        successful = False
        location = (col,0)
    #Empty Col
    elif (grid[col][numrows] == 0):
        grid[col][numrows] = player
        successful = True
        location = (col,numrows)
    else:
        for x in range(numrows):
            if (grid[col][x+1] != 0):
                grid[col][x] = player
                successful = True
                location = (col,x)
                break
    return (grid, successful, location)

def getColor(grid, col, row):
    if (grid[col][row] == 0):
        return (255,255,255)
    if (grid[col][row] == 1):
        return (255,0,0)
    if (grid[col][row] == 2):
        return (0,0,255)

def changeTurn(playerTurn):
    if (playerTurn == 1):
        return 2
    return 1

def move(selected, direction):
    if (selected+direction < 0):
        return 6
    if (selected+direction > 6):
        return 0
    return selected+direction

def wonH(offset, location, playerTurn, grid):
    count = 0
    if (location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            if (grid[location[0] - x + offset][location[1]] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

def wonV(offset, location, playerTurn, grid):
    count = 0
    if (location[1] - 3 + offset >= 0 and location[1] + offset <= 5):
        for x in range(4):
            if (grid[location[0]][location[1] - x + offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

def wonDiagDecrease(offset, location, playerTurn, grid):
    count = 0
    if (location[1] - 3 + offset >= 0 and location[1] + offset <= 5 and location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            if (grid[location[0] - x + offset][location[1] - x + offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

def wonDiagIncrease(offset, location, playerTurn, grid):
    count = 0
    if (location[1] + 3 - offset <= 5 and location[1] - offset >= 0 and location[0] - 3 + offset >= 0 and location[0] + offset <= 6):
        for x in range(4):
            print(grid[location[0] - x + offset][location[1] + x - offset], playerTurn)
            if (grid[location[0] - x + offset][location[1] + x - offset] == playerTurn):
                count += 1
    if (count == 4):
        return 1
    return 0

def checkIfWon(location, playerTurn, grid):
    won = 0
    for x in range(4):
        won += wonH(x, location, playerTurn, grid)
        won += wonV(x, location, playerTurn, grid)
        won += wonDiagDecrease(x, location, playerTurn, grid)
        won += wonDiagIncrease(x, location, playerTurn, grid)
    return won

selected = 0
playerTurn = 1
grid = []
numcolumns = 7
numrows = 6
for x in range(numcolumns):
    column=[]
    for y in range(numrows):
        column.append(0)
    grid.append(column)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0,0,0))

    
    centerx = 100
    centery = 100
    for x in range(numcolumns):
        for y in range(numrows):
            pygame.draw.circle(window, getColor(grid, x, y), (centerx, centery), 50)
            centery += 110
        centery = 100
        centerx += 110

    keys = pygame.key.get_pressed()
    keypressed = False
    if keys[pygame.K_LEFT]:
        selected = move(selected, -1)
        keypressed = True
    elif keys[pygame.K_RIGHT]:
        selected = move(selected, 1)
        keypressed = True
    elif keys[pygame.K_RETURN]:
        inserted = insert(grid, selected, numrows, playerTurn)
        if (inserted[1]):
            grid = inserted[0]
            if (checkIfWon(inserted[2], playerTurn, grid) > 0):
                print("DONEDONEDONE", checkIfWon(inserted[2], playerTurn, grid) > 0)
            playerTurn = changeTurn(playerTurn)
        keypressed = True

    pygame.display.update()
    if (keypressed):
        pygame.time.wait(200)