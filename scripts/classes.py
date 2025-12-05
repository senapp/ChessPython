from dataclasses import dataclass
from typing import Any
import math

@dataclass(frozen=True)
class VisualConfig:
    title: str
    font: str
    textSize: int
    width: int
    height: int
    menuWidth: int
    icon: str
    cellSize: int
    size: {int, int}

@dataclass(frozen=True)
class GameConfig:
    whiteStarts: bool
    blackAndWhiteColor: Any
    xGrid: int
    yGrid: int
    AI: bool

@dataclass(frozen=True)
class AppConfig:
    visual: VisualConfig
    game: GameConfig

class Piece():
    isWhite: bool
    position: tuple[int, int]
    pieceType: int
    movesMade: int
    posLocations: list[tuple[int, int]]
    alive: bool

    def __init__(self, position, pieceType, isWhite):
        self.isWhite = isWhite
        self.position = position
        self.pieceType = pieceType
        self.movesMade = 0
        self.posLocations = []
        self.alive = True

    def getValue(self):
        valMod = 1
        type = self.pieceType
        if (not self.isWhite): valMod = -1
        if (type == 0): return valMod * 1
        elif (type == 1): return valMod * 5
        elif (type == 2): return valMod * 3
        elif (type == 3): return valMod * 3.5
        elif (type == 4): return valMod * 9
        elif (type == 5): return valMod * math.pow(10,10)

    def getPieceName(self):
        type = self.pieceType
        if (type == 1): return "Rook"
        elif (type == 2): return "Knight"
        elif (type == 3): return "Bishop"
        elif (type == 4): return "Queen"
        elif (type == 5): return "King"
        else: return "Pawn"

    def getChessNotationPosition(self):
        x = self.position[0]
        y = self.position[1]
        if (x < 0 or y < 0): return None
        x = chr(ord('a') + x)
        y = str(y + 1)
        return f"{x}{y}"

    def getSprite(self):
        type = self.pieceType
        isWhite = self.isWhite
        if isWhite:
            if type == 1: return "Chess_rlt60.png"
            elif type == 2: return "Chess_nlt60.png"
            elif type == 3: return "Chess_blt60.png"
            elif type == 4: return "Chess_qlt60.png"
            elif type == 5: return "Chess_klt60.png"
            else: return "Chess_plt60.png"
        else:
            if type == 1: return "Chess_rdt60.png"
            elif type == 2: return "Chess_ndt60.png"
            elif type == 3: return "Chess_bdt60.png"
            elif type == 4: return "Chess_qdt60.png"
            elif type == 5: return "Chess_kdt60.png"
            else: return "Chess_pdt60.png"

class Board():
    pieces: list

    def __init__(self, appConfig: AppConfig):
        self.pieces =  [[None]* appConfig.game.xGrid for _ in range(appConfig.game.yGrid)]
        for y in range(appConfig.game.yGrid):
            for x in range(appConfig.game.xGrid):
                isWhite = True if y < appConfig.game.yGrid / 2 else False
                pieceType = -1

                if y == 1 or y == appConfig.game.yGrid - 2: pieceType = 0
                elif (y == 0 or y == appConfig.game.yGrid - 1) and (x == 0 or x == appConfig.game.xGrid - 1): pieceType = 1
                elif (y == 0 or y == appConfig.game.yGrid - 1) and (x == 1 or x == appConfig.game.xGrid - 2): pieceType = 2
                elif (y == 0 or y == appConfig.game.yGrid - 1) and (x == 2 or x == appConfig.game.xGrid - 3): pieceType = 3
                elif (y == 0 or y == appConfig.game.yGrid - 1) and (x == 3): pieceType = 4
                elif (y == 0 or y == appConfig.game.yGrid - 1) and (x == 4): pieceType = 5

                if (pieceType != -1):
                    self.pieces[x][y] = Piece([x, y], pieceType, isWhite)
