import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import routes
import components.buttons as button
import components.dialog as dialog
from services.utils import *

def draw_basic_ui(screen)-> None:
    info = pygame.display.Info()
    pygame.draw.rect(screen, "#1A1A1A", pygame.Rect(0, 0, info.current_w, info.current_h))
    pygame.draw.rect(screen, "#262626", pygame.Rect(0, 0, info.current_w, 72))
    
def draw_control_panel(screen)-> pygame.Rect:
    panel_w = 423
    panel_h = 143
    padding = 20
    info = pygame.display.Info()
    figure = pygame.draw.rect(
        screen, 
        "#313131", 
        pygame.Rect(
            50, 
            (info.current_h - 50 - panel_h), 
            panel_w, 
            panel_h
            )
        )
    pygame.draw.rect(
        screen, 
        "#3F3F3F", 
        pygame.Rect(
            figure.topleft[0], 
            figure.topleft[1], 
            panel_w, 
            panel_h,
            ),
            width=5
        )
    
    button.flat(
        screen, 
        lambda: routes.set_path("menu"),
        (figure.topleft[0] + padding, figure.topleft[1] + padding), 
        180,
        "Truco", 
        BTN_PRIMARY_COLOR,
    )
        
    button.flat(
        screen, 
        lambda: routes.set_path("menu"),
        (
            # Cord de figura X + padding + boton anterior + padding
            figure.topleft[0] + padding + 180 + padding, 
            # Cord de figura Y + padding
            figure.topleft[1] + padding
        ), 
        180,
        "Envido", 
        BTN_SUCCESS_COLOR,
    )
        
    button.flat(
        screen, 
        lambda: dialog.prompt(
            screen, 
            [
                {
                    "text":"Quiero", 
                    "callback":lambda:print("quiero")
                }, 
                {
                    "text":"No Quiero", 
                    "callback":lambda:print("nouiero")
                }, 
            ]
        ),
        (
            # Cord de figura X + padding + boton anterior + padding
            figure.topleft[0] + padding, 
            # Cord de figura Y + padding
            figure.topleft[1] + padding + 40 + padding
        ), 
        180 * 2 + padding,
        "Mazo", 
        BTN_DEFAULT_COLOR,
    )
    

def init(screen):
    
    #----------------------------TOOLBAR
    draw_basic_ui(screen)
    button.flat(
        screen, 
        lambda: routes.set_path("menu"),
        (25, (72 / 2) - 33 / 2), 
        0,
        "Salir", 
        BTN_RED_COLOR,
    )
    
    #----------------------------PANEL
    draw_control_panel(screen)

    
    
    
    