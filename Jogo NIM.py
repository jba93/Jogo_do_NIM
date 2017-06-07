#n = número de peças
#m = número máximo de peças a serem retiradas a cada jogada

def main():
    opcao = 0
    while (opcao!=1 and opcao!=2):
           print ("Bem-vindo ao jogo do NIM! Escolha:")
           print (" ")
           print ("1 - para jogar uma partida isolada")
           opcao = int (input ("2 - para jogar um campeonato "))
           print (" ")
    if (opcao==1):
            print ("Voce escolheu uma partida isolada!")
            partida()
    if (opcao==2):
           print ("Voce escolheu um campeonato!")
           campeonato()

def campeonato():
    for i in range (1, 4): #vai de 1 a 3 = 3 partidas
        print (" ")
        print ("**** Rodada", i,"****")
        print (" ")
        partida()
    print (" ")
    print ("**** Final do campeonato! ****")
    print ("Placar: Você", vj, "X", vc, "Computador")
    

def partida():
    computador = False
    usuario = False

    n = int (input ("Quantas peças? "))
    m = int (input ("Limite de peças por jogada? "))
    
    #jogador inicia a partida
    if ((n%(m+1))==0): #Se n é múltiplo de (m+1)
        print (" ")
        print ("Você começa!")
        usuario = True
        pecas_jog = usuario_escolhe_jogada(n, m)
        n = n - pecas_jog
        print ("Voce tirou", pecas_jog,"peças.")
        if (n!=0):
            print ("Agora restam", n, "peças no tabuleiro.")
        if (n==0):
            print("Fim do jogo! Você ganhou!")
            global vj
            vj = vj + 1
        
    #computador inicia a partida
    else:
        print (" ")
        print ("Computador começa!")
        computador = True
        pecas_comp = computador_escolhe_jogada(n, m)
        n = n - pecas_comp
        print (" ")
        if (pecas_comp==1):
            print ("O computador tirou uma peça.")
        else:
            print ("O computador tirou", pecas_comp, "peças!")
        if (n==1):
            print ("Agora resta apenas uma peça no tabuleiro.") 
        elif (n==0):
            print("Fim do jogo! O computador ganhou!")
            global vc
            vc = vc + 1
        else:
            print ("Agora restam", n, "peças no tabuleiro.")

    while n>0:
        #alternar jogadas
        if (computador == True):
            computador = False
            usuario = True
            pecas_jog = usuario_escolhe_jogada(n, m)
            n = n - pecas_jog
            print (" ")
            if (pecas_jog==1):
                print ("Voce tirou uma peça.")
            else:
                print ("Voce tirou", pecas_jog, "peças!")
            if (n==1):
                print ("Agora resta apenas uma peça no tabuleiro.") 
            elif (n==0):
                print("Fim do jogo! Você ganhou!")
                #global vj
                vj = vj + 1
                break
            else:
                print ("Agora restam", n, "peças no tabuleiro.")    
                
        if (usuario == True):
            usuario = False
            computador = True
            pecas_comp = computador_escolhe_jogada(n, m)
            n = n - pecas_comp
            print (" ")
            if (pecas_comp==1):
                print ("O computador tirou uma peça.")
            else:
                print ("O computador tirou", pecas_comp, "peças!")
            if (n==1):
                print ("Agora resta apenas uma peça no tabuleiro.") 
            elif (n==0):
                print("Fim do jogo! O computador ganhou!")
                #global vc
                vc = vc + 1
                break
            else:
                print ("Agora restam", n, "peças no tabuleiro.")
                
def computador_escolhe_jogada(n, m):
    #deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador
    #Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.
    computador = True
    i = 1
    while (i<=m and i<=n):
        if ((n-i)%(m+1)==0):
            return i
        else:
            i = i+1
    if m<=n:
        return m

def usuario_escolhe_jogada(n, m): #verifica se a quantidade de peças a ser retirada pelo jogador é válida
    usuario = True
    print (" ")
    pecas_jog = int (input("Quantas peças você vai tirar? "))
    while (pecas_jog>m or pecas_jog>n or pecas_jog<=0):
        print (" ")
        print ("Oops! Jogada inválida! Tente de novo.")
        print (" ")
        pecas_jog = int (input("Quantas peças você vai tirar? "))
    return pecas_jog

#num de vitórias do jogador e do computador
vj = 0
vc = 0
#início do programa
main() 



    


    
