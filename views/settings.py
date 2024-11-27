import pygame

def init(screen):
    info = pygame.display.Info()
    pygame.draw.rect(screen, "black", pygame.Rect(0, 0, info.current_w, info.current_h))
    