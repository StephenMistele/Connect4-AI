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

#construct board at game start
grid = constructEmptyBoard()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawBoard(window, grid, selected, playerTurn, False)
    #draw score
    text = font.render('Red wins:' + str(wins[0]), True, (255,0,0))
    window.blit(text, (15, bounds[1]-90))
    text = font.render('Blue wins:' + str(wins[1]), True, (0,0,255))
    window.blit(text, (bounds[0]-350, bounds[1]-90))

    keys = pygame.key.get_pressed()
    keypressed = False
    if keys[pygame.K_LEFT]:
        selected = move(selected, -1)
        keypressed = True
    elif keys[pygame.K_RIGHT]:
        selected = move(selected, 1)
        keypressed = True
    elif keys[pygame.K_RETURN]:
        inserted = insert(grid, selected, playerTurn)
        if (inserted[1]):
            grid = inserted[0]
            if (checkIfWon(inserted[2], playerTurn, grid) > 0):
                drawBoard(window, grid, selected, playerTurn, True)
                if (playerTurn == 1):
                    text = font.render('Red Wins!', True, (0,255,0))
                else:
                    text = font.render('Blue Wins!', True, (0,255,0))
                window.blit(text, (bounds[0]/2-140, 10))
                text = font.render('Red wins:' + str(wins[0]), True, (255,0,0))
                window.blit(text, (15, bounds[1]-90))
                text = font.render('Blue wins:' + str(wins[1]), True, (0,0,255))
                window.blit(text, (bounds[0]-350, bounds[1]-90))
                pygame.display.update()
                pygame.time.wait(3000)
                grid = constructEmptyBoard()
                wins[playerTurn-1] += 1
                selected = 3
                playerTurn = changeTurn(playerTurn)
                continue
            playerTurn = changeTurn(playerTurn)
        keypressed = True

    pygame.display.update()
    if (keypressed):
        drawBoard(window, grid, selected, playerTurn, False)
        pygame.time.wait(200)