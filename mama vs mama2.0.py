import random
while True:

    mama1 = random.randint(1, 3)
    mama2 = random.randint(1, 3)

    if mama1 == 1:
        print("Maquina 1 escolheu Pedra")
    elif mama1 == 2:
        print("Maquina 1 escolheu Papel")
    else:
        print("Maquina 1 escolheu Tesoura")

    if mama2 == 1:
        print("Maquina 2 escolheu Pedra")
    elif mama2 == 2:
        print("Maquina 2 escolheu Papel")
    else:
        print("Maquina 2 escolheu Tesoura")

    if mama1 == mama2:
        print ("Empate")
    
    elif (mama1 == 1 and mama2 == 3) or (mama1 == 2 and mama2 == 1) or (mama1 == 3 and mama2 == 2):
        print("Maquina 1 venceu!")

    else:
        print("Maquina 2 venceu!")

    print("1 - Continuar")
    print("2 - Sair")

    escolha = int(input("Escolha: "))

    if escolha == 2:
            break