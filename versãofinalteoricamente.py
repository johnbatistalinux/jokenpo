import random

print("---------------escolha o modo de jogo---------------")
print("1.humano vs humano")
print("2.humano vs maquina")
print("3.maquina vs maquina")

jogador1pontos=0
jogador2pontos=0

tesoura=3
pedra=1
papel=2

continuar=1

while True:
    
    escolhamodo=int(input("")) 
    
    if escolhamodo==1:
        
        while continuar == 1:
            
            print("1 - pedra") 
            print("2 - papel")
            print("3 - tesoura")                               
            jogador1 = int(input("Escolha uma opção: "))
            jogador2 = int(input("Escolha uma opção: ")) 
        
            if jogador1 == jogador2:
                
                print("empate")
            
            elif jogador1 == tesoura and jogador2 == papel or jogador1==pedra and jogador2==tesoura or jogador1==papel and jogador2==pedra:
                
                print("jogador 1 venceu")
                jogador1pontos+=1
                
                print(f'jogador1 {jogador1pontos} vs jogador {jogador2pontos}')
            else:
                
                print("jogador 2 venceu")
                jogador2pontos+=1
                print(f'jogador1 {jogador1pontos} vs jogador {jogador2pontos}')
            
            print("1 - continuar")
            print("0 - sair")
            continuar=int(input("Escolha: "))
            
            if escolha ==0:
                
                break
            
    
    elif escolhamodo==2:
        
        while continuar == 1:
            

            print("1 - pedra") 
            print("2 - papel")
            print("3 - tesoura")

            jogador1 = int(input("Escolha uma opção"))

            print ("Maquina escolheu", maquina)

            if jogador1 == maquina:
                
                print("Empate")

            elif jogador1 == tesoura and jogador2 == papel or jogador1==pedra and jogador2==tesoura or jogador1==papel and jogador2==pedra:
                
                print("Jogador 1 venceu")

            else:
                
                print("Maquina venceu")

            print("1 - continuar")
            print("0 - sair")

            escolha = int(input("Escolha: "))

            if escolhafinal == 2:
                
                break
    else:
    
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
    
        elif (mama1 == pedra and mama2 == tesoura) or (mama1 == papel and mama2 == pedra) or (mama1 == tesoura and mama2 == papel):
        
            print("Maquina 1 venceu!")

        else:
            print("Maquina 2 venceu!")

        print("1 - Continuar")
        print("0 - Sair")

        escolha = int(input("Escolha: "))

        if escolha == 0:
            break
        







        
        






        

