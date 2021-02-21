from scripts.Piece import piece
from scripts.Board import getCellOnMouse
from scripts.PieceManager import getPieceOnCell, isWhitesTurn, movePiece, pieceMakeMove, removePieceFromPlay

# First val = index in pieceArray, second val = piece object
heldPiece = 0,0
holdingPiece = False

def mouseDown(position):
    global holdingPiece, heldPiece
    if (holdingPiece): return

    pos = getCellOnMouse(position)
    heldPiece = getPieceOnCell(pos)
    if (heldPiece[1] != 0):
        if (heldPiece[1].isWhite == isWhitesTurn()):
            holdingPiece = True

def mouseReleased(position):
    global holdingPiece, heldPiece
    if (holdingPiece):
        pos = getCellOnMouse(position)
        if (pos in heldPiece[1].posLocations):
            pieceMakeMove(pos, heldPiece[0], heldPiece[1], True)
    holdingPiece = False

def getHoldingPiece():
    global heldPiece
    return heldPiece

def isHoldingPiece():
    global holdingPiece
    return holdingPiece


