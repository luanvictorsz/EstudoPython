usuario = input("Digite o Usuario: ")
qtd_caracteres = len(usuario)

print("a quantidade de caracteres é de ", qtd_caracteres, "Digitados")

if qtd_caracteres < 6:
    print("Digite no minimo 6 caracteres.")
else:
    print("Você foi cadastrado com sucesso.")
