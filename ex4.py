#4 - Faça um programa que verifique se um número fornecido é primo
def primo():
    num = int(input("Digite um número: "))

    if num <= 1:
        print(f"{num} não é primo.")
    else:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break

        if primo:
            print(f"{num} é primo.")
        else:
            print(f"{num} não é primo.")
primo()

