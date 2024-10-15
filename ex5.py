#5 - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.

def fibo(num):
    a,b = 0,1
    seq = []
    for _ in range(num):
        seq.append(a)
        a, b = b, a + b  
    print(seq)
num = int(input("digite até que número da sequencia fibonacci deseja consultar: "))
fibo(num)
