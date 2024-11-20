import views.menu as menu

def navigate(path:str, screen):
    match path:
        case "menu":
            menu.init(screen)
