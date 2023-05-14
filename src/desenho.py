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

    screen.fill(WHITE)

    return screen


def draw_graph(grafo, selected_nodes, screen, short_path_edges, distance):
    for building in grafo.adjacencias.keys():
            coordinates = grafo.coordenadas[building]
            x, y = coordinates
            x = (x + 1) * 100
            y = (y + 1) * 100
            node_color = BLACK
            if building in selected_nodes:
                node_color = RED if len(selected_nodes) == 1 else GREEN
            pygame.draw.circle(screen, node_color, (x, y), 10)
            font = pygame.font.Font(None, 20)
            text = font.render(building, True, BLACK)
            text_rect = text.get_rect(center=(x, y + 30))
            screen.blit(text, text_rect)

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
    if len(selected_nodes) > 0:
        start_node = selected_nodes[0]
        start_coordinates = grafo.coordenadas[start_node]
        start_x, start_y = start_coordinates
        start_x = (start_x + 1) * 100
        start_y = (start_y + 1) * 100
        start_text = font.render("Start: " + start_node, True, BLACK)
        start_text_rect = start_text.get_rect(bottomright=(700, HEIGHT - 60))
        screen.blit(start_text, start_text_rect)

    if len(selected_nodes) > 1:
        end_node = selected_nodes[1]
        end_coordinates = grafo.coordenadas[end_node]
        end_x, end_y = end_coordinates
        end_x = (end_x + 1) * 100
        end_y = (end_y + 1) * 100
        end_text = font.render("End: " + end_node, True, BLACK)
        end_text_rect = end_text.get_rect(bottomright=(700, HEIGHT - 40))
        screen.blit(end_text, end_text_rect)

    if len(selected_nodes) == 2:
        distance_text = font.render("Distância: " + str(distance), True, BLACK)
        distance_text_rect = distance_text.get_rect(bottomright=(700, HEIGHT - 20))
        screen.blit(distance_text, distance_text_rect)


def graph_ainda_preciso(grafo):

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
                                start = selected_nodes[0]
                                end = selected_nodes[1]
                                distance, path = grafo.dijkstra(start, end)
                                for i in range(len(path) - 1):
                                    origin = path[i]
                                    aux_distance = path[i + 1]
                                    short_path_edges.append((origin, aux_distance))
                        else:
                            selected_nodes = [selected_node]
        screen.fill(WHITE)

        draw_graph(grafo, selected_nodes, screen, short_path_edges, distance)

        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

