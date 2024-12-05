import pygame
import components.buttons as btn
from services.utils import *
import routes
import components.text_block as textBlock
import services.storage as storage
    
isLoadedData = False
settings = []
    
def save():
    storage.create_file("data/settings.csv", settings)
def load_settings():
    global settings
    settings = storage.read_file("data/settings.csv")
    
def alternate_silence_music():
    settings[0][1] = not(settings[0][1])
    print(settings)
    if settings[0][1]:
        song_play()
    else:
        song_pause()
        
    save()
    

def draw_basic_ui(screen)-> None:
    info = pygame.display.Info()
    pygame.draw.rect(screen, "#1A1A1A", pygame.Rect(0, 0, info.current_w, info.current_h))
    toolbar = pygame.draw.rect(screen, "#262626", pygame.Rect(0, 0, info.current_w, 72))
    
    btn.flat(screen, lambda:routes.set_path("menu"), (14, 18), 40, "X", BTN_DEFAULT_COLOR)
    
    font_size = 16 
    font = pygame.font.Font("assets/fonts/minecraft_font.ttf", font_size)
    text_color = "white"
    text_surface = font.render("Configuraciones", True, text_color)  # True para suavizar bordes (anti-aliasing)
    screen.blit(text_surface, (80, toolbar.center[1] - text_surface.get_height() / 2))
    
def draw_menu(screen):
    textBlock.create(screen, "Menu", (80, 100))
    btn.flat(screen, lambda:alternate_silence_music(), (80, 150), 300, f"Silenciar Musica: {settings[0][1]}", BTN_DEFAULT_COLOR)
    textBlock.create(screen, "__________________", (80, 200))
    textBlock.create(screen, "Alumno: Diego Carbone", (80, 240))
    textBlock.create(screen, "UTN Facultad Regional de Avellaneda", (80, 280))
    



def init(screen):
    if len(settings) == 0:
        load_settings()
        print(settings)
    
    draw_basic_ui(screen)
    draw_menu(screen)
    
    