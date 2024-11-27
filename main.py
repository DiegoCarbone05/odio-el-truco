import pygame
from pygame.locals import *
import views
import pygame.mixer as mixer

import views.menu
import views.settings

#Inicialize pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720), RESIZABLE)
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Trucaos")

def music():
    music = mixer.Sound("assets/music/aria_math.mp3")
    music.play()

path = "menu"

def set_path(new_path:str):
    global path
    path = new_path

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
       
    button_list = [
        {
            "text":"Jugar",
            "callback":lambda: print("Jugar")
        },
        {
            "text":"Anotaciones",
            "callback":lambda: print("Anotaciones")
        },
        {
            "text":"Ajustes",
            "callback":lambda: set_path("sett"),
        },
        {
            "text":"Salir",
            "callback":lambda: pygame.quit()
        },
    ]
    
    if path == "menu":
        views.menu.init(screen, button_list)
    if path == "sett":
        views.settings.init(screen)


    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
    

pygame.quit()