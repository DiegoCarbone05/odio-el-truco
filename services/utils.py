import pygame.mixer as mixer

#----------------------------------VARIABLES
BTN_PRIMARY_COLOR = {
    "primary":"#3689AD",
    "in_border":"#4C9EC2",
    "btn_shadow":"#265F78"
}
BTN_RED_COLOR = {
    "primary":"#D93636",
    "in_border":"#DC4646",
    "btn_shadow":"#791D1D"
}
BTN_DEFAULT_COLOR = {
    "primary":"#4B4B4B",
    "in_border":"#565656",
    "btn_shadow":"#252525"
}
BTN_SUCCESS_COLOR = {
    "primary":"#5E9B51",
    "in_border":"#70AE61",
    "btn_shadow":"#3C6035"
}

RED = "#FE3F3F"
GREEN = "#3FFE3F"
BLUE = "#3FFEFE"

mixer.init()
mixer.music.load("assets/music/click.mp3")

def song_play():
    mixer.music.play()
    
def song_pause():
    mixer.music.pause()
    