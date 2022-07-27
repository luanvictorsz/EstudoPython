# Nesse exemplo, funciona a soma de apenas numeros trabalhando no codigo.

num1 = input("Digite um número: ")
num2 = input("Digite outro Número: ")

# aqui definimos que nossas variaveis são de valores flutuantes, isso vai ajudar a evitar que letras sejam definidas ao cálculo.
try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
    
#aqui vemos a expressão responsavel por mandar a mensagem de erro, caso uma letra seja adicionada ao cálculo.
except:
    print("ERROR")
