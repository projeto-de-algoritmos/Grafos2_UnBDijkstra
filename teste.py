from desenho import desenhar_grafo
from grafos import Grafo


grafo = Grafo()

grafo.adicionar_predio("Prédio da Reitoria", (0,1))
grafo.adicionar_predio("Biblioteca Central", (1,0))
grafo.adicionar_predio("ICC", (2,0))
grafo.adicionar_predio("FT", (0,3))
grafo.adicionar_predio("FE", (1,1))
grafo.adicionar_predio("FS", (2,2))
grafo.adicionar_predio("FGA", (3,3))
grafo.adicionar_predio("FGA - S1", (5,3))

grafo.adicionar_conexao("ICC", "FT", 1)
grafo.adicionar_conexao("ICC", "FE", 1)
grafo.adicionar_conexao("Biblioteca Central", "ICC", 1)
grafo.adicionar_conexao("FGA", "ICC", 10)
grafo.adicionar_conexao("FGA", "FGA - S1", 1)
grafo.adicionar_conexao("Prédio da Reitoria", "Biblioteca Central", 1)
grafo.adicionar_conexao("FS", "ICC", 1)
grafo.adicionar_conexao("FS", "Prédio da Reitoria", 2)


predio_origem = "Biblioteca Central"
predio_destino = "FE"

distancia = grafo.dijkstra(predio_origem, predio_destino)

print("Menor distância entre", predio_origem, "e", predio_destino + ":", distancia)

desenhar_grafo(grafo)