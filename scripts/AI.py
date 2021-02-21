from scripts.Piece import piece
import random

steps = 0
isWhite = False
AIon = False

def IS_AI():
    global AIon
    return AIon

def setupAI(aiIsWhite, stepsAhead):
    global steps, isWhite, AIon
    steps = stepsAhead
    isWhite = aiIsWhite
    AIon = True

def calculateMove(whitePieceArray, blackPieceArray):
    global isWhite, steps
    movingArray = []
    defendingArray = []
    if (isWhite): 
        movingArray = whitePieceArray
        defendingArray = blackPieceArray
    else: 
        movingArray = blackPieceArray
        defendingArray: whitePieceArray
    
    selectedPiece = piece(0,0,isWhite)
    pieceIndex = 0
    move = 0
    if (steps == 0):
        while len(selectedPiece.posLocations) == 0:
            pieceIndex = random.randrange(len(movingArray))
            selectedPiece = movingArray[pieceIndex]
        move = random.randrange(len(selectedPiece.posLocations))
    pos = selectedPiece.posLocations[move]
    return pos, pieceIndex, selectedPiece, False