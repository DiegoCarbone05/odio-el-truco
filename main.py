import pygame
from pygame.locals import *
import routes
import services.utils as utils

# Views imports
import views.menu
import views.settings
import views.game

#Inicialize pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720), RESIZABLE)
overlay = pygame.Surface((1280, 720), SRCALPHA)
pygame.display.set_caption("Trucaos")

clock = pygame.time.Clock()
running = True
dt = 0

utils.song_play()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if routes.path == "menu":
        views.menu.init(screen)
    if routes.path == "play":
        views.game.init(screen)
    if routes.path == "sett":
        views.settings.init(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
pygame.quit()

