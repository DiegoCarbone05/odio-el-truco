import random

current_user_mallet = [
    # {"nombre": "1 de espada", "valor": 14, "src": "assets/cartas/1 de espada.jpg"},
    # {"nombre": "7 de espada", "valor": 12, "src": "assets/cartas/7 de espada.jpg"},
    # {"nombre": "3 de copa", "valor": 10, "src": "assets/cartas/3 de copa.jpg"},
]
current_bot_mallet = [
    # {"nombre": "7 de oro", "valor": 11, "src": "assets/cartas/7 de oro.jpg"},
    # {"nombre": "3 de oro", "valor": 10, "src": "assets/cartas/3 de oro.jpg"},
    # {"nombre": "2 de copa", "valor": 9, "src": "assets/cartas/2 de copa.jpg"},
]

turn = 1



cartas_truco = [
    {"nombre": "1 de espada", "valor": 14, "src": "assets/cartas/1 de espada.jpg"},
    
    {"nombre": "1 de basto", "valor": 13, "src": "assets/cartas/1 de basto.jpg"},
    
    {"nombre": "7 de espada", "valor": 12, "src": "assets/cartas/7 de espada.jpg"},
    {"nombre": "7 de oro", "valor": 11, "src": "assets/cartas/7 de oro.jpg"},
    
    {"nombre": "3 de espada", "valor": 10, "src": "assets/cartas/3 de espada.jpg"},
    {"nombre": "3 de basto", "valor": 10, "src": "assets/cartas/3 de basto.jpg"},
    {"nombre": "3 de oro", "valor": 10, "src": "assets/cartas/3 de oro.jpg"},
    {"nombre": "3 de copa", "valor": 10, "src": "assets/cartas/3 de copa.jpg"},
    
    {"nombre": "2 de espada", "valor": 9, "src": "assets/cartas/2 de espada.jpg"},
    {"nombre": "2 de basto", "valor": 9, "src": "assets/cartas/2 de basto.jpg"},
    {"nombre": "2 de copa", "valor": 9, "src": "assets/cartas/2 de copa.jpg"},
    {"nombre": "2 de oro", "valor": 9, "src": "assets/cartas/2 de oro.jpg"},
    
    {"nombre": "1 de copa", "valor": 8, "src": "assets/cartas/1 de copa.jpg"},
    {"nombre": "1 de oro", "valor": 8, "src": "assets/cartas/1 de oro.jpg"},
    
    # {"nombre": "12 de copa", "valor": 7, "src": "assets/cartas/12 de copa.jpg"},
    # {"nombre": "12 de espada", "valor": 7, "src": "assets/cartas/12 de espada.jpg"},
    # {"nombre": "12 de basto", "valor": 7, "src": "assets/cartas/12 de basto.jpg"},
    # {"nombre": "12 de oro", "valor": 7, "src": "assets/cartas/12 de oro.jpg"},
    
    # {"nombre": "11 de copa", "valor": 6, "src": "assets/cartas/11 de copa.jpg"},
    # {"nombre": "11 de espada", "valor": 6, "src": "assets/cartas/11 de espada.jpg"},
    # {"nombre": "11 de basto", "valor": 6, "src": "assets/cartas/11 de basto.jpg"},
    # {"nombre": "11 de oro", "valor": 6, "src": "assets/cartas/11 de oro.jpg"},
    
    {"nombre": "10 de copa", "valor": 5, "src": "assets/cartas/10 de copa.jpg"},
    {"nombre": "10 de espada", "valor": 5, "src": "assets/cartas/10 de espada.jpg"},
    {"nombre": "10 de basto", "valor": 5, "src": "assets/cartas/10 de basto.jpg"},
    {"nombre": "10 de oro", "valor": 5, "src": "assets/cartas/10 de oro.jpg"},
    
    {"nombre": "7 de copa", "valor": 4, "src": "assets/cartas/7 de copa.jpg"},
    {"nombre": "7 de basto", "valor": 4, "src": "assets/cartas/7 de basto.jpg"},
    
    {"nombre": "6 de espada", "valor": 3, "src": "assets/cartas/6 de espada.jpg"},
    {"nombre": "6 de basto", "valor": 3, "src": "assets/cartas/6 de basto.jpg"},
    {"nombre": "6 de copa", "valor": 3, "src": "assets/cartas/6 de copa.jpg"},
    {"nombre": "6 de oro", "valor": 3, "src": "assets/cartas/6 de oro.jpg"},
    
    {"nombre": "5 de espada", "valor": 2, "src": "assets/cartas/5 de espada.jpg"},
    {"nombre": "5 de basto", "valor": 2, "src": "assets/cartas/5 de basto.jpg"},
    {"nombre": "5 de copa", "valor": 2, "src": "assets/cartas/5 de copa.jpg"},
    {"nombre": "5 de oro", "valor": 2, "src": "assets/cartas/5 de oro.jpg"},
    
    {"nombre": "4 de espada", "valor": 1, "src": "assets/cartas/4 de espada.jpg"},
    {"nombre": "4 de basto", "valor": 1, "src": "assets/cartas/4 de basto.jpg"},
    {"nombre": "4 de copa", "valor": 1, "src": "assets/cartas/4 de copa.jpg"},
    {"nombre": "4 de oro", "valor": 1, "src": "assets/cartas/4 de oro.jpg"},
]

#------------------------------------------ENVIDO
def envido(isUserSender:bool=True):
    load_event(isUserSender, {"event":"envido"})


def r_envido(isUserSender:bool=True):
    load_event(isUserSender, {"event":"r-envido"})

        
def f_envido(isUserSender:bool=True):
    load_event(isUserSender, {"event":"f-envido"})


def truco(isUserSender:bool=True):
    load_event(isUserSender, {"event":"truco"})


def retruco(isUserSender:bool=True):
    load_event(isUserSender, {"event":"r-envido"})


def vale_4(isUserSender:bool=True):
    load_event(isUserSender, {"event":"v4"})

        
def load_card(card, isUserSender:bool=True):
    load_event(isUserSender, {"event":"card_send", "card":card})

        
def load_event(isUserSender, event:dict):
    print(event)
    if isUserSender:
        user_game_movements.append(event)
    else:
        bot_game_movements.append(event)
    print(user_game_movements)
        

def get_random_random():
    
    cards_in_game = []
    loaded_cards = cartas_truco
    
    for card in range(3):  
        try:
            index_random = random.randrange(0, len(loaded_cards))
            selected_card = loaded_cards[index_random]
            cards_in_game.append(selected_card)
            # loaded_cards.pop(index_random)
        except:
            print(len(loaded_cards))
        
    return cards_in_game

