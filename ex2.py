#2 - Desenvolva um programa que mostra a tabuada de um número informado pelo usuário

def tabuada(num):
    contador = 1
    for x in range (10):
        print(num ,"x", contador,"=",(num*contador))
        contador += 1
num = int(input("Digite um número: "))
tabuada(num)

