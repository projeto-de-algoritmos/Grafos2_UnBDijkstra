import pygame
import math
import grafos

def get_selected_node(mouse_pos, grafo):
    for node, coordinates in grafo.coordenadas.items():
        x, y = coordinates
        x = (x + 1) * 100
        y = (y + 1) * 100
        distance = math.sqrt((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2)
        if distance <= 20:  # Raio do círculo que representa o nó
            return node
    return None


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
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Clear the screen
    screen.fill(WHITE)

    selected_nodes = []
    arestas_menor_caminho = []


    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Botão esquerdo do mouse
                    mouse_pos = pygame.mouse.get_pos()
                    selected_node = get_selected_node(mouse_pos, grafo)
                    if selected_node:
                        if len(selected_nodes) < 2:
                            selected_nodes.append(selected_node)
                            if len(selected_nodes) == 2:
                                # Faça algo com os dois nós selecionados
                                print("Nós selecionados:", selected_nodes)
                                start = selected_nodes[0]
                                fim = selected_nodes[1]
                                print("start:", start)
                                print("fim", fim)
                                distancia, caminho = grafo.dijkstra(start, fim)
                                for i in range(len(caminho) - 1):
                                    origem = caminho[i]
                                    destino = caminho[i + 1]
                                    arestas_menor_caminho.append((origem, destino))

                                print("Menor distância entre", start, "e", fim + ":", distancia)

                        else:
                            selected_nodes = [selected_node]

        # Clear the screen
        screen.fill(WHITE)

        for predio in grafo.adjacencias.keys():
            coordenadas = grafo.coordenadas[predio]
            x, y = coordenadas
            x = (x + 1) * 100
            y = (y + 1) * 100
            node_color = BLACK
            if predio in selected_nodes:
                node_color = RED if len(selected_nodes) == 1 else GREEN
            pygame.draw.circle(screen, node_color, (x, y), 20)
            font = pygame.font.Font(None, 20)
            text = font.render(predio, True, BLACK)
            text_rect = text.get_rect(center=(x, y + 30))  # Ajuste a posição vertical do texto
            screen.blit(text, text_rect)

        for predio, conexoes in grafo.adjacencias.items():
            for destino, peso in conexoes.items():
                coordenadas_origem = grafo.coordenadas[predio]
                coordenadas_destino = grafo.coordenadas[destino]
                x1, y1 = coordenadas_origem
                x2, y2 = coordenadas_destino
                x1 = (x1 + 1) * 100
                y1 = (y1 + 1) * 100
                x2 = (x2 + 1) * 100
                y2 = (y2 + 1) * 100

                if (predio, destino) in arestas_menor_caminho or (destino, predio) in arestas_menor_caminho:
                    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 2)
                else:
                    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)


        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

