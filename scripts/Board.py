from scripts.Utilities import *

width = 0
height = 0
xGrid = 0
yGrid = 0
cellSize = 0

def setupBoard(w, h, x, y, cell):
    global width, height, xGrid, yGrid, cellSize
    width = w
    height = h
    xGrid = x
    yGrid = y
    cellSize = cell

def drawBoard():
    board = pygame.Surface((width, height))
    for y in range(yGrid):
        for x in range(xGrid):
            if y % 2 == 0:
                if x % 2 == 0:
                    pygame.draw.rect(board, getColor("white"), (x * cellSize, y * cellSize, cellSize, cellSize))
                else:
                    pygame.draw.rect(board, getColor("black"), (x * cellSize, y * cellSize, cellSize, cellSize))
            else:
                if x % 2 == 0:
                    pygame.draw.rect(board, getColor("black"), (x * cellSize, y * cellSize, cellSize, cellSize))
                else:
                    pygame.draw.rect(board, getColor("white"), (x * cellSize, y * cellSize, cellSize, cellSize))
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
    collum = math.floor(position[0] / cellSize) 
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