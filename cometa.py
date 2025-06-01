ano = int(input())
sobra = (ano - 1986) % 76
proximo = 76 - sobra + ano
print(proximo)