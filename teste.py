from grafos import Grafo


grafo = Grafo()

grafo.adicionar_predio("Prédio da Reitoria")
grafo.adicionar_predio("Biblioteca Central")
grafo.adicionar_predio("ICC")
grafo.adicionar_predio("FT")
grafo.adicionar_predio("FE")
grafo.adicionar_predio("FS")
grafo.adicionar_predio("FT")

grafo.adicionar_conexao("ICC", "FT", 3)
grafo.adicionar_conexao("ICC", "FE", 2)
grafo.adicionar_conexao("Biblioteca Central", "ICC", 1)

predio_origem = "Biblioteca Central"
predio_destino = "FE"

distancia = grafo.dijkstra(predio_origem, predio_destino)

print("Menor distância entre", predio_origem, "e", predio_destino + ":", distancia)
