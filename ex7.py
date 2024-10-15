#7 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada

print("Escolha a conversão desejada:\n1: Celsius para Fahrenheit\n2: Fahrenheit para Celsius")
escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} °C é igual a {fahrenheit:.2f} °F.")

elif escolha == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} °F é igual a {celsius:.2f} °C.")

else:
    print("Escolha inválida. Por favor, digite 1 ou 2.")
