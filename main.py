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

#Default values
title = 'Chess Python'
icon = 'images/icon-round.png'
font = 'Arial'
myfont = Any
screen = Any

FPS = pygame.time.Clock()

maxFPS = 30
logFPS = False
menuWidth = 150
width = 400
height = 400
xGrid = 8
yGrid = 8
cellSize = 50
fontSize = 30
whiteStarts = True
blackAndWhiteColor = True
AI = True
#Default values end

def setup():
    global title, icon, font,myfont, maxFPS, logFPS, menuWidth, width, height, xGrid, yGrid, screen, FPS, cellSize, fontSize, whiteStarts, AI, blackAndWhiteColor

    settings = open("settings.config", "r")
    try:
        for setting in settings.readlines():
            if ("title" in setting): title = setting.split(':')[1]
            elif ("font" in setting): font = setting.split(':')[1]
            elif ("textSize" in setting): fontSize = int(setting.split(':')[1])
            elif ("maxFPS" in setting): maxFPS = int(setting.split(':')[1])
            elif ("logFPS" in setting):
                if ("true" in setting.split(':')[1].lower()): logFPS = True
                else: logFPS = False
            elif ("width" in setting): width = int(setting.split(':')[1])
            elif ("height" in setting): height = int(setting.split(':')[1])
            elif ("menuWidth" in setting): menuWidth = int(setting.split(':')[1])
            elif ("whiteStarts" in setting):
                if ("true" in setting.split(':')[1].lower()): whiteStarts = True
                else: whiteStarts = False
            elif ("AI" in setting):
                if ("true" in setting.split(':')[1].lower()): AI = True
                else: AI = False
            elif ("blackAndWhiteColor" in setting):
                if ("true" in setting.split(':')[1].lower()): blackAndWhiteColor = True
                else: blackAndWhiteColor = False
            #elif ("xGrid" in setting): xGrid = int(setting.split(':')[1])
            #elif ("yGrid" in setting): yGrid = int(setting.split(':')[1])
    except: print("settings.config format errors")

    # Pygame setup
    pygame.init()
    img = pygame.image.load(icon)
    pygame.display.set_icon(img)
    pygame.display.set_caption(title)
    pygame.font.init()

    myfont = pygame.font.SysFont(font, 30)
    cellSize = width / xGrid
    size = width + menuWidth, height
    screen = pygame.display.set_mode(size)

    FPS = pygame.time.Clock()
    FPS.tick(maxFPS)

async def main():
    setup()
    RUNNING = True

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
        if (logFPS): updateFPS()
        await asyncio.sleep(0)

    pygame.quit()

def updateFPS():
    pygame.display.set_caption("FPS: " + str(round(FPS.get_fps(), 0)))
    FPS.tick(maxFPS)

asyncio.run(main())