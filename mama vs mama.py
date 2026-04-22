import random

while True:

    mama1 = random.randint(1, 3)
    mama2 = random.randint(1, 3)

    print("Maquina 1 escolheu: ", mama1)
    print("Maquina 2 escolheu: ", mama2)

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