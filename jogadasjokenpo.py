jogadas = ["papel", "pedra", "tesoura"]  # lista com as opções possíveis do jogo (índices 0,1,2)
jogador = input ("Faça sua jogada: ").lower()  # lê a jogada do usuário e normaliza para minúsculas

import random  # importa o módulo random para escolher jogada do computador
posicao = random.randint(0,2)  # gera um inteiro aleatório entre 0 e 2 (inclusivos) para escolher a jogada do PC

pc = jogadas[posicao]  # obtém a jogada do computador a partir da lista usando o índice gerado

if jogador == pc:  # se a escolha do jogador for igual à do computador -> empate
    print("Empate!")  # informa empate
elif (jogador == "papel" and pc == "pedra") or (jogador == "pedra" and pc == "tesoura") or (jogador == "tesoura" and pc == "papel"):  # verifica todas as combinações em que o jogador vence
    print("Você ganhou!")  # informa vitória do jogador
else:
    print("Você perdeu!")  # em qualquer outro caso válido, o jogador perde (inclui também entradas invalidas não tratadas)
    # Na linha 9 -> if jogador not in jogadas:
    #                   print("Entrada inválida!") 
    #               elif jogador == pc:  
    #                   print("Empate!")
    #               elif (jogador == "papel" and pc == "pedra") or (jogador == "pedra" and pc == "tesoura") or (jogador == "tesoura" and pc == "papel"):  # verifica todas as combinações em que o jogador vence
    #                   print("Você ganhou!")
    #               else:
    #                   print("Você perdeu!")
    # É importante essa verificação acontecer antes da comparação de jogadas empate!