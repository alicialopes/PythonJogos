import adivinhacao
import forca

def escolhe_jogo():
    print("\n*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************\n")

    print("(1) Adivinhação", "(2) Forca", sep="\n")

    jogo = int(input("\nQual jogo? "))

    if(jogo == 1):
        print("Jogando Adivinhação...\n")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando Forca...")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()