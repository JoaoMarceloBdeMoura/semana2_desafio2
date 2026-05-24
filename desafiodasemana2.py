#FUNÇÕES

def exibir_placar():
    print("\nPLACAR:")
    print(nome1, "-", hp1, "HP")
    print(nome2, "-", hp2, "HP")

def ataque():
    global hp2

    hp2 = hp2 - atk1
    
    if hp2 <= 0:
        hp2 = 0
        print(f"O {nome1} atacou e {nome2} desmaiou!\n{nome1} é o vencedor!")       
        return 0

    else:
        print(f"O {nome1} atacou {nome2} causando {atk1} de dano e deixando ele com {hp2} de vida!")
        print("A batalha continua!") 
        return hp2
        
    
    
def contraataque():
    global hp1

    hp1 = hp1 - atk2
    
    if hp1 <= 0:
        hp1 = 0
        print(f"O {nome2} atacou e {nome1} desmaiou!\n{nome2} é o vencedor!")       
        return 0

    else:
        print(f"O {nome2} atacou {nome1} causando {atk2} de dano e deixando ele com {hp1} de vida!")
        print("A batalha continua!") 
        return hp1


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
        while hp1 > 0 and hp2 > 0:

            print("Que comece o duelo!")

            resultado = ataque()
            exibir_placar()

            if resultado == 0:
                print("Final do duelo")
                valida = 0
                break

            resultado = contraataque()
            exibir_placar()
            
            if resultado == 0:
                print("Final do duelo")
                valida = 0
                break
    