import pygame

#------------------------------------------------------------------------------VARIABLES
btn = pygame.image.load("assets/ui/btn.png") # BTN Texture
btn_selected = pygame.image.load("assets/ui/btn-selected.png") # BTN Texture

#------------------------------------------------------------------------------FUNCTIONS
# Load background
def load_background(screen)-> None:
    info = pygame.display.Info()
    image = pygame.image.load("assets/menu-bg.png")  # Reemplaza con la ruta de tu imagen
    image = pygame.transform.scale(image, (info.current_w, info.current_h))
    try:
        screen.blit(image, (0, 0)) 
    except:
        print("An exception occurred")

# Load menu logotype
def menu_title(screen)-> None:
    info = pygame.display.Info()
    
    # width and height responsive
    w = info.current_w / 2 
    h = w / 3 - w / 20
    
    image = pygame.image.load("assets/game-title.png")  # Reemplaza con la ruta de tu imagen
    image = pygame.transform.scale(image, (w, h))
    
    try:
        screen.blit(image, ((info.current_w / 2) - w/2, 0)) 
    except:
        print("An exception occurred")
    #Load center title

def menu_button_large(screen, positions, text:str, callback)-> None:
    pos = pygame.mouse.get_pos()
    obj = pygame.draw.rect(screen, "#00000000", pygame.Rect(positions[0], positions[1], positions[2], positions[3]))
    texture = pygame.transform.scale(btn, (obj.width, obj.height))
    
    if obj.collidepoint(pos):
        texture = pygame.transform.scale(btn_selected, (obj.width, obj.height))
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            callback()

    screen.blit(texture, obj.topleft)
    
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

def load_buttons(screen, buttons)-> None:
    info = pygame.display.Info()
    wt = (info.current_w / 100) * 30
    ht = (info.current_w / 100) * 3.1
    gap = 18
    x = (info.current_w / 2) - wt / 2
    y = ((info.current_h / 2) - ht / 2) - 100
    
    pos = [x, y, wt, ht]
    isFirstButton = True
    
    for item in buttons:
        if isFirstButton:
            menu_button_large(screen, pos, item["text"], item["callback"])
        else:
            pos = [pos[0], (pos[1] + pos[3] + gap), pos[2], pos[3]]
            menu_button_large(screen, pos, item["text"], item["callback"])
        isFirstButton = False
        
    
    
#------------------------------------------------------------------------------INIT-MODULE
def init(screen, btns)-> None:
    load_background(screen)
    menu_title(screen) 
    load_buttons(screen, btns)
    