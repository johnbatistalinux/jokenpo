print("---------------escolha o modo de jogo---------------")
print("1.humano vs humano-----",end="")
print("2.humano vs maquina-----",end="")
print("3.maquina vs maquina")


while True:
    escolhamodo=int(input(""))
    print("1.tesoura----2.pedra----3.papel")
    if escolhamodo==1:
        print("jogador 1, faça sua jogada")
        jogador1=int(input(""))
        print("jogador 2, faça sua jogada")
        jogador2=int(input(""))
        
continuar = True
contador = 0

print("1 - Jogador vs maquina")
print("2 - sair")

modo = int(input("escolha: "))

if modo == 1:

    while continuar:
        contador = contador + 1 

        print("1 - pedra") 
        print("2 - papel")
        print("3 - tesoura")

        jogador1 = int(input("Escolha uma opção"))

        maquina = contador % 3 + 1
   

        print ("Maquina escolheu", maquina)

        if jogador1 == maquina:
            print("Empate")

        elif (jogador1 == 1 and maquina == 3) or (jogador1 == 2 and maquina == 1) or (jogador1 == 3 and maquina == 2):
            print("Jogador venceu")

        else:
            print("Maquina venceu")

        print("1 - continuar")
        print("2 - sair")

        escolha = int(input("Escolha: "))

        if escolha == 2:
            break

elif modo == 2:
    print("sair do jogo")




        
        






        

