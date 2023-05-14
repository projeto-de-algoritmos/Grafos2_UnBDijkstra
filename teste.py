from desenho import desenhar_grafo
from grafos import Grafo


grafo = Grafo()

grafo.adicionar_predio("Prédio da Reitoria", (0,1))
grafo.adicionar_predio("Biblioteca Central", (1,0))
grafo.adicionar_predio("ICC", (2,0))
grafo.adicionar_predio("FT", (0,3))
grafo.adicionar_predio("FE", (1,1))
grafo.adicionar_predio("FS", (2,2))
grafo.adicionar_predio("FT", (3,3))

grafo.adicionar_conexao("ICC", "FT", 3)
grafo.adicionar_conexao("ICC", "FE", 2)
grafo.adicionar_conexao("Biblioteca Central", "ICC", 1)

predio_origem = "Biblioteca Central"
predio_destino = "FE"

distancia = grafo.dijkstra(predio_origem, predio_destino)

print("Menor distância entre", predio_origem, "e", predio_destino + ":", distancia)

desenhar_grafo(grafo)