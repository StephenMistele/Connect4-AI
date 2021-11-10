import pygame
from win import * 
from functions import *
pygame.init()
bounds = (1200,800)
window = pygame.display.set_mode(bounds)
block_size = 20
font = pygame.font.SysFont('comicsans',60, True)
selected = 0
playerTurn = 1

#construct board at game start
grid = []
for x in range(7):
    column=[]
    for y in range(6):
        column.append(0)
    grid.append(column)

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawBoard(window, grid)

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
                drawBoard(window, grid)
                if (playerTurn == 1):
                    text = font.render('Red Wins!', True, (0,255,0))
                else:
                    text = font.render('Blue Wins!', True, (0,255,0))
                window.blit(text, (bounds[0]/2-100, bounds[1]/2-100))
                pygame.display.update()
                pygame.time.wait(1000)
                run = False
            playerTurn = changeTurn(playerTurn)
        keypressed = True

    pygame.display.update()
    if (keypressed):
        pygame.time.wait(200)