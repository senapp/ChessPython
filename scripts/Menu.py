from scripts.Utilities import *
from scripts.Board import  getSize
from timeit import default_timer as timer

gameover = False
endTime = 0
whiteWinner = False
startTime = 0

def resetGame():
    global startTime, gameover
    startTime = round(timer(), 1)
    gameover = False

def gameOver(whiteWon):
    global gameover, endTime, whiteWinner
    endTime = round(timer() - startTime, 1)
    whiteWinner = whiteWon
    gameover = True

def drawMenu(menuWidth, myfont, fontSize, whitesTurn, lastMove):
    width, height = getSize()

    menu = pygame.Surface((width + menuWidth, height), pygame.SRCALPHA, 32)

    pygame.draw.rect(menu, getColor("white"), (width, 0, menuWidth, height))
    pygame.draw.line(menu, getColor("black"), (width, 0), (width, height))

    if (not gameover):
        if (whitesTurn):
            drawText(width, height,myfont, menu, "White's turn", fontSize, (width + menuWidth / 2,height - height / 10))
            drawText(width, height,myfont, menu, "Move: " + lastMove[0], fontSize, (width + menuWidth / 2,height / 8))
            drawText(width, height,myfont, menu, lastMove[1], fontSize, (width + menuWidth / 2,height / 6))
        else:
            drawText(width, height,myfont, menu, "Black's turn", fontSize, (width + menuWidth / 2,height / 10))
            drawText(width, height,myfont, menu, "Move: " + lastMove[0], fontSize, (width + menuWidth / 2,height  - height / 8))
            drawText(width, height,myfont, menu, lastMove[1], fontSize, (width + menuWidth / 2,height  - height / 11))

        drawText(width, height, myfont, menu, "Time: " + str(round(timer() - startTime, 1))+ "s", fontSize, (width + menuWidth / 2,height / 2))
    else:
        if (whiteWinner):
            drawText(width, height,myfont, menu, "White won!" , fontSize, (width + menuWidth / 2,height / 10))
        else:
            drawText(width, height,myfont, menu, "Black won!", fontSize, (width + menuWidth / 2,height / 10))
        drawText(width, height,myfont, menu, "Time: " + str(endTime) + "s", fontSize, (width + menuWidth / 2,height  - height / 8))
        drawText(width, height,myfont, menu, "Press R to restart", fontSize,  (width + menuWidth / 2,height / 2))
    return menu