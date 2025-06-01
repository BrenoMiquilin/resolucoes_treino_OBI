leituras_realizadas, capacidade_maxima = map(int, input().split())

quantidade = 0
var = 'N'
for andares in range(leituras_realizadas):
    sairam, entraram = map(int, input().split())

    quantidade = (quantidade - sairam) + entraram

    if (quantidade > capacidade_maxima):
        var = 'S'
        break
print(f"{var}")