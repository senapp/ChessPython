from scripts.Menu import gameOver, resetGame
from scripts.Utilities import *
from scripts.Piece import *
from scripts.Board import getBoardPositonCenter, getRowAndCollum, getCellSize, getGrid, getSize

pieceSize = 250
piecesAmount = 0
whitePieceArray = []
blackPieceArray = []
redrawRequired = False
whitesTurn = True
lastMove = ["NONE", ""]

def removePieceFromPlay(isWhite, index):
    global redrawRequired
    if (isWhite):
        if (whitePieceArray[index].pieceType == 5): gameOver(False)
        whitePieceArray[index].alive = False
    else:
       if (blackPieceArray[index].pieceType == 5): gameOver(True)
       blackPieceArray[index].alive = False
    redrawRequired = True

def moveText(piece, newPos):
    move = [piece.getPieceName(),""]

    x, number = getRowAndCollum(piece.position)
    letter = getChar(x)
    move[1] = letter + str(getGrid()[1] - number)

    x, number = getRowAndCollum(newPos)
    letter = getChar(x)
    move[1] += " -> " + letter + str(getGrid()[1] - number)
    return move

def movePiece(isWhite, index, newPos):
    global redrawRequired, lastMove, whitesTurn
    if (isWhite):
        lastMove = moveText(whitePieceArray[index], newPos)
        whitePieceArray[index].position = newPos
        whitePieceArray[index].movesMade = 1 + whitePieceArray[index].movesMade
        whitesTurn = False
    else:
        lastMove = moveText(blackPieceArray[index], newPos)
        blackPieceArray[index].position = newPos
        blackPieceArray[index].movesMade = 1 + blackPieceArray[index].movesMade
        whitesTurn = True
    redrawRequired = True

def resetPieces():
    global whitePieceArray, blackPieceArray, lastMove
    whitePieceArray.clear()
    blackPieceArray.clear()
    lastMove = ["NONE", ""]
    resetGame()

def pieceManagerSetup(xGrid, yGrid, whiteStarts):
    global piecesAmount, whitesTurn, pieceSize
    whitesTurn = whiteStarts
    piecesAmount = xGrid * yGrid
    cell = getCellSize()
    pieceSize = cell * 5
    for y in range(yGrid):
        for x in range(xGrid):
            position = y * xGrid + x
            xCenter = math.floor(xGrid / 2)
            if position < xGrid:
                if x == xCenter: 
                    blackPieceArray.append(piece(position, 5, False))
                if x == xCenter - 1: 
                    blackPieceArray.append(piece(position, 4, False))
                if x == xCenter - 2 or x == xCenter + 1: 
                    blackPieceArray.append(piece(position, 3, False))
                if x == xCenter - 3 or x == xCenter + 2: 
                    blackPieceArray.append(piece(position, 2, False))
                if x == xCenter - 4 or x == xCenter + 3: 
                    blackPieceArray.append(piece(position, 1, False))
            elif position >= xGrid * (yGrid - 1):
                if x == xCenter: 
                    whitePieceArray.append(piece(position, 5, True))
                if x == xCenter - 1:
                    whitePieceArray.append(piece(position, 4, True))
                if x == xCenter - 2 or x == xCenter + 1: 
                    whitePieceArray.append(piece(position, 3, True))
                if x == xCenter - 3 or x == xCenter + 2: 
                    whitePieceArray.append(piece(position, 2, True))
                if x == xCenter - 4 or x == xCenter + 3: 
                    whitePieceArray.append(piece(position, 1, True))
            elif position >= xGrid and position < xGrid * 2:
                blackPieceArray.append(piece(position, 0, False))
            elif position >= xGrid * (yGrid - 2) and position < xGrid * (yGrid - 1):
                  whitePieceArray.append(piece(position, 0, True))

def getPieceOnCell(cell):
    for index, piece in enumerate(whitePieceArray):
        if (piece.position == cell and piece.alive):
            return index, piece

    for index, piece in enumerate(blackPieceArray):
        if (piece.position == cell and piece.alive):
            return index, piece

    return 0, 0
    
def drawPieces():
    global redrawRequired
    redrawRequired = False

    width, height = getSize()

    pieces = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    for pieceW in whitePieceArray:
        if pieceW.alive:
            pieceW.posLocations = getPossibleLocations(pieceW)
            drawSprite(width, height, pieces, pieceSprite.getPiece(pieceSprite("white"),pieceW.pieceType), pieceSize, getBoardPositonCenter(pieceW.position))
    for pieceB in blackPieceArray:
        if pieceB.alive:
            pieceB.posLocations = getPossibleLocations(pieceB)
            drawSprite(width, height, pieces, pieceSprite.getPiece(pieceSprite("black"),pieceB.pieceType), pieceSize, getBoardPositonCenter(pieceB.position))
    return pieces

