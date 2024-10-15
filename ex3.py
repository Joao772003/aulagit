#Escreva um função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente)

def palindromo(frase):
    frase = frase.lower()
    frase_invert = frase[::-1].replace(" ","").lower()
    if frase == frase_invert:
        return print("É um paindromo")
    else:
        print("Não é um palindromo")
frase = input("Digite uma palavra ou frase: ")
palindromo(frase)
