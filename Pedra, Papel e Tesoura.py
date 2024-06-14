# Fazerjogo Pedra Papel e Tesoura
from random import randint

# Codigos para movimentos do jogador!
movimentos = ['pedra', 'papel', 'tesoura']

while True:
    computer = movimentos[randint(0,2)]
    player = input("Pedra,Papel ou Tesoura? (Ou fim de Jogo")
    if player == "fim de jogo":
        print("O jogo terminou.")
        break
    elif player == computer
        print("O jogo empatou")
    elif player == "Pedra" and computer == "Papel":
        print ("Você Perdeu", computer, "beats", player)
        else("voce venceu", player, "beats", computer)
    elif player == "papel" and computer == "Tesoura":
        print("Você Perdeu", computer, "beats", player)
        else ("voce venceu", player, "beats", computer)
    elif player == "tesoura" and computer == "Pedra":
        print("Você Perdeu", computer, "beats", player)
        else ("voce venceu", player, "beats", computer)
    else:
        print ("cheque sua escrita")