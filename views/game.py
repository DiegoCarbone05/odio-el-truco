import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import routes
import components.buttons as button
import components.dialog as dialog
import components.text_block as textBlock
from services.utils import *
import services.cards as CardService

in_game = True
c1_pos = True
c2_pos = True
c3_pos = True

cb1_pos = False
cb2_pos = False
cb3_pos = False

user_game_movements = [
]

bot_game_movements = [
]


turn = 1

def set_card_1():
    global c1_pos
    global turn
    turn += 1
    c1_pos = False
def set_card_2():
    global c2_pos
    global turn
    turn += 1
    c2_pos = False
def set_card_3():
    global c3_pos
    global turn
    turn += 1
    c3_pos = False

def draw_basic_ui(screen)-> None:
    info = pygame.display.Info()
    pygame.draw.rect(screen, "#1A1A1A", pygame.Rect(0, 0, info.current_w, info.current_h))
    pygame.draw.rect(screen, "#262626", pygame.Rect(0, 0, info.current_w, 72))
    
def draw_control_panel(screen)-> pygame.Rect:
    info = pygame.display.Info()
    panel_w = 423
    panel_h = 143
    padding = 20
    
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
    
    #----------------------PANEL-BUTTONS
    
    button.flat(
        screen, 
        lambda: print("no"),
        (figure.topleft[0] + padding, figure.topleft[1] + padding), 
        180,
        "Truco", 
        BTN_PRIMARY_COLOR,
    )
        
    button.flat(
        screen, 
        lambda: print("no"),
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
        lambda: print("no"),

        (
            # Cord de figura X + padding + boton anterior + padding
            figure.topleft[0] + padding, 
            # Cord de figura Y + padding
            figure.topleft[1] + padding + 40 + padding
        ), 
        180 * 2 + padding,
        "Mazo", 
        BTN_RED_COLOR,
    )
    
                
isCardClicked = False
def draw_card(screen, cords:tuple, card:dict, action:any):

    w = 120
    h = 200
    
    card_obj = pygame.draw.rect(
        screen, 
        "#FFFFFF00", 
        pygame.Rect(
            cords[0],
            (cords[1]),
            w, 
            h
            )
        )
        
    shadow_file = pygame.image.load("assets/ui/shadow.png") # BTN Texture
    shadow_texture = pygame.transform.scale(shadow_file, (card_obj.width + 40, card_obj.height + 40))
    screen.blit(shadow_texture, (card_obj.topleft[0] - 20, card_obj.topleft[1] - 20))
    
    file = pygame.image.load(card["src"]) # BTN Texture
    texture = pygame.transform.scale(file, (card_obj.width, card_obj.height))
    screen.blit(texture, card_obj.topleft)
    
    global isCardClicked
    pos = pygame.mouse.get_pos()
    if card_obj.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if isCardClicked == False:
            if mouse_buttons[0]:
                action()
                user_game_movements.append(card)
                print(card)
                isCardClicked = True
        else:
            if mouse_buttons[0] == False:
                isCardClicked = False
                
    return card_obj
    
def click(el, callback):
    global isCardClicked
    pos = pygame.mouse.get_pos()
    if el.collidepoint(pos):
        mouse_buttons = pygame.mouse.get_pressed()
        if isCardClicked == False:
            if mouse_buttons[0]:
                
                callback()
                isCardClicked = True
        else:
            if mouse_buttons[0] == False:
                isCardClicked = False

def draw_mallet(screen, new_cards):
    info = pygame.display.Info()
    if len(new_cards) == 3:
        
        global c1_pos
        global c2_pos
        global c3_pos
        
        global cb1_pos
        global cb2_pos
        global cb3_pos
        
        global user_game_movements
        global bot_game_movements
        global turn 
 
        if len(user_game_movements) == 1 and turn == 2:
            bot_game_movements.append(CardService.current_bot_mallet[0])
            turn += 1
            print(bot_game_movements)
        if len(user_game_movements) == 2 and turn == 4:
            bot_game_movements.append(CardService.current_bot_mallet[2])
            turn += 1
            print(bot_game_movements)
        if len(user_game_movements) == 3 and turn == 6:
            bot_game_movements.append(CardService.current_bot_mallet[1])
            turn += 1
            print(bot_game_movements)

        
        if c1_pos: draw_card(screen, (75, info.current_h - 120 - 240), new_cards[0], lambda: set_card_1())
        if c2_pos: draw_card(screen, (75 + 130, info.current_h - 120 - 240), new_cards[1], lambda: set_card_2())
        if c3_pos: draw_card(screen, (225 + 110, info.current_h - 120 - 240), new_cards[2], lambda: set_card_3())
        
        user_start_pos = (600, 400)
        bot_start_pos = (600, 150)
        index = 0
        
        
        for card_xd in user_game_movements:
            draw_card(screen, (user_start_pos[0] + 200 * index, user_start_pos[1]), card_xd, lambda: print("xd"))
            draw_card(screen, (bot_start_pos[0] + 200 * index, bot_start_pos[1]), CardService.current_bot_mallet[index], lambda: print("xd"))
            
            if card_xd["valor"] > CardService.current_bot_mallet[index]["valor"]:
                textBlock.create(screen, "Ganaste! :D", (user_start_pos[0] + 200 * index, 630), 16, GREEN)
            elif card_xd["valor"] == CardService.current_bot_mallet[index]["valor"]:
                textBlock.create(screen, "Empate! ;-;", (user_start_pos[0] + 200 * index, 630), 16, BLUE)
            else:
                textBlock.create(screen, "Perdiste! :C", (user_start_pos[0] + 200 * index, 630), 16, RED)
            index += 1 
            
        

def init(screen):
    
    global in_game
    
    if in_game:
        CardService.current_user_mallet = CardService.get_random_random()
        CardService.current_bot_mallet = CardService.get_random_random()
        
        in_game = False
    
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
    draw_mallet(screen, CardService.current_user_mallet)
    draw_control_panel(screen)
    # draw_table_cards(screen)