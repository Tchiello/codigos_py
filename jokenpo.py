pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'

jogador1 = input('Faça sua jogada: ')
jogador2 = input('Faça sua jogada: ')

if jogador1 == tesoura:
    if jogador2 == tesoura:
        print('Empate')
    elif jogador2 == pedra:
        print('Jogador 2 Ganhou')
    elif jogador2 == papel:
        print('Jogador 1 Ganhou')

elif jogador1 == pedra:
    if jogador2 == pedra:
        print('Empate')
    elif jogador2 == tesoura:
        print('Jogador 1 Ganhou')
    elif jogador2 == papel:
        print('Jogador 2 Ganhou') 

elif jogador1 == papel:
    if jogador2 == papel:
        print('Empate')
    elif jogador2 == pedra:
        print('Jogador 1 Ganhou')
    elif jogador2 == tesoura:
        print('Jogador 2 Ganhou')