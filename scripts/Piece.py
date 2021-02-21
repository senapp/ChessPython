from scripts.Utilities import *

class piece(): 
    def __init__(self, position, pieceType, isWhite): 
        self.isWhite = isWhite
        self.position = position
        self.pieceType = pieceType
        self.movesMade = 0
        self.posLocations = []
        self.alive = True

    def getValue(self):
        valMod = 1
        if (not self.isWhite): valMod = -1
        if (self.pieceType == 0): return valMod * 1
        elif (self.pieceType == 1): return valMod * 5
        elif (self.pieceType == 2): return valMod * 3
        elif (self.pieceType == 3): return valMod * 3.5
        elif (self.pieceType == 4): return valMod * 9
        elif (self.pieceType == 5): return valMod * math.pow(10,10)

    def getPieceName(self):
        type = self.pieceType
        if (type == 1): return "Rook"
        elif (type == 2): return "Knight"
        elif (type == 3): return "Bishop"
        elif (type == 4): return "Queen"
        elif (type == 5): return "King"
        else: return "Pawn"

class pieceSprite():
    def __init__(self, color):
        if (color == "black"):
            self.pawn = pygame.image.load("images/Chess_pdt60.png").convert_alpha()
            self.rook = pygame.image.load("images/Chess_rdt60.png").convert_alpha()
            self.knight = pygame.image.load("images/Chess_ndt60.png").convert_alpha()
            self.bishop = pygame.image.load("images/Chess_bdt60.png").convert_alpha()
            self.queen = pygame.image.load("images/Chess_qdt60.png").convert_alpha()
            self.king = pygame.image.load("images/Chess_kdt60.png").convert_alpha()
        else:
            self.pawn = pygame.image.load("images/Chess_plt60.png").convert_alpha()
            self.rook = pygame.image.load("images/Chess_rlt60.png").convert_alpha()
            self.knight = pygame.image.load("images/Chess_nlt60.png").convert_alpha()
            self.bishop = pygame.image.load("images/Chess_blt60.png").convert_alpha()
            self.queen = pygame.image.load("images/Chess_qlt60.png").convert_alpha()
            self.king = pygame.image.load("images/Chess_klt60.png").convert_alpha()

    def getPiece(self, piece):
        if piece == 1: return self.rook
        elif piece == 2: return self.knight
        elif piece == 3: return self.bishop
        elif piece == 4: return self.queen
        elif piece == 5: return self.king
        else: return self.pawn
