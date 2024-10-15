#8 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados.

lista = []
print("Digite 5 números para retornar o maior e o menor")
for x in range(5):
    n = int(input("digite aqui: "))
    lista.append(n)

def tratamento(lista):
    maior = max(lista)
    menor = min(lista)

    print("O maior núumero é", maior)
    print("O menor número é", menor)
tratamento(lista)