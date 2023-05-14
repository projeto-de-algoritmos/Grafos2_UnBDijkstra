import pygame
import math

def desenhar_grafo(grafo):
    # Initialize Pygame
    pygame.init()

    # Set the width and height of the window
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Graph Drawing")

    # Set colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Clear the screen
    screen.fill(WHITE)

    for predio in grafo.adjacencias.keys():
        coordenadas = grafo.coordenadas[predio]
        x, y = coordenadas
        x = (x + 1) * 100
        y = (y + 1) * 100
        pygame.draw.circle(screen, BLACK, (x, y), 20)
        font = pygame.font.Font(None, 20)
        text = font.render(predio, True, BLACK)
        text_rect = text.get_rect(center=(x, y + 30))  # Ajuste a posição vertical do texto
        screen.blit(text, text_rect)

    for predio, conexoes in grafo.adjacencias.items():
        for destino in conexoes.keys():
            coordenadas_origem = grafo.coordenadas[predio]
            coordenadas_destino = grafo.coordenadas[destino]
            x1, y1 = coordenadas_origem
            x2, y2 = coordenadas_destino
            x1 = (x1 + 1) * 100
            y1 = (y1 + 1) * 100
            x2 = (x2 + 1) * 100
            y2 = (y2 + 1) * 100
            pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
