#entrada de dados
hp1=999
hp2=999
valida = 1

    
while valida == 1:
    #monstro1
    nome1=input("Nome do Monstro:")
    hp1=int(input("Valor do hp:"))
    atk1=int(input("Valor do atk:"))

    #monstro2
    nome2=input("Nome do Monstro:")
    hp2=int(input("Valor do hp:"))
    atk2=int(input("Valor do atk:"))
    
    #pede pro usuário escrever numero acima de 0 pra atk e hp
    if hp1 <= 0 or hp2 <= 0 or atk1 <= 0 or atk2 <= 0:
        print("ESCREVE DIREITO, VALOR POSITIVO MANO")
    else:
        #LUTA =========== BATALHA ============= DUELO
        while hp1>0 and hp2>0:
            print("Que comece o duelo!")
            print(ataque())
            if ataque() == 0:
                print("Final do duelo")
            else:
                print(contraataque())
                if contraataque() == 0:
                    print("Final do duelo")


#FUNÇÕES

def ataque():
    hp = hp2 - atk1
    
    if hp <= 0:
        print(f"O", nome2,"desmaiou!\n",nome1,"é o vencedor!")       
        return(0)
    else:
        print(f"O",nome1,"atacou",nome2,"deixando ele com",hp,"de vida!")
        print("A batalha continua!") 
        return(hp) 
        
    
    
def contraataque():
    hp = hp1 - atk2
    
    if hp <= 0:
        print(f"O", nome1,"desmaiou!\n",nome2,"é o vencedor!")       
        return(0)
    else:
        print(f"O",nome2,"atacou",nome1,"deixando ele com",hp,"de vida!")
        print("A batalha continua!") 
        return(hp) 
    
    
    
    
    
    
    
    
'''
def batalha():
    novohp2 = hp2 - atk1
    novohp1 = hp1 - atk2
    
    
    #verificação de vitória
    if novohp1 <= 0 and novohp2 <=0:
        print("Ambos desmaiaram! Tivemos um empate!")
        novohp1 == novohp2 == 0
        return()
    elif novohp1 <= 0:
        print(f"O", nome1,"desmaiou!\n",nome2,"é o vencedor!")
        
    elif novohp2 <= 0:
        print(f"O", nome2,"desmaiou!\n",nome1,"é o vencedor!")
    else:
        print(f"O",nome1,"está com",novohp1,"de hp\n","O",nome2,"está com",novohp2,"de hp")
        print("A batalha continua!")'''
    