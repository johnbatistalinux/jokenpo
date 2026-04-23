import random
import getpass
import os



jogador1pontos=0
jogador2pontos=0
maquina1pontos=0
maquina2pontos=0
tesoura=3
pedra=1
papel=2
anci = """      ___    ______    __   ___  _______  _____  ___     _______    ______    
     |"  |  /    " \  |/"| /  ")/"     "|(\"   \|"  \   |   __ "\  /    " \   
     ||  | // ____  \ (: |/   /(: ______)|.\\   \    |  (. |__) :)// ____  \  
     |:  |/  /    ) :)|    __/  \/    |  |: \.   \\  |  |:  ____//  /    ) :) 
  ___|  /(: (____/ // (// _  \  // ___)_ |.  \    \. |  (|  /   (: (____/ //  
 /  :|_/ )\        /  |: | \  \(:      "||    \    \ | /|__/ \   \        /   
(_______/  \"_____/   (__|  \__)\_______) \___|\____\)(_______)   \"_____/    
                                                                              """















continuar=1

while True:

    jogador1=0
    jogador2=0
    os.system('cls')
    os.system('clear')
    print(anci)
    print(" ======= Escolha o Modo de Jogo ======= ")
    print("1.👤 Humano   vs   👤 Humano")
    print("2.👤 Humano   vs   🤖 Maquina")
    print("3.🤖 Maquina  vs   🤖 Maquina")
    print("")
    print("0. Sair")
    print("")
    
    escolhamodo=int(input("Escolha: "))
    
    continuar=1
    
    if escolhamodo==1:
        
        while continuar == 1:
            os.system('cls')
            os.system('clear')
            print("1  -  Pedra    🪨")
            print("2  -  Papel    📜")
            print("3  -  Tesoura  ✂️")
            jogador1 = int(getpass.getpass(prompt="Jogador 1, escolha uma opção: "))
            jogador2 = int(getpass.getpass(prompt="Jogador 2, escolha uma opção: "))
        
            if jogador1 == jogador2:
                
                print("Empate!")
                os.system('cls')
                os.system('clear')
            
            elif jogador1 == tesoura and jogador2 == papel or jogador1==pedra and jogador2==tesoura or jogador1==papel and jogador2==pedra:
                os.system('cls')
                os.system('clear')
                print("jogador 1 venceu")
                jogador1pontos+=1
                
            else:
                os.system('cls')
                os.system('clear'   )
                print("O jogador 2 venceu")
                jogador2pontos+=1

            
            if jogador1==1:
                jogador1="🪨"
            elif jogador1==2:
                jogador1="📜"
            else:
                jogador1="✂️"
            
            if jogador2==1:
                jogador2="🪨"
            elif jogador2==2:
                jogador2="📜"
            else:
                jogador2="✂️"



            print(f'👤 {jogador1} vs {jogador2} 👤')    
            print("======================================================")
            print("🏆 Placar")    
            print(f'👤 jogador 1: [{jogador1pontos}]')
            print(f'👤 jogador 2: [{jogador2pontos}]')
                
            print("======================================================")
            print("1 - Continuar")
            print("0 - Sair")
            print("")
            continuar=int(input("Escolha: "))
            
            if continuar == 0:
                jogador1pontos=0
                jogador2pontos=0
                break
            
    
    elif escolhamodo==2:
        
        while continuar == 1:
            os.system('cls')
            os.system('clear')
            maquina = random.randint(1, 3)
            print("1  -  Pedra    🪨")
            print("2  -  Papel    📜")
            print("3  -  Tesoura  ✂️")


         
            jogador1 =int(input("Escolha uma opção: "))


            if jogador1 == maquina:
                
                print("Empate")
                os.system('cls')
                os.system('clear')

            elif jogador1 == tesoura and maquina == papel or jogador1==pedra and maquina==tesoura or jogador1==papel and maquina==pedra:
                os.system('cls')
                os.system('clear')
                print("👤 Você ganhou, parabéns.")
                jogador1pontos+=1

            else:
                os.system('cls')
                os.system('clear')
                print("🤖 Maquina venceu.")
                maquina1pontos+=1
            

            if maquina==1:
                maquina="🪨"
            elif maquina==2:
                maquina="📜"
            else:
                maquina="✂️"
            
            if jogador1==1:
                jogador1="🪨"
            elif jogador1==2:
                jogador1="📜"
            else:
                jogador1="✂️"

            print(f'👤 {jogador1} vs {maquina} 🤖')

            print("======================================================")
            print("🏆 Placar")   
            print(f'👤 Humano:  [{jogador1pontos}]')
            print(f'🤖 Maquina: [{maquina1pontos}]')
                
            print("======================================================")
            print("1 - Continuar")
            print("0 - Sair")
            print("")

            continuar = int(input("Escolha uma opção: "))

            if continuar == 0:
                jogador1pontos=0
                maquina1pontos=0
                break
                
    elif escolhamodo==3:
    
        while continuar == 1:
            os.system('cls')
            os.system('clear')
            maquina1 = random.randint(1, 3)
            maquina2 = random.randint(1, 3)


            if maquina1 == maquina2:
            
                print ("Empate")
                os.system('cls')
                os.system('clear')
    
            elif (maquina1 == pedra and maquina2 == tesoura) or (maquina1 == papel and maquina2 == pedra) or (maquina1 == tesoura and maquina2 == papel):
                os.system('cls')
                os.system('clear')
                print("🤖 Maquina 1 venceu!")
                maquina1pontos+=1
            else:
                os.system('cls')
                os.system('clear')
                print("🤖 Maquina 2 venceu!")
                maquina2pontos+=1
            
            if maquina1==1:
                maquina1="🪨"
            elif maquina1==2:
                maquina1="📜"
            else:
                maquina1="✂️"
            
            if maquina2==1:
                maquina2="🪨"
            elif maquina2==2:
                maquina2="📜"
            else:
                maquina2="✂️"
            print(f'🤖 {maquina1} vs {maquina2} 🤖')

            print("======================================================")
            print("🏆 Placar")    
            print(f'🤖 Maquina 1: [{maquina1pontos}]')
            print(f'🤖 Maquina 2: [{maquina2pontos}]')
                
            print("======================================================")   
            print("1 - Continuar")
            print("0 - Sair")
            print("")
            continuar = int(input("Escolha: "))

            if continuar == 0:
                maquina1pontos=0
                maquina2pontos=0
                break
    
    elif escolhamodo==0:
        print("Programa encerrado")
        break
    else:
        print("Entrada invalida, digite novamente")

