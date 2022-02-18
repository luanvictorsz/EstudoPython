horario = input("Digite o Horario 0-23: ")

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("Horario deve estar dentro do padrão 0 - 23.")
    else:
        if horario <= 11:
            print("Bom Dia!")
        elif horario <= 17:
            print("Boa Tarde!")
        else:
            print("Boa Noite!")
else:
    print("por favor, digite um Horario entre 0 a 23.")
