#1 - criar uma função que calcule calcule o fatorial de um numero dado pelo usuario 

def fatorial(num):
    resultado = 1
    if num == 0 or num == 1:
        return 1    
    else:
        for x in range (num):
            resultado *= num
            num -= 1
            if num == 0:
                return resultado
num = int(input("Digite um número: "))
fatorial(num)

