import random



jogador1pontos=0
jogador2pontos=0

tesoura=3
pedra=1
papel=2

continuar=1

while True:
    
    print("---------------escolha o modo de jogo---------------")
    print("1.humano vs humano")
    print("2.humano vs maquina")
    print("3.maquina vs maquina")   
    
    escolhamodo=int(input("")) 
    
    continuar=1
    
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
            
            if continuar == 0:
                
                break
            
    
    elif escolhamodo==2:
        
        while continuar == 1:
            
            maquina = random.randint(1, 3)
            print("1 - pedra") 
            print("2 - papel")
            print("3 - tesoura")



            jogador1 = int(input("Escolha uma opção"))

            print (f'Maquina escolheu {maquina}')

            if jogador1 == maquina:
                
                print("Empate")

            elif jogador1 == tesoura and maquina == papel or jogador1==pedra and maquina==tesoura or jogador1==papel and maquina==pedra:
                
                print("Você ganhou, parabéns.")

            else:
                
                print("Maquina venceu, se fodeu.")

            print("1 - continuar")
            print("0 - sair")

            continuar = int(input("Escolha: "))

            if continuar == 0:
                
                break
    
    elif escolhamodo==3:
    
        while continuar == 1:
            
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
            continuar = int(input("Escolha: "))

            if continuar == 0:
            
                break
        
    else:
        print("entrada invalida, digite novamente")






        
        






        

