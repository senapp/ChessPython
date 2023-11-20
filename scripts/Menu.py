from scripts.Utilities import *
from scripts.Board import  getSize
from datetime import *

gameover = False
endTimeSeconds = 0
whiteWinner = False
startTime = datetime.now()

def seconds_between(d1, d2):
    return abs((d1 - d2).seconds)

def resetGame():
    global startTime, gameover
    startTime = datetime.now()
    gameover = False

def gameOver(whiteWon):
    global gameover, endTime, whiteWinner
    endTime = seconds_between(datetime.now(), startTime)
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

        drawText(width, height, myfont, menu, "Time: " + str(seconds_between(datetime.now(), startTime))+ "s", fontSize, (width + menuWidth / 2,height / 2))
    else:
        if (whiteWinner):
            drawText(width, height,myfont, menu, "White won!" , fontSize, (width + menuWidth / 2,height / 10))
        else:
            drawText(width, height,myfont, menu, "Black won!", fontSize, (width + menuWidth / 2,height / 10))
        drawText(width, height,myfont, menu, "Time: " + str(endTime) + "s", fontSize, (width + menuWidth / 2,height  - height / 8))
        drawText(width, height,myfont, menu, "Press R to restart", fontSize,  (width + menuWidth / 2,height / 2))
    return menu