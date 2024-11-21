from logging import info
import pygame
from pygame.locals import *
import views.menu as menu
import routes
import services.utils as utils
import pygame.mixer as mixer

#Inicialize pygame
pygame.init()

screen = pygame.display.set_mode((1920, 1080), RESIZABLE | FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Trucaos")

def music():
    music = mixer.Sound("assets/music/aria_math.mp3")
    music.play()

#music()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Parametros: Ruta y control de pantalla de pygame
    routes.navigate("menu", screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
    

pygame.quit()