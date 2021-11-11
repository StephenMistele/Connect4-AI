import pygame

#check to see if user wants to close game
def checkQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

#try insert a puck into a given row
def insert(grid, col, player):
    successful = True
    location = (0,0)
    #Full Col
    if (grid[col][0] != 0):
        successful = False
        location = (col,0)
    #Empty Col
    elif (grid[col][5] == 0):
        grid[col][5] = player
        successful = True
        location = (col,5)
    #Regular insert
    else:
        for x in range(5):
            if (grid[col][x+1] != 0):
                grid[col][x] = player
                successful = True
                location = (col,x)
                break
    return (successful, grid, location)

#given a piece location and 2d array representing pieces, return the appropriate color to display for that piece
def getColorPiece(grid, col, row):
    if (grid[col][row] == 0):
        return (255,255,255)
    if (grid[col][row] == 1):
        return (255,0,0)
    if (grid[col][row] == 2):
        return (0,0,255)

#get color of current player turn
def getColorSlider(playerTurn):
    if (playerTurn == 1):
        return (255,0,0)
    return (0,0,225)

#change turn
def changeTurn(playerTurn):
    if (playerTurn == 1):
        return 2
    return 1

#move column cursor left or right and wrap if needed
def move(selected, direction):
    if (selected+direction < 0):
        return 6
    if (selected+direction > 6):
        return 0
    return selected+direction

#draws the board. This includes the game board and the cursor piece
def drawBoard(window, grid, selected, playerTurn, won):
    #draw pieces
    window.fill((0,0,0))
    centerx = 100
    for x in range(7):
        centery = 170
        for y in range(6):
            pygame.draw.circle(window, getColorPiece(grid, x, y), (centerx, centery), 50)
            centery += 110
        if (selected == x and not won):
            pygame.draw.circle(window, getColorSlider(playerTurn), (centerx, 60), 50)
        centerx += 110
    
#returns an empty playing board
def constructEmptyBoard():
    grid=[]
    for x in range(7):
        column=[]
        for y in range(6):
            column.append(0)
        grid.append(column)
    return grid

#displays score at bottom
def drawScore(font, window, bounds, wins):
    text = font.render('Red wins:' + str(wins[0]), True, (255,0,0))
    window.blit(text, (15, bounds[1]-90))
    text = font.render('Blue wins:' + str(wins[1]), True, (0,0,255))
    window.blit(text, (bounds[0]-350, bounds[1]-90))

#runs on game win
def drawWinText(font, bounds, window, wins, playerTurn):
    if (playerTurn == 1):
        text = font.render('Red Wins!', True, (0,255,0))
    else:
        text = font.render('Blue Wins!', True, (0,255,0))
    window.blit(text, (bounds[0]/2-140, 10))
    drawScore(font, window, bounds, wins)
    pygame.display.update()
    pygame.time.wait(3000)