import pygame
from win import * 
from functions import *
pygame.init()
bounds = (870,850)
window = pygame.display.set_mode(bounds)
block_size = 20
font = pygame.font.SysFont('comicsans',60, True)
selected = 3
playerTurn = 1
wins = [0,0]
grid = constructEmptyBoard()

#game loop
run = True
while run:
    run = checkQuit()
    drawBoard(window, grid, selected, playerTurn, False)
    drawScore(font, window, bounds, wins)

    keys = pygame.key.get_pressed()
    keypressed = False
    if keys[pygame.K_LEFT]:
        selected = move(selected, -1)
        keypressed = True
    elif keys[pygame.K_RIGHT]:
        selected = move(selected, 1)
        keypressed = True
    elif keys[pygame.K_RETURN]:
        insertInfoTouple = insert(grid, selected, playerTurn)
        keypressed = True
        if (insertInfoTouple[0]):
            grid = insertInfoTouple[1]
            if (checkIfWon(insertInfoTouple[2], playerTurn, grid) > 0):
                drawBoard(window, grid, selected, playerTurn, True)
                drawWinText(font, bounds, window, wins, playerTurn)
                grid = constructEmptyBoard()
                wins[playerTurn-1] += 1
                selected = 3
                playerTurn = changeTurn(playerTurn)
                continue
            playerTurn = changeTurn(playerTurn)

    pygame.display.update()
    if (keypressed):
        drawBoard(window, grid, selected, playerTurn, False)
        pygame.time.wait(200)