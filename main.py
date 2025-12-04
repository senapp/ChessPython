from dataclasses import dataclass
from scripts.AI import setupAI


from typing import Any
import pygame
from pygame.locals import *
from scripts.Utilities import *
from scripts.Board import *
from scripts.PieceManager import *
from scripts.Menu import *
from scripts.PieceMover import *

import asyncio

import yaml

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
    maxFPS: int
    logFPS: bool
    whiteStarts: bool
    blackAndWhiteColor: Any
    xGrid: int
    yGrid: int
    AI: bool

@dataclass(frozen=True)
class AppConfig:
    visual: VisualConfig
    game: GameConfig

def setup():
    appConfig: AppConfig = None

    with open('settings.yml', 'r') as file:
        raw_config = yaml.safe_load(file)
        
        visual = VisualConfig(
            title = raw_config.visual.title,
            font = raw_config.visual.font,
            textSize = raw_config.visual.textSize,
            width = raw_config.visual.width,
            height = raw_config.visual.height,
            menuWidth = raw_config.visual.menuWidth,
            icon = raw_config.visual.icon,
            cellSize = (raw_config.visual.width / raw_config.visual.xGrid),
            size = (raw_config.visual.width + raw_config.visual.menuWidth, raw_config.visual.height)
        )

        game = GameConfig(
            maxFPS = raw_config.game.maxFPS,
            logFPS = raw_config.game.logFPS,
            whiteStarts = raw_config.game.whiteStarts,
            blackAndWhiteColor = raw_config.game.blackAndWhiteColor,
            xGrid = raw_config.game.xGrid,
            yGrid = raw_config.game.yGrid,
            AI = raw_config.game.AI
        )

        appConfig = AppConfig(visual = visual, game = game)

    if appConfig is None:
        raise ValueError("Failed to load configuration.")
    
    asyncio.run(main(appConfig))

async def main(appConfig: AppConfig):
    RUNNING = True

    pygame.init()
    pygame.display.set_icon(pygame.image.load(appConfig.visual.icon))
    pygame.display.set_caption(appConfig.visual.title)
    pygame.font.init()

    myfont = pygame.font.SysFont(appConfig.visual.font, appConfig.visual.fontSize)
    screen = pygame.display.set_mode(appConfig.visual.size)

    FPS = pygame.time.Clock()
    FPS.tick(appConfig.game.maxFPS)

    setupBoard(width, height, xGrid, yGrid, cellSize, blackAndWhiteColor)
    pieceManagerSetup(xGrid,yGrid, whiteStarts)
    if (AI):
        setupAI(False, 0)

    board = drawBoard()
    pieces = drawPieces()
    menu = drawMenu(menuWidth, myfont, fontSize, isWhitesTurn(), getLastMove())

    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                mouseReleased(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetPieces()
                    pieceManagerSetup(xGrid, yGrid, whiteStarts)
                    pieces = drawPieces()

        menu = drawMenu(menuWidth, myfont, fontSize, isWhitesTurn(), getLastMove())
        if (isRedrawRequired()): pieces = drawPieces()

        screen.blit(board, (0,0))
        screen.blit(pieces, (0,0))
        screen.blit(menu, (0,0))

        if (isHoldingPiece()):
            movingPiece = drawMovingPiece(getHoldingPiece()[1], pygame.mouse.get_pos(), blackAndWhiteColor)
            screen.blit(movingPiece,(0,0))

        pygame.display.flip()

        if appConfig.game.logFPS:
            pygame.display.set_caption("FPS: " + str(round(FPS.get_fps(), 0)))
            FPS.tick(appConfig.game.maxFPS)

        await asyncio.sleep(0)

    pygame.quit()
    

if __name__ == "__main__":
    setup()