def drawMovingPiece(currentPiece, currentposition):
    width, height = getSize()
    cellSize = getCellSize()
    x, y = getRowAndCollum(currentPiece.position)
    pieceColor = "black"

    movingPiece = pygame.Surface((width, height), pygame.SRCALPHA, 32)

    if currentPiece.isWhite: pieceColor = "white"
    if y % 2 == 0:
        if x % 2 == 0:
            pygame.draw.rect(movingPiece, getColor("white"), (x * cellSize, y * cellSize, cellSize, cellSize))
        else:
            pygame.draw.rect(movingPiece, getColor("black"), (x * cellSize, y * cellSize, cellSize, cellSize))
    else:
        if x % 2 == 0:
            pygame.draw.rect(movingPiece, getColor("black"), (x * cellSize, y * cellSize, cellSize, cellSize))
        else:
            pygame.draw.rect(movingPiece, getColor("white"), (x * cellSize, y * cellSize, cellSize, cellSize))
   
    for place in currentPiece.posLocations:
        x, y = getRowAndCollum(place)
        pygame.draw.rect(movingPiece, getColor("green"), (x * cellSize, y * cellSize, cellSize, cellSize))


    drawSprite(width, height, movingPiece, pieceSprite.getPiece(pieceSprite(pieceColor),currentPiece.pieceType), pieceSize, currentposition)
    return movingPiece

def getPossibleLocations(piece):
        places = []
        position = 0
        direction = 1
        xGrid, yGrid = getGrid()
        if not piece.isWhite: direction = -1

        if (piece.pieceType == 0):
            for i in range(2):
                position = piece.position - xGrid * direction * (i + 1)
                if (checkMove(piece, position, 0) and piece.movesMade * i == 0): places.append(position)
                else: break
            position = piece.position - xGrid * direction - 1
            if (checkMove(piece,position, 1)): places.append(position)
            position = piece.position - xGrid * direction + 1
            if (checkMove(piece,position, 1)): places.append(position)
        elif(piece.pieceType == 1):
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(xGrid - (piece.position % xGrid + 1)):
                position = piece.position + (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(yGrid - math.floor(piece.position / xGrid)):
                position = piece.position + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(math.floor(piece.position / xGrid)):
                position = piece.position - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
        elif(piece.pieceType == 2):
            if (piece.position % xGrid >= 1):
                position = piece.position + xGrid * 2 - 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position - xGrid * 2 - 1
                if (checkMove(piece,position, 2)): places.append(position)
            if (piece.position % xGrid <= xGrid - 2):
                position = piece.position - xGrid * 2 + 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + xGrid * 2 + 1
                if (checkMove(piece,position, 2)): places.append(position)
            if (piece.position % xGrid > 1):
                position = piece.position - xGrid - 2
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + xGrid - 2
                if (checkMove(piece,position, 2)): places.append(position)
            if (piece.position % xGrid < xGrid - 2):
                position = piece.position - xGrid + 2
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + xGrid + 2
                if (checkMove(piece,position, 2)): places.append(position)
        elif(piece.pieceType == 3):
            for i in range(xGrid - (piece.position % xGrid) - 1):
                position = piece.position + (i + 1) + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1) + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(xGrid - (piece.position % xGrid) - 1):
                position = piece.position + (i + 1) - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1) - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
        elif(piece.pieceType == 4):
            for i in range(xGrid - (piece.position % xGrid) - 1):
                position = piece.position + (i + 1) + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1) + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(xGrid - (piece.position % xGrid) - 1):
                position = piece.position + (i + 1) - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1) - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(piece.position % xGrid):
                position = piece.position - (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(xGrid - (piece.position % xGrid + 1)):
                position = piece.position + (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(yGrid - math.floor(piece.position / xGrid)):
                position = piece.position + xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
            for i in range(math.floor(piece.position / xGrid)):
                position = piece.position - xGrid * (i + 1)
                if (checkMove(piece,position, 2)): places.append(position)
                else: break
                if (not checkMove(piece,position, 0)): break
        elif (piece.pieceType == 5):
            position = piece.position - xGrid
            if (checkMove(piece,position, 2)): places.append(position)
            position = piece.position + xGrid
            if (checkMove(piece,position, 2)): places.append(position)

            if (piece.position % xGrid <= xGrid - 2):
                position = piece.position - xGrid + 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + xGrid + 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + 1
                if (checkMove(piece,position, 2)): places.append(position)

            if (piece.position % xGrid >= 1):
                position = piece.position - xGrid - 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position + xGrid - 1
                if (checkMove(piece,position, 2)): places.append(position)
                position = piece.position - 1
                if (checkMove(piece,position, 2)): places.append(position)  
        return places

def checkMove(piece, position, moveType):
    xGrid, yGrid = getGrid()
    if (position < 0 or position >= xGrid * yGrid): return False
    if (getPieceOnCell(position)[1] == 0 and moveType == 0): return True
    elif (getPieceOnCell(position)[1] == 0 and moveType == 2): return True
    elif (getPieceOnCell(position)[1] != 0):
        if (not getPieceOnCell(position)[1].isWhite and piece.isWhite and moveType == 1): return True
        elif (getPieceOnCell(position)[1].isWhite and not piece.isWhite and moveType == 1): return True
        elif (not getPieceOnCell(position)[1].isWhite and piece.isWhite and moveType == 2): return True
        elif (getPieceOnCell(position)[1].isWhite and not piece.isWhite and moveType == 2): return True
        else: return False
    else: return False

def isWhitesTurn():
    global whitesTurn
    return whitesTurn

def getLastMove():
    global lastMove
    return lastMove

def isRedrawRequired():
    global redrawRequired
    return redrawRequired