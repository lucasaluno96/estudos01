#JOGO DE PAPEL PEDRA E TESOURA
import random
#lista de escolhas possiveis
opcao = ["papel", "pedra", "tesoura"]

#boas vindas
print("seja bem vindo ao GAME! escolha papel, pedra ou tesoura ")
jogador = input("escolha uma opçao: ")
pc = random.choice(opcao)

#opção de cada jogador
print(f"voce escolheu {jogador}")
print(f"o pc escolheu {pc}")

#opção de vitoria ou derrota
if jogador == pc:
    print("empate")
elif jogador == "pedra" and pc == "tesoura":
    print("voce ganhou")
elif jogador == "tesoura" and pc == "papel":
    print("parabens voce ganhou")
elif jogador == "papel" and pc == "pedra":
    print("parabes voce ganhou")
else:
    print("voce perdeu")
    a