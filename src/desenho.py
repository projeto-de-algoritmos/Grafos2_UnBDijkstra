import pygame
import math
import grafos

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WIDTH, HEIGHT = 1300, 1000

def get_selected_node(mouse_pos, grafo):
    for node, coordinates in grafo.coordenadas.items():
        x, y = coordinates
        x = (x + 1) * 100
        y = (y + 1) * 100
        distance = math.sqrt((x - mouse_pos[0]) ** 2 + (y - mouse_pos[1]) ** 2)
        if distance <= 20:
            return node
    return None


def setup_screen():

    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("dijkstra - FGA")
    background_image = pygame.image.load("darcy.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    screen.blit(background_image, (0, 0))

    return screen


def draw_graph(grafo):

    screen = setup_screen()

    selected_nodes = []
    short_path_edges = []
    distance = None

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
                                short_path_edges = []
                                distance = 0
                                start = selected_nodes[0]
                                end = selected_nodes[1]
                                distance, path = grafo.dijkstra(start, end)
                                for i in range(len(path) - 1):
                                    origin = path[i]
                                    aux_distance = path[i + 1]
                                    short_path_edges.append((origin, aux_distance))
                        else:
                            selected_nodes = [selected_node]

        for building in grafo.adjacencias.keys():
                coordinates = grafo.coordenadas[building]
                x, y = coordinates
                x = (x + 1) * 100
                y = (y + 1) * 100
                node_color = BLACK
                if building in selected_nodes:
                    node_color = RED if len(selected_nodes) == 1 else GREEN
                pygame.draw.circle(screen, node_color, (x, y), 5)

        for building, connections in grafo.adjacencias.items():
            for destiny, weight in connections.items():
                origin_coordinates = grafo.coordenadas[building]
                destination_coordinates = grafo.coordenadas[destiny]
                x1, y1 = origin_coordinates
                x2, y2 = destination_coordinates
                x1 = (x1 + 1) * 100
                y1 = (y1 + 1) * 100
                x2 = (x2 + 1) * 100
                y2 = (y2 + 1) * 100

                if (building, destiny) in short_path_edges or (destiny, building) in short_path_edges:
                    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 4)
                else:
                    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
        font = pygame.font.Font('arial.ttf', 20)

        if len(selected_nodes) == 2:
            distance_text = font.render("Distância: " + str(distance), True, BLACK)
            distance_text_rect = distance_text.get_rect(bottomright=(1300, HEIGHT - 20))
            screen.blit(distance_text, distance_text_rect)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

