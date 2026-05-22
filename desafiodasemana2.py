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
        valida = 0    
            
print("teste")    
        
            


    #print(nome1,"\nataque:",atk1,"\nhp:",hp1,"\n")
    #print(nome2,"\nataque:",atk2,"\nhp:",hp2)


#FUNÇÕES
def ataque(ataque,vida):
    hp = vida-ataque
    print(f"O",nome1,"atacou",nome2,"deixando ele com",hp,"de vida!")
    return(hp)
    
    
def contraataque(contraataque,vida):
    hp = vida-contraataque
    print(f"O",nome2,"contra atacou",nome1,"deixando ele com",hp,"de vida!")
    return(hp)

def batalha(atk1,atak2,hp1,hp2):
    novohp2 = hp2 - atk1
    novohp1 = hp1 - atak2
    
    
    #verificação de vitória
    if novohp1 <= 0 and novohp2 <=0:
        print("Ambos desmaiaram! Tivemos um empate!")
    elif novohp1 <= 0:
        print(f"O", nome1,"desmaiou!\n",nome2,"é o vencedor!")
    elif novohp2 <= 0:
        print(f"O", nome2,"desmaiou!\n",nome1,"é o vencedor!")
    else:
        print(f"O",nome1,"está com",novohp1,"de hp\n","O",nome2,"está com",novohp2,"de hp")
        print("A batalha continua!")
    