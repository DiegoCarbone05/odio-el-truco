import pygame
import components.buttons as button
from services.utils import *

def prompt(screen, buttons:list):
    info = pygame.display.Info()
    
    superficie_transparente = pygame.Surface((info.current_w, info.current_h), pygame.SRCALPHA)
    superficie_transparente.fill((0, 0, 0, 128))  # Dibujar un rectángulo rojo transparente

    # Dibujar la superficie en la pantalla
    screen.blit(superficie_transparente, (0, 0))  # x, y
    
    dialog_w = 439
    dialog_h = 190
    
    figure = pygame.draw.rect(
        screen, 
        "#313131", 
        pygame.Rect(
            (info.current_w / 2) - dialog_w / 2, 
            (info.current_h / 2) - dialog_h / 2, 
            dialog_w, 
            dialog_h
            )
        )
    btn_container = pygame.draw.rect(
        screen, 
        "#2C2C2C", 
        
        pygame.Rect(
            figure.left, 
            figure.centery + 20, 
            dialog_w, 
            dialog_h / 2 - 20
            )
        )
    pygame.draw.rect(
        screen, 
        "#3F3F3F", 
        pygame.Rect(
            figure.topleft[0], 
            figure.topleft[1], 
            439, 
            190,
            ),
            width=5
        )
    
    
    #-----------------Text
    font_size = 30
    font = pygame.font.Font("assets/fonts/minecraft_font.ttf", font_size)
    text_color = "white"
    text_surface = font.render("Truco!", True, text_color)  # True para suavizar bordes (anti-aliasing)
     
    text_x = figure.topleft[0] + 30
    text_y = figure.topleft[1] + 30
    
    screen.blit(text_surface, (text_x, text_y))
    
    
    button.flat(
        screen, 
        buttons[0]["callback"], 
        (
            btn_container.topleft[0] + 22, 
            btn_container.centery - 22
            ), 
        190,
        buttons[0]["text"]
        )
    
    button.flat(
        screen, 
        buttons[1]["callback"],
        (
            btn_container.topleft[0] + 22 + 200 + 5, 
            btn_container.centery - 22
        ), 
        190,
        buttons[1]["text"],
        BTN_RED_COLOR
    )
    