papel = "papel"
pedra = "pedra"
tesoura = "tesoura"

jogador1 = input("Jogador 1, escolha papel, pedra ou tesoura: ").lower()
jogador2 = input("Jogador 2, escolha papel, pedra ou tesoura: ").lower()

if jogador1 == jogador2:
    print("Empate!")
elif (jogador1 == papel and jogador2 == pedra) or (jogador1 == pedra and jogador2 == tesoura) or (jogador1 == tesoura and jogador2 == papel):
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")