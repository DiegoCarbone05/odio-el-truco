import pygame
import views.menu as menu
import routes

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

color = "#000000"

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Parametros: Ruta y control de pantalla de pygame
    routes.navigate("menu", screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()