import pygame
import random

# Configuración inicial de Pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Truco")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)

# Fuentes
FONT = pygame.font.Font(None, 36)

# Configuración del mazo
PALOS = ["Espadas", "Bastos", "Oros", "Copas"]
VALORES = ["4", "5", "6", "7", "10", "11", "12", "1", "2", "3"]
MAZO = [(valor, palo) for palo in PALOS for valor in VALORES]

# Rango de jerarquía de cartas
JERARQUIA = {valor: i for i, valor in enumerate(VALORES)}

# Variables del juego
mano_jugador = []
mano_computadora = []
turno_jugador = True
ganador_ronda = None


def barajar_mazo():
    """Baraja el mazo y reparte las cartas."""
    mazo = MAZO[:]
    random.shuffle(mazo)
    return mazo[:3], mazo[3:6]


def dibujar_mano(mano, y):
    """Dibuja las cartas de una mano en pantalla."""
    x_offset = 150
    for i, (valor, palo) in enumerate(mano):
        carta_texto = FONT.render(f"{valor} de {palo}", True, BLACK)
        screen.blit(carta_texto, (x_offset + i * 200, y))


def evaluar_cartas(carta_jugador, carta_computadora):
    """Evalúa qué carta gana en la ronda."""
    valor_jugador, _ = carta_jugador
    valor_computadora, _ = carta_computadora
    if JERARQUIA[valor_jugador] > JERARQUIA[valor_computadora]:
        return "Jugador"
    elif JERARQUIA[valor_jugador] < JERARQUIA[valor_computadora]:
        return "Computadora"
    else:
        return "Empate"


def main():
    global mano_jugador, mano_computadora, turno_jugador, ganador_ronda

    clock = pygame.time.Clock()
    mano_jugador, mano_computadora = barajar_mazo()

    running = True
    while running:
        screen.fill(GREEN)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and turno_jugador:
                pos = pygame.mouse.get_pos()
                # Verificar si el jugador hace clic en una carta
                for i, (valor, palo) in enumerate(mano_jugador):
                    x_offset = 150 + i * 200
                    if x_offset <= pos[0] <= x_offset + 150 and 450 <= pos[1] <= 500:
                        carta_jugador = mano_jugador.pop(i)
                        carta_computadora = mano_computadora.pop(0)
                        ganador_ronda = evaluar_cartas(carta_jugador, carta_computadora)
                        turno_jugador = False
                        break

        # Dibujar elementos en pantalla
        titulo = FONT.render("Juego de Truco", True, WHITE)
        screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 20))

        # Dibujar manos
        dibujar_mano(mano_jugador, 450)  # Mano del jugador
        dibujar_mano(mano_computadora, 100)  # Mano de la computadora

        # Mostrar el ganador de la ronda
        if ganador_ronda:
            resultado = FONT.render(f"Ganador de la ronda: {ganador_ronda}", True, WHITE)
            screen.blit(resultado, (WIDTH // 2 - resultado.get_width() // 2, HEIGHT // 2))

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
