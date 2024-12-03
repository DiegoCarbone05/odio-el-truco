import pygame
import services.utils as utils

def flat(screen, callback, cords:tuple=(0, 0), btn_width:int=0, text:str="Button", style=utils.BTN_PRIMARY_COLOR):
    #------------------Text
    font_size = 16 
    font = pygame.font.Font("assets/fonts/minecraft_font.ttf", font_size)
    text_color = "white"
    text_surface = font.render(text, True, text_color)  # True para suavizar bordes (anti-aliasing)
    
    # Get text width and padding button added
    relative_btn_width = text_surface.get_width() + 100
    if btn_width > 0:
        relative_btn_width = btn_width
    
    # Fill
    btn = pygame.draw.rect(screen, style["primary"], pygame.Rect(cords[0], cords[1], relative_btn_width, 40))
    # Stroke
    pygame.draw.rect(screen, style["in_border"], pygame.Rect(cords[0], cords[1], relative_btn_width, 40), width=2)
    # Shadow
    pygame.draw.rect(screen, style["btn_shadow"], pygame.Rect(btn.bottomleft[0], btn.bottomleft[1], relative_btn_width, 4), width=2)
    screen.blit(text_surface, (btn.center[0] - text_surface.get_width() / 2, btn.center[1] - text_surface.get_height() / 2))
    
    pos = pygame.mouse.get_pos()
    if btn.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            callback()