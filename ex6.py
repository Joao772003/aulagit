#6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort)

lista = [64, 34, 25, 12, 22, 11, 90]
n = len(lista)

for i in range(n):
    trocou = False
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            trocou = True
    if not trocou:
        break

print(lista) 
