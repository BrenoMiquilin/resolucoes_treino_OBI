linhas_tabuleiro, colunas_tabuleiro = map(int, input().split())

matriz = [list(input()[:colunas_tabuleiro]) for _ in range(linhas_tabuleiro)]
# for linha in matriz:
#     print("".join(linha))

disparos_feitos = int(input())
local_disparo = set()

for _ in range(disparos_feitos):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if 0 <= x < linhas_tabuleiro and 0 <= y < colunas_tabuleiro:
        local_disparo.add((x, y))
# print(local_disparo)

tiros_certos = 0
locais_visitados = set()

for x, y in local_disparo:
    if (x, y) in locais_visitados:
        continue
    if matriz[x][y] == '#':
        barco = []
        j = y

        while(j >= 0 ):
            if (matriz[x][j] == '#'):
                barco.append((x, j))
                locais_visitados.add((x, j))
                j -= 1
            else:
                break

        j = y + 1
        while(j < colunas_tabuleiro):
            if (matriz[x][j] == '#'):
                barco.append((x, j))
                locais_visitados.add((x, j))
                j += 1
            else:
                break

        if all(pos in local_disparo for pos in barco):
            tiros_certos += 1

print(tiros_certos)