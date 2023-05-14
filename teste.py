from grafos import Grafo


grafo = Grafo()

# Adicionando os prédios
grafo.adicionar_predio("Prédio da Reitoria")
grafo.adicionar_predio("Biblioteca Central")
grafo.adicionar_predio("ICC")
grafo.adicionar_predio("FT")
grafo.adicionar_predio("FE")
grafo.adicionar_predio("FS")
grafo.adicionar_predio("FT")

# Adicionando as conexões com peso
grafo.adicionar_conexao("ICC", "FT", 3)
grafo.adicionar_conexao("ICC", "FE", 2)
grafo.adicionar_conexao("Biblioteca Central", "ICC", 1)

# Executando o algoritmo de Dijkstra a partir do prédio inicial
# Definindo o prédio de origem e o prédio de destino
predio_origem = "Biblioteca Central"
predio_destino = "FE"

# Executando o algoritmo de Dijkstra para encontrar a menor distância entre os prédios
distancia = grafo.dijkstra(predio_origem, predio_destino)

# Imprimindo as distâncias mínimas a partir do prédio inicial
print("Menor distância entre", predio_origem, "e", predio_destino + ":", distancia)
