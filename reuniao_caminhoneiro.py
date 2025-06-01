import heapq

grafo = {}
cidades = []

numero_cidades, numero_estradas = map(int, input().split())

for ind in range(numero_cidades):
    cidades.append(ind)
    grafo[ind] = {}

for i in range(numero_estradas):
    cidade1, cidade2, distancia_entre_cidades = map(int, input().split())
    grafo[cidade1][cidade2] = distancia_entre_cidades
    grafo[cidade2][cidade1] = distancia_entre_cidades

menor_maior_distancia = float('inf')

for ponto_partida_cidade in grafo:
    distancia = {cidade: float('inf') for cidade in grafo}
    distancia[ponto_partida_cidade] = 0
    fila = [(0, ponto_partida_cidade)]

    while fila:
        atual_distancia, cidade_teste_atual = heapq.heappop(fila)

        for cidade_vizinha, tamanho_trajeto in grafo[cidade_teste_atual].items():
            distancia_atualizada = atual_distancia + tamanho_trajeto
            
            if distancia_atualizada < distancia[cidade_vizinha]:
                distancia[cidade_vizinha] = distancia_atualizada
                heapq.heappush(fila, (distancia_atualizada, cidade_vizinha))

    maior_distancia = max(distancia.values())

    if maior_distancia < menor_maior_distancia:
        menor_maior_distancia = maior_distancia

print(f"{menor_maior_distancia}")