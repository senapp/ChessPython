import math
import pygame

def getChar(pos):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return chars[pos]

def getColor(color):
    white = (255, 255, 255, 255)
    grey = (100, 100, 100, 255)
    brown = (90, 45, 0, 255)
    black = (50, 50, 50, 255)
    green = (0, 255, 0, 100)

    if (color == "grey"): return grey
    elif (color == "black"): return black
    elif (color == "white"): return white
    elif (color == "brown"): return brown
    elif (color == "green"): return green
    else: return black

def drawSprite(width, height, surface, texturesurface, size = 10, position = (0,0)):
    textsurface = texturesurface
    txt_width, txt_height = textsurface.get_size()
    textsurface = pygame.transform.scale(textsurface, (int(txt_width / width * size), int(txt_height / height * size)))
    textrect = textsurface.get_rect()
    textrect = textrect.move((position[0] - textrect.w / 2, position[1] - textrect.h / 2))
    surface.blit(textsurface, textrect)

def drawText(width, height, myfont, surface, string, fontSize, position = (0,0),):
    textsurface = myfont.render(string, True, (0, 0, 0))
    txt_width, txt_height = textsurface.get_size()
    fontSize = fontSize * width / 50
    textsurface = pygame.transform.scale(textsurface, (int(txt_width / width * fontSize), int(txt_height / height * fontSize )))
    textrect = textsurface.get_rect()
    textrect = textrect.move((position[0] - textrect.w / 2, position[1] - textrect.h / 2))
    surface.blit(textsurface, textrect)