num1 = input("Digite o primeiro valor: ")
num2 = input("Digite o segundo valor: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print("Há letras ou Caracteres presentes")
