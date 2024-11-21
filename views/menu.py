import pygame

Surface = pygame.Surface

# Load background
def load_background(screen:Surface):
    info = pygame.display.Info()
    image = pygame.image.load("assets/menu-bg.png")  # Reemplaza con la ruta de tu imagen
    image = pygame.transform.scale(image, (info.current_w, info.current_h))
    screen.blit(image, (0, 0)) 
    
# Load menu logotype
def menu_title(screen:Surface):
    info = pygame.display.Info()
    
    # width and height responsive
    w = info.current_w / 2 
    h = w / 3 - w / 20
    
    image = pygame.image.load("assets/game-title.png")  # Reemplaza con la ruta de tu imagen
    image = pygame.transform.scale(image, (w, h))
    
    #Load center title
    screen.blit(image, ((info.current_w / 2) - w/2, 0)) 


def menu_button_large(screen, positions, text:str):
         
    obj = pygame.draw.rect(screen, "#00000000", pygame.Rect(positions[0], positions[1], positions[2], positions[3]))
    file = pygame.image.load("assets/ui/btn.png")
    texture = pygame.transform.scale(file, (obj.width, obj.height))
    screen.blit(texture, obj.topleft)
    
    
    # PLAY BTN
    info = pygame.display.Info()
    font_size = int((positions[3] / 100) * 37) 
    font = pygame.font.Font("assets/fonts/minecraft_font.ttf", font_size)
    text_color = "white"
    text_surface = font.render(text, True, text_color)  # True para suavizar bordes (anti-aliasing)
    
    text_color = "#00000000"
    text_shadow = font.render(text, True, text_color)  # True para suavizar bordes (anti-aliasing)

    # Calcular la posición del texto para centrarlo
    text_rect_shadow = text_shadow.get_rect(center=((positions[0] + positions[2] // 2) + 2 , positions[1]+((positions[3] / 2) - (font_size / 4)) + 2))
    screen.blit(text_shadow, text_rect_shadow)
    
    
    text_rect = text_surface.get_rect(center=((positions[0] + positions[2] // 2), positions[1]+((positions[3] / 2) - (font_size / 4))))
    screen.blit(text_surface, text_rect)



      
def load_buttons(screen:Surface):
    info = pygame.display.Info()
    wt = (info.current_w / 100) * 30
    ht = (info.current_w / 100) * 3.1
    gap = 18
    x = (info.current_w / 2) - wt / 2
    y = ((info.current_h / 2) - ht / 2) - 100
    
    positions_play_btn = [x, y, wt, ht]
    positions_anotations_btn = [x, y + ht + gap, wt, ht]
    
    menu_button_large(screen, positions_play_btn, "Jugar")
    menu_button_large(screen, positions_anotations_btn, "Anotaciones")
    
    

def init(screen:Surface):
    load_background(screen)
    menu_title(screen)
    load_buttons(screen)
    