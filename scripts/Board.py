from scripts.Utilities import *

width = 0
height = 0
xGrid = 0
yGrid = 0
cellSize = 0
blackAndWhiteColor = True

def setupBoard(w, h, x, y, cell, blackAndWhite):
    global width, height, xGrid, yGrid, cellSize, blackAndWhiteColor
    width = w
    height = h
    xGrid = x
    yGrid = y
    cellSize = cell
    blackAndWhiteColor = blackAndWhite

def drawBoard():
    board = pygame.Surface((width, height))
    for y in range(yGrid):
        for x in range(xGrid):
            color = ""
            if (y + x) % 2 == 0:
                color = "black"
                if blackAndWhiteColor == False:
                    color = "brown"
            else:
                color = "white"
                if blackAndWhiteColor == False:
                    color = "lightbrown"
            pygame.draw.rect(board, getColor(color), (x * cellSize, y * cellSize, cellSize, cellSize))

    return board

def getBoardPositonCenter(position):
    row = math.floor(position / xGrid)
    collum = position % xGrid
    return cellSize / 2 + cellSize * collum, cellSize / 2 + cellSize * row

def getRowAndCollum(cell):
    row = math.floor(cell / xGrid)
    collum = cell % xGrid
    return collum, row

def getCellOnMouse(position):
    row = math.floor(position[1] / cellSize)
    if ((position[1] / cellSize) > 8):
        return -1
    collum = math.floor(position[0] / cellSize)
    if ((position[0] / cellSize) > 8):
        return -1
    return row * xGrid + collum

def getBoardPosition(position):
    row = math.floor(position / xGrid)
    collum = position % xGrid
    return cellSize * collum, cellSize * row

def getGrid():
    global xGrid, yGrid
    return xGrid, yGrid

def getCellSize():
    global cellSize
    return cellSize

def getSize():
    global width, height
    return width, height