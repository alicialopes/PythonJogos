import random

def jogar():
    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    # print(numero_secreto)

    print("Qual nível de dificuldade?")
    print("(1) Fácil", "(2) Médio", "(3) Difícil\n", sep="\n")

    nivel = int(input("Digite o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        # print(f'Tentativa {rodada} de {total_de_tentativas}')

        chute = input("Digite a sua tentativa com um número de 1 a 100: ")
        tentativa = int(chute)
        print("Você digitou o número:", tentativa)

        if(tentativa < 1 or tentativa > 100):
            print("\nVocê deve digitar um número entre 1 e 100.\n")
            continue

        acertou     = tentativa == numero_secreto
        chute_maior = tentativa > numero_secreto
        chute_menor = tentativa < numero_secreto

        if (acertou):
            print(f"\nVocê acertou e fez {pontos} pontos!")
            break
        else:
            if(chute_maior):
                print("\nVocê errou! Seu chute foi maior que o número secreto.\n")
            elif(chute_menor):
                print("\nVocê errou! Seu chute foi menor que o número secreto.\n")
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos

        rodada += 1

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()