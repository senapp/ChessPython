from scripts.Piece import piece
from scripts.Board import getCellOnMouse
from scripts.PieceManager import getPieceOnCell, isWhitesTurn, movePiece, removePieceFromPlay

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
            pieceOnNewPos = getPieceOnCell(pos)
            if (pieceOnNewPos[0] != 0):
                removePieceFromPlay(pieceOnNewPos[1].isWhite, pieceOnNewPos[0])
                movePiece(heldPiece[1].isWhite, heldPiece[0], pos)
            else:
                movePiece(heldPiece[1].isWhite, heldPiece[0], pos)
    holdingPiece = False

def getHoldingPiece():
    global heldPiece
    return heldPiece

def isHoldingPiece():
    global holdingPiece
    return holdingPiece


