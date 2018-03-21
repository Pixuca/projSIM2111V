import math
import pygame
import time
import random
from objects import *

pygame.init()
bg = "campo.jpg"
screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load(bg).convert()
end = False

distX, distY = 800 / 9, 600 / 9
distT = (distX + distY)/2
print("A cada %.2f pixels se tem 1 (um) metro." % distT)

if (robo.x > bola.x):
    if (robo.y > bola.y):
        distancia = (robo.x - bola.x) + (robo.y - bola.y)
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
    elif (robo.y < bola.y):
        distancia = (robo.x - bola.x) + (bola.y - robo.y)
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
elif (robo.x < bola.x):
    if(robo.y > bola.y):
        distancia = (bola.x - robo.x) + (robo.y - bola.y)
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
    elif (robo.y < bola.y):
        distancia = (bola.x - robo.x) + (bola.y - robo.y)
        print("Distância = %d" % distancia)
        distanciaT = distancia/distT
        print("Distância (em metros) = %.2fm" % distanciaT)
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    r = pygame.draw.rect(screen, robo.color, pygame.Rect(robo.x, robo.y, 30, 30))
    b = pygame.draw.circle(screen, bola.color, (bola.x, bola.y), bola.thickness)
    l = pygame.draw.line(screen, line.color, (line.xi+15, line.yi+15), (line.xf, line.yf), line.thickness)

    pygame.display.flip()
