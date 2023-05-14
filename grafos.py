import heapq
import math


class Grafo:
    def __init__(self):
        self.adjacencias = {}
        self.coordenadas = {}

    def adicionar_predio(self, predio, coordenadas):
        self.adjacencias[predio] = {}
        self.coordenadas[predio] = coordenadas

    def adicionar_conexao(self, predio1, predio2, peso):
        self.adjacencias[predio1][predio2] = peso
        self.adjacencias[predio2][predio1] = peso

    def obter_conexoes(self, predio):
        return self.adjacencias[predio]

    def calcular_distancia_euclidiana(self, predio1, predio2):
        x1, y1 = self.coordenadas[predio1]
        x2, y2 = self.coordenadas[predio2]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def dijkstra(self, predio_origem, predio_destino):
        distancia = {predio: float('inf') for predio in self.adjacencias}
        distancia[predio_origem] = 0
        fila = [(0, predio_origem)]
        while fila:
            dist, predio = heapq.heappop(fila)
            if predio == predio_destino:
                break
            if dist > distancia[predio]:
                continue
            for adjacente, peso in self.adjacencias[predio].items():
                nova_distancia = dist + peso
                if nova_distancia < distancia[adjacente]:
                    distancia[adjacente] = nova_distancia
                    heapq.heappush(fila, (nova_distancia, adjacente))
        return distancia[predio_destino]